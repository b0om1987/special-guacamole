import logging
import os
from time import sleep
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types
from config import bot, dp, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT




async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler(commands=['start', 'help'])
async def help(message: types.Message):
    await message.answer('Это эхо бот. Он всё повторяет за вами.')


@dp.message_handler(commands=['image', 'img'])
async def imag(message: types.Message):
    with open('img/92c785b8-6540-421f-9b97-b65e75dc3daa.__CR0,0,1164,720_PT0_SX970_V1___.jpg', 'rb') as photo:
    	await message.reply_photo(photo, caption='LEGO STAR WARS NIGGA!')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

endless = 1
while endless == 1:
    sleep(1800)
    endless = 1
