# -*- coding: utf-8 -*-


from resources import token
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time

import text

bot = telebot.TeleBot(token)



#Listener [Se ejecuta cada ves que el bot recibe algun mensaje]
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


#Mensaje de bienvenida para nuevos usuarios en un chat grupal
@bot.message_handler(content_type=["new_chat_members"])
def bienvenida(m):
    bot.send_message(m.chat.id,text.bienvenida)

#Mensaje de despedida para usuarios en un chat grupal
@bot.message_handler(content_type=["left_chat_member"])
def despedida(m):
    bot.send_message(m.chat.id,text.adios)


#Mensaje de ayuda
@bot.message_handler(commands=['ayuda']) # Indicamos que lo siguiente va a controlar el comando '/ayuda'
def command_ayuda(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_chat_action(cid, 'typing') # Enviando ...
    time.sleep(1) #La respuesta del bot tarda 1 segundo en ejecutarse
    bot.send_message( cid, text.ayuda) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.

#Mensaje de info
@bot.message_handler(commands=['info']) # Indicamos que lo siguiente va a controlar el comando '/ayuda'
def command_info(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_chat_action(cid, 'typing') # Enviando ...
    time.sleep(1) #La respuesta del bot tarda 1 segundo en ejecutarse
    bot.send_message( cid, text.info) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.

#Mensaje con las reglas del grupo
@bot.message_handler(commands=['rules'])
def command_rules(m):
    cid = m.chat.id
    rules = []
    for a in range(5):
        if a > 0:
            r = open('./img/rules/'+str(a)+'.jpeg','rb')
            rules.append(r)

    bot.send_chat_action(cid,'typing')
    time.sleep(1)
    bot.send_message(cid, text.rules)
    for a in range(4):
        bot.send_photo(cid,rules[a])

@bot.message_handler(commands=['hola'])
def command_hola(m):
    bot.send_message(m.chat.id,text.bienvenida)

# Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
bot.set_update_listener(listener) 
#Iniciamos el bot
bot.polling()