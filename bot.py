import os
import logging
import time
from aiogram.types import user

from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from api.utils.static_text import START, TYPE

from api.model import img_search
from api.recommender import rec_music
from api.utils.artist_list import artist_list
from aiogram.types import FSInputFile

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
    logging.info(f'{user_id} started bot at {time.asctime()}')
    await message.reply(START %user_name)


@dp.message_handler(commands=['about'])
async def process_help_command(message: types.Message):
    await message.reply("Tired of listening to the same artists? Write an artist you are interested in and i will suggest artists with similar (lyrics)!")

@dp.message_handler(commands=['list'])
async def process_list_command(message: types.Message):
    await message.reply(artist_list())

@dp.message_handler()
async def echo_message(message: types.Message): # waits txt
    # if message.content_type not in TYPE:
    #     await bot.send_message(message.from_user.id, 'Wrong type')
    if not message.text.isalpha():
        await bot.send_message(message.from_user.id, 'No numbers or special')
    elif len(message.text) > 15:
        await bot.send_message(message.from_user.id, 'Wrong size')
    else:
        user_name = message.from_user.full_name
        user_id = message.from_user.id
        logging.info(f'Нам написал {user_name}, его id = {user_id}')
        await bot.send_message(user_id, 'Данные в пути')
        await bot.send_message(user_id, rec_music(message.text))
        await bot.send_message(user_name, img_search(message.text))



if __name__ == '__main__':
    executor.start_polling(dp)
    