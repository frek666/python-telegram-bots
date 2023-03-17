import telebot

# Creating an instance of the bot
bot = telebot.TeleBot('Here enter the token received from @botfather')

# A function that processes the /start command
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "I'm in touch. Write me something")

# receiving a message from a user
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, "You wrote :" + message.text)

# launching the bot
bot.polling(none_stop=True, interval=0)