import telebot
from environs import Env

import messages
from trello import TrelloManager
from utils import write_chat_to_csv, check_chat_id_from_csv, get_trello_username_by_chat_id, get_member_tasks_message
from keyboards import get_boards_btn, get_lists_btn

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html")


# /start
@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, messages.WELCOME_MSG)


@bot.message_handler(commands=["register"])
def register_handler(message):
    if not check_chat_id_from_csv("chats.csv", message.chat.id):
        bot.send_message(message.chat.id, messages.SEND_TRELLO_USERNAME)
        bot.register_next_step_handler(message, get_trello_username)
    else:
        bot.send_message(message.chat.id, messages.ALREADY_REGISTERED)


# Trello username
def get_trello_username(message):
    write_chat_to_csv("chats.csv", message)
    bot.send_message(message.chat.id, messages.ADD_SUCCESSFULLY)


@bot.message_handler(commands=["boards"])
def get_boards(message):
    if not check_chat_id_from_csv("chats.csv", message.chat.id):
        bot.send_message(message.chat.id, messages.TRELLO_USERNAME_NOT_FOUND)
    else:
        trello_username = get_trello_username_by_chat_id("chats.csv", message.chat.id)
        if trello_username:
            bot.send_message(message.chat.id, messages.SELECT_BOARD, reply_markup=get_boards_btn(trello_username))
        else:
            bot.send_message(message.chat.id, messages.TRELLO_USERNAME_NOT_FOUND)
    bot.register_next_step_handler(message, get_board_lists)


def get_board_lists(message):
    trello_username = get_trello_username_by_chat_id("chats.csv", message.chat.id)
    trello = TrelloManager(trello_username)
    board_id = trello.get_board_id_with_name(message.text)
    bot.send_message(message.chat.id, "Listni tanlang:", reply_markup=get_lists_btn(trello, board_id))
    bot.register_next_step_handler(message, get_member_cards(board_id))


def get_member_cards(board_id):
    def inner(message):
        trello_username = get_trello_username_by_chat_id("chats.csv", message.chat.id)
        trello = TrelloManager(trello_username)
        list_data = trello.get_lists_on_a_board(board_id)
        list_id = trello.get_list_id_with_name(list_data, message.text)
        card_data = trello.get_cards_on_a_list(list_id)
        msg = get_member_tasks_message(card_data, trello.get_member_id())
        if msg:
            bot.send_message(message.chat.id, msg)
        else:
            bot.send_message(message.chat.id, messages.NO_TASKS)

    return inner


my_commands = [
    telebot.types.BotCommand("/start", "Boshlash"),
    telebot.types.BotCommand("/register", "Ro'yxatdan o'tish"),
    telebot.types.BotCommand("/boards", "Doskalarni ko'rish"),
    telebot.types.BotCommand("/help", "Yordam")
]

if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(my_commands)
    bot.infinity_polling()