import telebot
import config
import bot_config
import main
import random
import podcaper
from telebot import types


bot = telebot.TeleBot(config.TOKEN)
users = {}



# keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard = True)


@bot.message_handler(commands=['start'])
def welcome(message):
	#sticker = open ('stickers/sticker1.webp', 'rb')
	#bot.send_sticker(message.chat.id, sticker)
	#item1 = types.KeyboardButton("Отправь-ка мемасек")
	#item2 = types.KeyboardButton("Пагаварим?")
	#markup.add(item1, item2)
	bot.send_message(message.chat.id, "ПРИВЕТ МАЛЫЖКА, {0.first_name}!!".format(message.from_user, bot.get_me(), parse_mode = 'html'), reply_markup = markup)


@bot.message_handler(commands=['pikup'])
def pick_up_handler(message):
    item1 = types.KeyboardButton("Рамантешный")
    item2 = types.KeyboardButton("Глупый")
    item3 = types.KeyboardButton("Интеллектуальный")
    item4 = types.KeyboardButton("Политический")
    markup.add(item1, item2, item3, item4)


@bot.message_handler(content_types=['text'])
def replier(message):
    if message.chat.type == 'private':
        print(message.text, message.chat.id, message.from_user.username, message.message_id)
        podcaper.get_user_info(message)
        bot.send_message(message.chat.id, main.bot(message.text))




bot.polling(none_stop = True)
