from random import randint

import telegram
from telegram import bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

print("Бот запущен. Нажмите Ctrl+C для завершения")


def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет, я Валютный бот")
    print('Hello, i am a valute bot!')


def on_message(update, context):
    chat = update.effective_chat
    text = update.message.text
    try:
        number = float(text)
        rate = 27.20
        hrivens = number * rate
        message = "$%.2f = %.2f UAH" % (number, hrivens)
        context.bot.send_message(chat_id=chat.id, text=message)
        context.bot.send_message(chat_id=chat.id, text="Столько гривасов вы получите за свои баксы. Или не получите...")
    except:
        context.bot.send_message(chat_id=chat.id, text="Ничего не понял...")
        context.bot.send_message(chat_id=chat.id, text="Напишите число для перевода из баксов в гривни")


def on_message_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="This is my Hi to you!!!")




token = "1665828950:AAFIxWCJTvm1UyPNqRMdO-vsfs3HYAMxBUA"

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(CommandHandler("hi", on_message_hi))
dispatcher.add_handler(CommandHandler("game", on_game))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()
