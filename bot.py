import os
import logging
import time

from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from api.utils.static_text import START, TYPE

from api.model import img_search
from api.recommender import rec_music

# Логирование
logging.basicConfig(filename='log.log',
                    encoding='utf-8',
                    level=logging.INFO)

# Загрузка токена через env
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'{user_id} запустил бота в {time.asctime()}')
    await message.reply(START %user_name)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(message: types.Message):
    if message.content_type not in TYPE:
        await bot.send_message(message.from_user.id, 'Wrong type')
    elif not message.text.isalpha():
        await bot.send_message(message.from_user.id, 'No numbers or special')
    elif len(message.text) > 10:
        await bot.send_message(message.from_user.id, 'Wrong size')
    else:
        user_name = message.from_user.full_name
        user_id = message.from_user.id
        logging.info(f'Нам написал {user_name}, его id = {user_id}')
        await bot.send_message(user_id, rec_music(message.text))

        await bot.send_message(message.from_user.id, img_search(message.text))

    
    # await bot.send_message(message.from_user.id, square(int(message.text)))


if __name__ == '__main__':
    executor.start_polling(dp)
    