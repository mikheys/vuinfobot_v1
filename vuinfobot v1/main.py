import telebot
from telebot import types
import logging

bot = telebot.TeleBot("5224125822:AAGkrKCzJyoXPE3Bv1CeQ8-cYFVbOTvhBek")
logging.basicConfig(level=logging.INFO)

mainmenu = ("""
*Экстренное*
/emergency - аварийные службы
/medical - медицинская помощь
/veterinary - ветеринарная помощь

*Контакты, инфо ВУ*

*Транспорт*
/transport - общественный транспорт
/taxi - такси

*Сервис*
/publicservice - коммунальные услуги

*Прочие услуги*
/others - прочие услуги
""")

def main_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard = True)
    btn1 = types.KeyboardButton('Главное меню.')
    markup.add(btn1)
    return markup

@bot.message_handler(commands=['start', 'mem'])
def main_message(message):
    # markup.add(item1)
    bot.send_message(message.chat.id, "*Выберите интересующий раздел и нажмите на команду.*", parse_mode= "Markdown", reply_markup=main_keyboard())
    bot.send_message(message.chat.id, mainmenu, parse_mode= "Markdown")


@bot.message_handler(commands=['emergency'])
def main_message(message):
    bot.send_message(message.chat.id, "https://teletype.in/@vuinfobot/OQx0XDEgb58", parse_mode= "Markdown")

@bot.message_handler(commands=['medical'])
def main_message(message):
    bot.send_message(message.chat.id, "https://telegra.ph/1-urok-Vvodnyj-10-25", parse_mode= "Markdown")

bot.polling()