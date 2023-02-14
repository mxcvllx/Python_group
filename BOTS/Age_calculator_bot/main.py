import telebot
from environs import Env

env = Env()
env.read_env()
BOT_TOKEN = env("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id,
                     f"Привет {user.first_name} \n"
                     f"Задача этого бота находить ваш возраст")


@bot.message_handler(func=lambda message: int)
def meesage_age(message):
    ms = message.text
    bot.reply_to(message, f"Ваш возраст равна --> {2023 - int(ms)} годам.")


if __name__ == "__main__":
    bot.infinity_polling()
