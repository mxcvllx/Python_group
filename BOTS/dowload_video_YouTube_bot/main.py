from aiogram import *
from BOTS.dowload_video_YouTube_bot.config import BOT_TOKEN
from pytube import YouTube

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['/start'])
async def start_message(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Привет я могу скачывать виде с ютуба\n"
                                    "отправь мне ссылку на видео")


@dp.message_handler()
async def text_message(message: types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == "https://youtu.be/" or "https://www.youtube.com":
        await bot.send_message(chat_id, f'*Начинаю загрузку видео* : *{yt.title}*/n'
                                        f'*С канала* : [{yt.author}], ({yt.channel_url})', parse_mode="MarkDown")


if __name__ == "__main__":
    executor.start_polling(dp)
