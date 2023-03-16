from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ContentType
from aiogram.utils import executor
import logging
from aiogram import Bot
import bot_token
from aiogram import types as tp

from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(bot_token.get_token())
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.DEBUG)

keyboard_start = tp.InlineKeyboardMarkup(row_width=1)\
    .add(tp.InlineKeyboardButton(text='Movie Time!', url="https://t.me/movie_time85"))


@dp.message_handler(commands='start')
async def start(message: tp.Message):
    await message.answer(
        'The best telegram channel about films and the film industry,\n'
        ' subscribe and there will be no more problems in choosing a film for the evening',
        reply_markup=keyboard_start
    )


if __name__ == '__main__':
    executor.start_polling(dp)
