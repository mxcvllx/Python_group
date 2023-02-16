from datetime import datetime
import telebot
from environs import Env
from telebot.types import BotCommand

from get_data import get_data
from BOTS.Weather_APP_bot.keybosrds import days_inline_btn
from BOTS.Weather_APP_bot.keybosrds import weather_inline_btn

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html")


# /weather
@bot.message_handler(commands=["weather"])
def weather_handler(message):
    today = datetime.now()
    weather_data = get_data()
    today_weather = None
    for day_weather in weather_data:
        day_date = datetime.strptime(day_weather.get("day"), "%Y.%m.%d")
        if day_date.date() == today.date():
            today_weather = day_weather
    msg = f"сегоднешняя погода ->:\n\n" \
          f"градус ->{today_weather.get('Средняя тепература')}"
    bot.send_message(message.chat.id, msg, parse_mode="html", reply_markup=days_inline_btn)


@bot.callback_query_handler(func=lambda call: True)
def weather_handler(call):
    if call.data == "5":
        bot.send_message(call.message.chat.id, "Entry date ", reply_markup=weather_inline_btn)
    if call.data != "5":
        bot.send_message(call.message.chat.id, f"{call.data}")


def my_commands():
    return [
        BotCommand("/weather", "Сегоднящная погода")
    ]


if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()