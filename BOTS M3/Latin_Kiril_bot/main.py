from kiril_latin import to_cyrillic, to_latin
from environs import Env
import telebot

env = Env()
env.read_env()
BOT_TOKEN = env("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    a = "Salom \nmatn kiriting:"
    bot.reply_to(message, a)


@bot.message_handler(func=lambda message: True)
def ech_all(message):
    mesagg = message.text
    javob = lambda mesagg: to_cyrillic(mesagg) if mesagg.isascii() else to_latin(mesagg)
    bot.reply_to(message, javob(mesagg))


if __name__ == "__main__":
    bot.polling()
