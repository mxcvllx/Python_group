import telebot
from TRELLO_BOT import messages
from environs import Env
from state import CreateNewTask
from trello import TrelloManager
from utils import write_chat_to_csv, check_chat_id_from_csv, \
    get_member_tasks_message, get_trello_username_by_chat_id
from keyboards import get_inline_boards, get_inline_lists_btn, \
    get_list_btn, get_member_btn

env = Env()
env.read_env()
BOT_TOKEN = env("BOT_TOKEN")
state_storage = telebot.storage.StateMemoryStorage()
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='html')


# /start
@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, messages.WELCOME_MSG)


# /cancel
@bot.message_handler(commands=["cancel"])
def exit_start(message):
    bot.send_message(message.chat.id, messages.CANCEL)


# /register
@bot.message_handler(commands=["register"])
def register_handler(message):
    if not check_chat_id_from_csv("chats.csv", message.chat.id):
        bot.send_message(message.chat.id, messages.SEND_TRELLO_USERNAME)
        bot.register_next_step_handler(message, get_trello_username)
    else:
        bot.send_message(message.chat.id, messages.ALREADY_REGISTERED)


# Trello username
def get_trello_username(message):
    write_chat_to_csv('chats.csv', message)
    bot.send_message(message.chat.id, messages.ADD_SUCCESFULLY)


# /boards
@bot.message_handler(commands=['boards'])
def boards_info(message):
    if not check_chat_id_from_csv('chats.csv', message.chat.id):
        bot.send_message(message.chat.id, messages.TRELLO_USERNAME_NOT_FOUND)
    else:
        trello_user = get_trello_username_by_chat_id('chats.csv', message.chat.id)
        if trello_user:
            bot.send_message(
                message.chat.id, messages.SELECT_BOARD, reply_markup=get_inline_boards(trello_user, 'show_tasks')
            )
        else:
            bot.send_message(message.chat.id, messages.TRELLO_USERNAME_NOT_FOUND)


@bot.callback_query_handler(lambda c: c.data.startwith('show_tasks'))
def boards_list_info(cal):
    message = cal.message
    trello_username = get_trello_username_by_chat_id('chats.csv', message.chat.id)
    trello = TrelloManager(trello_username)
    boards_id = cal.data.split('_')[2]
    bot.send_message(
        message.chat.id, 'Listni tanlang:', reply_markup=get_inline_lists_btn(trello, boards_id, 'show_list_tasks')
    )


@bot.callback_query_handler(lambda call: call.data.startwith('show_list_tasks_'))
def members_cards(call):
    message = call.message
    list_id = call.data.split('_')[3]
    trello_user_name = get_trello_username_by_chat_id('chats.csv', message.chat.id)
    trello = TrelloManager(trello_user_name)
    cards_data = trello.get_cards_on_a_list(list_id)
    msg = get_member_tasks_message(cards_data, trello.get_member_id())

    if msg:
        bot.send_message(message.chat.id, msg)

    else:
        bot.send_message(message.chat.id, messages.NO_TASKS)


@bot.message_handler(commands=['new task'])
def new_tasks(message):
    if not check_chat_id_from_csv('chats.csv', message.chat.id):
        bot.send_message(message.chat.id, messages.TRELLO_USERNAME_NOT_FOUND)
    else:
        trello_user_name = get_trello_username_by_chat_id('chats.csv', message.chat.id)
        if trello_user_name:
            bot.send_message(
                message.chat.id, messages.CREATE_TASK,
                reply_markup=get_inline_boards(trello_user_name, 'new_tasks')
            )
            bot.set_state(message.from_user.id, CreateNewTask.boards, message.chat.id)
        else:
            bot.send_message(message.chat.id, messages.TRELLO_USERNAME_NOT_FOUND)


@bot.callback_query_handler(lambda call: call.data.startwith('new_tasks_'), state=CreateNewTask.boards)
def new_task_name(call):
    message = call.message
    trello_user_name = get_trello_username_by_chat_id('chats.csv', message.chat.id)
    trello = TrelloManager(trello_user_name)
    boards_id = call.data.split('_')[2]
    bot.send_message(
        message.chat.id, messages.NEW_LIST, reply_markup=get_list_btn(trello, boards_id)
    )
    bot.set_state(message.from_user.id, CreateNewTask.list, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['tasks_board_id'] = boards_id


@bot.message_handler(state=CreateNewTask.list)
def list_if_new_task(message):
    bot.send_message(message.chat.id, messages.TASK_NAME)
    bot.set_state(message.from_user.id, CreateNewTask.name, message.chat.id)


@bot.message_handler(state=CreateNewTask.name)
def get_task_name(message):
    bot.send_message(message.chat.id, messages.TASK_DESC)
    bot.set_state(message.from_user.id, CreateNewTask.description, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['task_name'] = message.text
        params = {
            'name': data['name'],
            'desc': data['desc'],
        }


@bot.message_handler(state=CreateNewTask.description)
def get_task_description(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['task_desc'] = message.text
        board_id = data['task_board_id']
        trello_user_name = get_trello_username_by_chat_id('chats.csv', message.chat.id)
        bot.send_message(
            message.chat.id, messages.TASK_MEMBERS, get_member_btn(trello_user_name, board_id, 'new_task_member')
        )
        bot.set_state(message.from_user.id, CreateNewTask.members, message.chat.id)


@bot.callback_query_handler(lambda c: c.data.startswith("new_task_member_"))
def get_member_id(call):
    message = call.message
    member_id = call.data.split("_")[3]
    bot.send_message(message.chat.id, messages.TASK_LABELS)
    bot.set_state(message.from_user.id, CreateNewTask.members, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["member_id"] = member_id


my_commands = [
    telebot.types.BotCommand("/start", "Boshlash"),
    telebot.types.BotCommand("/register", "Ro'yxatdan o'tish"),
    telebot.types.BotCommand("/new", "Yangi task yaratish."),
    telebot.types.BotCommand("/cancel", "Bekor qilish ?"),
    telebot.types.BotCommand("/boards", "Doskalarni ko'rish"),
    telebot.types.BotCommand("/help", "Yordam")
]

if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(my_commands)
    bot.infinity_polling()