import requests
from BOTS.Weather_APP_bot.config import BOT_TOKEN, wether_api
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import telebot
from telebot.types import BotCommand

bot = Bot(token=BOT_TOKEN)
bott = telebot.TeleBot(BOT_TOKEN, parse_mode="html")
dp = Dispatcher(bot)


# /start....
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user_name = message.from_user
    await message.reply(f"Привет {user_name.first_name}, введите название города ")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q=" + message.text + "&appid=" + wether_api + "&units=metric"
        )
        data = r.json()

        city_name = data["name"]
        weather = data["main"]["temp"]

        await message.reply(f"Погода в городе -->: {city_name}\nТемпература: {weather}C°")
    except:
        await message.reply("Проверте название города")


def my_commands():
    return [
        BotCommand("/start", "Start bot")
    ]


if __name__ == "__main__":
    print("Started...")
    bott.set_my_commands(commands=my_commands())
    executor.start_polling(dp)
