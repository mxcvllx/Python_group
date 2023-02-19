from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

languages_btn = ReplyKeyboardMarkup(resize_keyboard=True)
result_btn = ReplyKeyboardMarkup(resize_keyboard=True)

LANGUAGES = {
    "UZ": "uz",
    "RU": "ru",
    "EN": "en"
}

languages_btn.add(
    KeyboardButton(list(LANGUAGES.keys())[0]),
    KeyboardButton(list(LANGUAGES.keys())[1]),
    KeyboardButton(list(LANGUAGES.keys())[2])
)


def language(value):
    languages_inline_btn = InlineKeyboardMarkup()
    languages_inline_btn.add(
        InlineKeyboardButton(list(LANGUAGES.keys())[0],
                             callback_data=f"{value}_language_{list(LANGUAGES.values())[0]}"),
        InlineKeyboardButton(list(LANGUAGES.keys())[1],
                             callback_data=f"{value}_language_{list(LANGUAGES.values())[1]}"),
        InlineKeyboardButton(list(LANGUAGES.keys())[2], callback_data=f"{value}_language_{list(LANGUAGES.values())[2]}")
    )
    return languages_inline_btn


phone = ReplyKeyboardMarkup(resize_keyboard=True)
phone.add(KeyboardButton("Share phone", request_contact=True))


def csv_file(action):
    save = {
        "NO": "no",
        "YES": "yes"
    }
    result_inline_btn = InlineKeyboardMarkup()
    result_inline_btn.add(
        InlineKeyboardButton(list(save.keys())[0], callback_data=f"{action}_{list(save.values())[0]}"),
        InlineKeyboardButton(list(save.keys())[1], callback_data=f"{action}_{list(save.values())[1]}"),
    )
    return result_inline_btn