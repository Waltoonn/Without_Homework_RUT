from aiogram import Bot, Dispatcher, types, executor
from config import my_token

bot = Bot(my_token)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Я работаю asdasdas')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)