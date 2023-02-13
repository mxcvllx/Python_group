import telebot
from telebot.types import BotCommand
from environs import Env
from datetime import datetime, date

env = Env()
env.read_env()
BOT_TOKEN = env("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    user = message.from_user
    answer = f"HEllO {user.first_name}"
    answer += "\nEnter your birthyear (exm: 2000):"
    bot.reply_to(message, answer)


@bot.message_handler(func=lambda message: True)
def calculate_age(message):
    today = date.today()
    a = int(message)
    age = (today.year - message)
    bot.reply_to(a, f"Your Age: {age}")


def my_commands():
    return [
        BotCommand("/start", "Start bot")
    ]


if __name__ == "__main__":
    bot.set_my_commands(commands=my_commands())
    bot.polling()
