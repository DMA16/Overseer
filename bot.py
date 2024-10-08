import telebot
import random
import logging
import get_data

logging.basicConfig(
    format=u'[%(asctime)s] %(levelname)s %(message)s',
    level=logging.INFO
)

bot = telebot.TeleBot(token=get_data.tg_token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте шлюшки!')


@bot.message_handler(content_types=['voice'])
def gay_voice(message):
    logging.info(message.voice.duration)
    if int(message.voice.duration) > 1:
        bot.reply_to(message, random.choice(get_data.swearings))
    else:
        bot.reply_to(message, 'Yoooo GANGSTER!!')


bot.infinity_polling()
