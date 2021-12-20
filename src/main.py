import telebot
from helpers import *
from private import token

ariadne = telebot.TeleBot(token)


@ariadne.message_handler(commands=['start'])
def command_start(message):
    ariadne.send_message(message.chat.id, 'Hi! My name is Ariadne. I will be your virtual assistant ❤')
    ariadne.send_message(message.chat.id, 'All of my available texts: ' + getDictionaryValues(supported_texts))


@ariadne.message_handler(content_types=['text'])
def get_text(message):
    txt = message.text.lower()
    if txt in supported_texts:
        ariadne.send_message(message.chat.id, supported_texts[txt])
    else:
        ariadne.send_message(message.chat.id, 'Sorry, I don\'t support this text yet :(')


ariadne.polling(none_stop=True, interval=0)
