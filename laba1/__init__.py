import random
import telebot
from telebot import types

api_key = '6476669582:AAGLvFas1cs2wPylE8mQAPIxQdusfILlGMk'

bot = telebot.TeleBot(api_key)

cmds = ["Прислать картинку", "Прислать аудио", "Рассказать о себе"]


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    img_btn = types.KeyboardButton(cmds[0])
    audio_btn = types.KeyboardButton(cmds[1])
    url_btn = types.KeyboardButton(cmds[2])

    markup.add(img_btn)
    markup.add(audio_btn)
    markup.add(url_btn)

    bot.send_message(
        message.from_user.id,
        "Привет, выбери одну из команд ниже или напиши мне 'автор', чтобы узнать больше о боте",
        reply_markup=markup
    )


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if message.text == cmds[0]:
        with open(f'cats/{random.randint(1, 4)}.jpg', 'rb') as img:
            bot.send_message(message.from_user.id, "Вот твоя картинка", reply_markup=markup)
            bot.send_photo(message.from_user.id, img, reply_markup=markup)

    if message.text == cmds[1]:
        with open(f'meow/{random.randint(1, 3)}.mp3', 'rb') as audio:
            bot.send_message(message.from_user.id, "Вот твое мурлыканье", reply_markup=markup)
            bot.send_audio(message.from_user.id, audio, reply_markup=markup)

    if message.text == cmds[2] or message.text.lower() == "автор":
        bot.send_message(
            message.from_user.id,
            "Я - телеграм бот для 1 лабы.\nВот ссылка на мои исходники:\nhttps://github.com/vasshil/Labs_5_sem",
            reply_markup=markup)


bot.polling(none_stop=True, interval=0)
