from aiogram import Bot, Dispatcher, types, executor
from config import *
from inlinebutton import *
from button import *
from text import *

bot = Bot(my_token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Я работаю')

# Команда старт
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(select_group_text, parse_mode='HTML', reply_markup=ikb_start)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)