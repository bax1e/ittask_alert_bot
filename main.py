import telebot

# Вставь сюда свой токен ОТ BotFather, в кавычках
TOKEN = "8394431801:AAH0_ojaFGruQ9LJQMJIEkXa9v0Gnbhjgfk"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я рабочий бот компании it-task 🚀")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Привет!")

bot.infinity_polling()
