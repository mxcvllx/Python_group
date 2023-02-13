import config as cfg
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
a = 0
keyss = []
keyb = InlineKeyboardMarkup()
for i, j in cfg.LANGDICT.items():
    key = InlineKeyboardButton(j, callback_data=i)
    keyss.append(key)
    a+= 1;
    if a == 3:
        a = 0
        keyb.add(keyss[0], keyss[1], keyss[2])
        keyss = []