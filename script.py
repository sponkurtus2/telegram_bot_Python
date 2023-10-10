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

#   Steps to deploy it to Heroku
#   1 - Create a file Procfile with the following content - bot: python name_of_your_py_file
#   2 - Get all the important dependencies of your project with pip freeze > requirements.txt
#   3 - Log in heroku with heroku loin
#   4 - Initialize a reposiory with git init
#   5 - Add all the files to the repository git add .
#   6 - Push the code to heroku with git push heroku master
#   7 - And turn on the bot with heroku ps:scale bot = 1
