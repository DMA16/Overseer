import telebot
import json
import random
import logging
#from config import TOKEN


logging.basicConfig(
    format=u'[%(asctime)s] %(levelname)s %(message)s',
    level=logging.INFO
)


def read_sw(path:str)->dict:
    with open(path, "r") as sw_file:
        return sw_file.readlines()


def read_conf(path:str)->dict:
    with open(path,"r") as conf_file:
        return json.loads(conf_file.read())


config = read_conf("env.json")
swearings=read_sw("swearings.txt")
bot = telebot.TeleBot(token=config["TG_TOKEN"])

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте шлюшки!')


#@bot.message_handler(func = lambda msg:msg.text!="")
@bot.message_handler()
def faggot_detector(message):
    logging.info(message)
    bot.reply_to(message, 'Ты гей!')


@bot.message_handler(content_types=['voice'])
def gay_voice(message):
    logging.info(message.voice.duration)
    if int(message.voice.duration) > 1:
        bot.reply_to(message, random.choice(swearings))
    else:
        bot.reply_to(message, 'Yoooo GANGSTER!!')
        

#bot.polling()
bot.infinity_polling()
