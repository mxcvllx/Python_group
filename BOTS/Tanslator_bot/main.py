from googletrans import Translator
from environs import Env
import telebot
import config as cfg

tran = Translator()
env = Env()
env.read_env()
BOT_TOKEN = env("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    a = "Salom \nmatn kiriting:"
    bot.reply_to(message, a)

