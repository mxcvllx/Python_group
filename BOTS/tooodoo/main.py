import telebot
from environs import Env
import csv
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand, ReplyKeyboardRemove
from key.key import phone, csv_file, languages_btn
from key.message import messages
from key.state import StudentRegistrationForm
from chatt import Chat
from key.utils import write_row_to_csv, get_fullname
from key.save_info import Save

env = Env()
env.read_env()
BOT_TOKEN = env("BOT_TOKEN")
state_storage = StateMemoryStorage()

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html", state_storage=state_storage)


# /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = get_fullname(user.first_name, user.last_name)
    bot.send_message(chat_id, f"Здраствуйте {fullname} отправьте команду /register для регистрации")


@bot.callback_query_handler(lambda call: call.data.startswith("language"))
def set_language_query_handler(call):
    message = call.message
    lang = call.data.split("_")[1]
    print(lang)
    chat = message.chat
    new_chat = Chat(
        chat.id,
        get_fullname(chat.first_name, chat.last_name),
        lang
    )
    write_row_to_csv(
        "chats.csv",
        list(new_chat.get_attrs_as_dict().keys()),
        new_chat.get_attrs_as_dict()
    )
    bot.delete_message(chat.id, message.id)
    bot.send_message(chat.id, messages[lang].get("add_task"))


@bot.message_handler(commands=["register"])
def register_student_handler(message):
    bot.send_message(message.chat.id, "Введите Имя:")
    bot.set_state(message.from_user.id, StudentRegistrationForm.first_name, message.chat.id)


@bot.message_handler(state=StudentRegistrationForm.first_name)
def first_name_get(message):
    bot.send_message(message.chat.id, 'Введите Фамилию:')
    bot.set_state(message.from_user.id, StudentRegistrationForm.last_name, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['first_name'] = message.text


@bot.message_handler(state=StudentRegistrationForm.last_name)
def last_name_get(message):
    bot.send_message(message.chat.id, 'Отправьте свой номер телефона:', reply_markup=phone)
    bot.set_state(message.from_user.id, StudentRegistrationForm.phone, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['last_name'] = message.text


@bot.message_handler(state=StudentRegistrationForm.phone, content_types=["contact"])
def phone_get(message):
    bot.send_message(message.chat.id, 'Введите свой возраст:', reply_markup=ReplyKeyboardRemove())
    bot.set_state(message.from_user.id, StudentRegistrationForm.age, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['phone'] = message.contact.phone_number


@bot.message_handler(state=StudentRegistrationForm.age)
def age_get(message):
    bot.send_message(message.chat.id, 'Выбрать язык:', reply_markup=languages_btn("course"))
    bot.set_state(message.from_user.id, StudentRegistrationForm.language, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = message.text


@bot.callback_query_handler(lambda call: call.data.startswith("course_language_"),
                            state=StudentRegistrationForm.language)
def language_get(call):
    message = call.message
    lang_code = call.data.split("_")[2]
    bot.send_message(message.chat.id, 'Введите курс:')
    bot.set_state(message.from_user.id, StudentRegistrationForm.course, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['language'] = lang_code
        print(lang_code)


@bot.message_handler(content_types=['text'])
def get_task_handler(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['course'] = message.text
        messagess = f"Была получена следующая информация:\n"
        messagess += f"Имя -->: {data.get('first_name')}\n"
        messagess += f"Фамилия -->: {data.get('last_name')}\n"
        messagess += f"Телефон -->: {data.get('phone')}\n"
        messagess += f"Возраст -->: {data.get('age')}\n"
        messagess += f"Язык -->: {data.get('language')}\n"
        messagess += f"Курс -->: {data.get('course')}\n"
        messagess += "Сохранить данные ?\n"
        messagess += "ДА -->\n"
        messagess += "НЕТ -->"
        bot.send_message(message.chat.id, messagess, reply_markup=csv_file('save'))


@bot.callback_query_handler(func=lambda call: call.data.startswith("save"))
def callback(call):
    message = call.message
    text = call.data.split("_")[1]
    if text == "yes":
        with bot.retrieve_data(call.from_user.id, message.chat.id) as data:
            save_info = Save(
                data.get('Имя'),
                data.get('Фамилия'),
                data.get("Телефон"),
                data.get("Возраст"),
                data.get("Язык"),
                data.get("Курс")
            )

        write_row_to_csv(
            "registration.csv",
            save_info.get_save_func().keys(),
            save_info.get_save_func()
        )

    elif text == "no":
        bot.send_message(message.chat.id, "Информация не сохранилась, введиет /register для введение новых данных")
    bot.delete_state(message.from_user.id, message.chat.id)


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/register", "Register student")
    ]


bot.add_custom_filter(custom_filters.StateFilter(bot))

if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
