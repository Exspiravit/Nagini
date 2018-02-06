# -*- coding: utf-8 -*-

import telegram
import random
from telegram.ext import Updater, CommandHandler
from resources import token

mi_bot         = telegram.Bot(token=token)
mi_bot_updater = Updater(mi_bot.token)

def manza(bot=mi_bot, updater=mi_bot_updater):
    bot.sendMessage(chat_id=updater.message.chat_id, text="El es mi creador.")
    bot.sendMessage(chat_id=updater.message.chat_id, text="Me creo con Python.")

def Python(bot=mi_bot, updater=mi_bot_updater):
    Python_1 = bot.sendMessage(chat_id=updater.message.chat_id, text="Python es facil y rapido.")
    Python_2 = bot.sendMessage(chat_id=updater.message.chat_id, text="Cuack")
    Python_3 = bot.sendMessage(chat_id=updater.message.chat_id, text="A mi creadir le gusta programar :P")
    lista_variables_python = [Python_1,Python_2,Python_3]
    elegir_python = random.choise(lista_variables_python)
    bot.sendMessage(chat_id=updater.message.chat_id, text=str(elegir_python))

def saludame(bot=mi_bot, updater=mi_bot_updater):
    Python1 = bot.sendMessage(chat_id=updater.message.chat_id,text = "Holaaaa!")
    Python2 = bot.sendMessage(chat_id=updater.message.chat_id,text = "Saludos")
    Python3 = bot.sendMessage(chat_id=updater.message.chat_id,text = "Te saludo")
    lista_variables_python = [Python_1,Python_2,Python_3]
    elegir_python = random.choise(lista_variables_python)
    bot.sendMessage(chat_id=updater.message.chat_id, text=str(elegir_python))

manza_handler    = CommandHandler('manza',manza)
python_handler   = CommandHandler('python',Python)
saludame_handler = CommandHandler('saludame',saludame)

dispatcher       = mi_bot_updater.dispatcher

dispatcher.add_handler(manza_handler)
dispatcher.add_handler(python_handler)
dispatcher.add_handler(saludame_handler)

mi_bot_updater.start_polling()

while True:
    pass