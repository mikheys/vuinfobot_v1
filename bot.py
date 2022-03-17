import logging
from aiogram.utils.callback_data import CallbackData
from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types.message import ContentTypes
# from aiogram.types.message import ContentType
import os
from flask import Flask

import config as cfg
import text as txt
import markups as nav

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)
app = Flask(__name__)
# --- Основное меню ---
@dp.message_handler(commands=["start"], commands_prefix="/")
async def start_menu(message: types.Message):
    await message.answer(txt.WELCOME, reply_markup=nav.startMenu)
    await message.answer("Выберите нужный раздел ", reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "Меню":
        # await message.delete()
        await message.answer("Выберите нужный раздел ", reply_markup=nav.mainMenu)
    else:
        # await message.reply('Неизвестная команда')
        await message.delete()



# --- Обработка пунктов меню ---
@dp.callback_query_handler(text="emergency")
async def randome(message: types.Message):
    await bot.send_message(message.from_user.id, "Экстренное:\nhttps://telegra.ph/emergency-03-16")
    await message.answer()

@dp.callback_query_handler(text="medical")
async def randome(message: types.Message):
    await bot.send_message(message.from_user.id, "Медицинская помощь:\nhttps://telegra.ph/medical-03-16-3")
    await message.answer()

@dp.callback_query_handler(text="veterinary")
async def randome(message: types.Message):
    await bot.send_message(message.from_user.id, "Ветеринарная помощь:\nhttps://telegra.ph/veterinary-03-16")
    await message.answer()

@dp.callback_query_handler(text="infovu")
async def randome(message: types.Message):
    await bot.send_message(message.from_user.id, "Контакты, инфо ВУ:\nhttps://telegra.ph/infovu-03-16")
    await message.answer()

@dp.callback_query_handler(text="transport")
async def randome(message: types.Message):
    await bot.send_message(message.from_user.id, "Общественный транспорт:\nhttps://telegra.ph/transport-03-16")
    await message.answer()

@dp.callback_query_handler(text="taxi")
async def randome(message: types.Message):
    await bot.send_message(message.from_user.id, "Такси:\nhttps://telegra.ph/taxi-03-16-2")
    await message.answer()

@dp.callback_query_handler(text="publicservice")
async def randome(message: types.Message):
    await bot.send_message(message.from_user.id, "Коммунальные услуги:\nhttps://telegra.ph/publicservice-03-16")
    await message.answer()

@dp.callback_query_handler(text="others")
async def randome(message: types.Message):
    await bot.send_message(message.from_user.id, "Прочие услуги:\nhttps://telegra.ph/others-03-16")
    await message.answer()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    executor.start_polling(dp, skip_updates = True)
