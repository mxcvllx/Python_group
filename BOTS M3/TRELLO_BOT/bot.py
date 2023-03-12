import telebot
from environs import Env
from psycopg2.extras import RealDictCursor

import messages
from db import queries, connection
from keyboards import get_inline_boards_btn
from sync import sync_boards
from trello import TrelloManager
from utils import get_user_tasks_message

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
state_storage = telebot.storage.StateMemoryStorage()
bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage, parse_mode="html")


# /start
@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, messages.WELCOME_MSG)


# /cancel
@bot.message_handler(commands=["cancel"])
def welcome(message):
    bot.send_message(message.chat.id, messages.CANCEL)


@bot.message_handler(commands=["register"])
def register_handler(message):
    chat_id = message.chat.id
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.GET_USER_BY_CHAT_ID, (chat_id,))
        user = cur.fetchone()
        if not user:
            chat = message.from_user
            cur.execute(queries.REGISTER_USER, (chat_id, chat.first_name, chat.last_name, chat.username))
            connection.commit()
            bot.send_message(message.chat.id, messages.SEND_TRELLO_USERNAME)
            bot.register_next_step_handler(message, get_trello_username)
        else:
            bot.send_message(message.chat.id, messages.ALREADY_REGISTERED)


# Trello username
def get_trello_username(message):
    with connection.cursor() as cur:
        trello_username = message.text
        trello_id = TrelloManager(trello_username).get_member_id()
        cur.execute(
            queries.UPDATE_USER_TRELLO_BY_CHAT_ID, (trello_username, trello_id, message.chat.id)
        )
        connection.commit()
    bot.send_message(message.chat.id, messages.ADD_SUCCESSFULLY)


@bot.message_handler(commands=["sync"])
def sync_trello_handler(message):
    bot.send_message(message.chat.id, messages.SYNC_STARTED)
    # Sync Trello
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.GET_USER_BY_CHAT_ID, (message.chat.id,))
        user = cur.fetchone()
        trello_username = user.get("trello_username")
        sync_boards(trello_username)
    bot.send_message(message.chat.id, messages.SYNC_ENDED)


@bot.message_handler(commands=["tasks"])
def sending_tasks_handler(message):
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.GET_USER_BY_CHAT_ID, (message.chat.id,))
        user = cur.fetchone()
        trello_username = user.get("trello_username")
    if trello_username:
        bot.send_message(
            message.chat.id, messages.SELECT_BOARD,
            reply_markup=get_inline_boards_btn(user.get("id"), "tasks_board")
        )
    else:
        bot.send_message(message.chat.id, messages.TRELLO_USERNAME_NOT_FOUND)


@bot.callback_query_handler(lambda c: c.data.startswith("tasks_board"))
def get_user_tasks_handler(call):
    message = call.message
    chat_id = message.chat.id
    board_id = call.data.split("_")[2]
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.GET_USER_BY_CHAT_ID, (chat_id,))
        user = cur.fetchone()
        if user:
            cur.execute(queries.GET_USER_CARDS_BY_BOARD_ID, (board_id, user.get("id")))
            cards = cur.fetchall()
            if cards:
                bot.send_message(chat_id, get_user_tasks_message(cards))
            else:
                bot.send_message(chat_id, messages.NO_TASKS)
        else:
            bot.send_message(chat_id, messages.USER_NOT_FOUND)


my_commands = [
    telebot.types.BotCommand("/start", "Boshlash"),
    telebot.types.BotCommand("/register", "Ro'yxatdan o'tish"),
    telebot.types.BotCommand("/tasks", "Vazifalarni ko'rish"),
    telebot.types.BotCommand("/new", "Yangi task yaratish"),
    telebot.types.BotCommand("/sync", "Trello sinxronizatsiya"),
    telebot.types.BotCommand("/cancel", "Bekor qilish"),
    telebot.types.BotCommand("/help", "Yordam")
]

if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(my_commands)
    bot.infinity_polling()