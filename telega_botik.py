import logging
import os
from time import sleep
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from config import bot, dp, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
import PIL
from PIL import Image
import random
from random import randint




async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler(commands=['start', 'help'])
async def help(message: types.Message):
    await message.answer('Это эхо бот. Он всё повторяет за вами.')


@dp.message_handler(commands=['image', 'img'])
async def imag(message: types.Message):
    first_layer_image = Image.open('img/head/head_'+str(randint(1, 3))+'.png')
    second_layer_image = Image.open('img/eyes/eyes_'+str(randint(1, 3))+'.png')
    first_layer_image.paste(second_layer_image, (0,0), second_layer_image)
    img = first_layer_image
#    width, height = img.size
#    for temp1 in range(width):
#        for temp2 in range(height):
#            if img.getpixel((temp1, temp2)) == (255, 0, 0, 255):
#                img.putpixel((temp1, temp2), (randint(110, 150), randint(8, 20), randint(80, 120), 255))
#            if img.getpixel((temp1, temp2)) == (0, 255, 0, 255):
#                img.putpixel((temp1, temp2), (randint(10, 20), randint(210, 220), randint(110, 120), 255))        
#    img = img.resize((1023, 1023), 0)
    await message.reply_photo(img) 


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
