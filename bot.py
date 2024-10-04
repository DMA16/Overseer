import telebot
from config import TOKEN

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте шлюшки!')


@bot.message_handler(content_types=["text"])
def faggot_detector(message):
    bot.reply_to(message, 'Ты гей!')


bot.polling()
#bot.infinity_polling()