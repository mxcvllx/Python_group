from datetime import datetime

from get_data import get_data
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

days_btn = {
    "Weather for 5 days": "5"
}

days_inline_btn = InlineKeyboardMarkup()

days_inline_btn.add(
    InlineKeyboardButton(list(days_btn.keys())[0], callback_data=list(days_btn.values())[0])
)


def get_dict_info():
    weather_data = get_data()
    weather = []
    days = []
    for day_weather in weather_data:
        day_date = datetime.strptime(day_weather.get("day"), "%Y.%m.%d")
        days.append(str(day_date.date()))
        weather.append(day_weather.get("average_temperature"))
    return {
        f"{days[0]}": f"{weather[0]} °C",
        f"{days[1]}": f"{weather[1]} °C",
        f"{days[2]}": f"{weather[2]} °C",
        f"{days[3]}": f"{weather[3]} °C",
        f"{days[4]}": f"{weather[4]} °C"
    }


weather_btn = get_dict_info()

weather_inline_btn = InlineKeyboardMarkup()

weather_inline_btn.add(
    InlineKeyboardButton(list(weather_btn.keys())[0], callback_data=list(weather_btn.values())[0]),
    InlineKeyboardButton(list(weather_btn.keys())[1], callback_data=list(weather_btn.values())[1]),
    InlineKeyboardButton(list(weather_btn.keys())[2], callback_data=list(weather_btn.values())[2]),
    InlineKeyboardButton(list(weather_btn.keys())[3], callback_data=list(weather_btn.values())[3]),
    InlineKeyboardButton(list(weather_btn.keys())[4], callback_data=list(weather_btn.values())[4])
)