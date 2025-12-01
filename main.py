import telebot
import os

# Берём токен из переменной среды Railway
TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    raise ValueError("ERROR: переменная среды TOKEN не найдена! Добавь её в Railway → Variables.")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я рабочий бот компании it-task 🚀")


@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Привет!")


bot.infinity_polling()
