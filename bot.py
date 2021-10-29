import os
import logging
import time
import pandas as pd

from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from api.utils.static_text import ABOUT, START, STICKER, INPUT_ERROR

from api.utils.artist_list import artist_list
from api.utils.name_check import name_check
from api.core.parser import parser
from api.utils.artist_to_dict import artist_dict
from api.core.tf_idf import tf_idf
from api.utils.similar_artists import similiar_artists
# Логирование
logging.basicConfig(filename='log.log',
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
    await message.reply(START % user_name)


@dp.message_handler(commands=['about'])
async def process_help_command(message: types.Message):
    await message.reply(ABOUT)

@dp.message_handler(commands=['list'])
async def process_list_command(message: types.Message):
    await message.reply(artist_list())

# main handler
@dp.message_handler()
async def echo_message(message: types.Message): # waits txt
    
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    exist_authors = pd.read_csv('api/data/exist_artists.csv')

    logging.info(f'{user_id} wrote {text} at {time.asctime()}')
    
    if len(text) > 30:
        await bot.send_message(user_name, 'Please, enter artist\'s name no longer than 30 symbols')
    else:
        name = name_check(text)
        if name == 'name_error':
            await message.reply(f'Can\'t find {text}, check whether name is spelled correctly')
        elif name not in exist_authors.values:
            logging.info(f'Database upd: {name}')
            await bot.send_sticker(user_id, STICKER)
            # await bot.send_message(user_id, 'Updating database - this might take a while')
            parser(name)
            artist_dict(name)
            tf_idf()
            # add artist to artists data file
            exist_authors.loc[exist_authors.index.max() + 1] = name
            exist_authors.to_csv('api/data/exist_artists.csv')
            await bot.send_message(user_id, similiar_artists(name))
        else:
            await bot.send_message(user_id, similiar_artists(name))

# обработчик на случай, если был прислан не текст, а стикер, фото или любой другой тип данных
@dp.message_handler(content_types='any')
async def unknown_message(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(user_id, INPUT_ERROR)

if __name__ == '__main__':
    executor.start_polling(dp)
    