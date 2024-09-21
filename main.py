from aiogram import Bot, Dispatcher, types, executor
from config import my_token

bot = Bot(my_token)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Я работаю')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)