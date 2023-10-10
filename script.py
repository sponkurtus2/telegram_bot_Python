import telebot

# BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_TOKEN = '6504422559:AAExHFJfH5iv9_PXrI4HnD3b3n_oljSu2zk'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi teacher, how are you???")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
