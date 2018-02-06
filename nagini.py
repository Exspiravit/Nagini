# -*- coding: utf-8 -*-


from resources import token
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time

bot = telebot.TeleBot(token)

ayuda = """Puedes utilizar los siguientes comandos : 
            /ayuda  -   Guia para utilizar el bot. 
            /info   -   Informacion de interes sobre el grupo.
            /rules  -   Reglas del grupo. 
            /hola   -   Saludo del Bot"""

#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # El Cid es el identificador del chat los negativos son grupos y positivos los usuarios
        if cid > 0:
            mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text # Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre.
        else:
            mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text # Si 'cid' es negativo, usaremos 'm.from_user.first_name' para el nombre.
        f = open( 'log.txt', 'a') # Abrimos nuestro fichero log en modo 'Añadir'.
        f.write(mensaje + "\n") # Escribimos la linea de log en el fichero.
        f.close() # Cerramos el fichero para que se guarde.
        print(mensaje) # Imprimimos el mensaje en la terminal, que nunca viene mal :) 

@bot.message_handler(commands=['ayuda']) # Indicamos que lo siguiente va a controlar el comando '/ayuda'
def command_ayuda(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_chat_action(cid, 'typing') # Enviando ...
    time.sleep(1) #La respuesta del bot tarda 1 segundo en ejecutarse
    bot.send_message( cid, ayuda) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.

# Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
bot.set_update_listener(listener) 
#Iniciamos el bot
bot.polling()