from datetime import datetime

import telebot
from environs import Env

from weather import WeatherManager
from telebot.types import BotCommand
from student import Student
from utils import write_to_csv, is_exist_chat_id

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
    bot.send_message(chat_id, f"Assalomu aleykum {fullname}!")
    if not is_exist_chat_id(chat_id):
        student = Student(chat_id, fullname)
        write_to_csv(student)
    else:
        print("User already exist.")


@bot.message_handler(command=["weather"])
def weather_handler(message):
    today = datetime.now()
    weather_data = WeatherManager("tashkent").get_daily_temperature()
    today_weather = None
    for day_weather in weather_data:
        day_date = datetime.strptime(day_weather.get("day"), "%Y.%m.%d")
        if day_date.date() == today.date():
            today_weather = day_weather
    msg = f"Bugungi Ob-Havo:\n Harorat:{today_weather.get('tepmerature_avg')}"
    bot.send_message(message.chat.id, msg)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/weather", "Today weather")
    ]


if __name__ == "__main__":
    print("Started...")
    bot.infinity_polling()
