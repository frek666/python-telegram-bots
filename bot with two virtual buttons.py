import telebot
import random
from telebot import types

# uploading an interesting fact
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

# uploading a list of sayings
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()

# Creating an instance of the bot
bot = telebot.TeleBot('Here enter the token received from @botfather')

# the start command
@bot.message_handler(commands=['start'])
def start(m, res=False):
    # adding two buttons
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("fact")
    item2 = types.KeyboardButton("proverb")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Push: \fact to get an interesting fact\na saying for getting a wise quote ', reply_markup=markup)

# receiving messages from the user
@bot.message_handler(content_types=['text'])
def handle_text(message):
    # if the user pressed 1
    if message.text.strip() == 'fact' :
        answer = random.choice(facts)
    # if the user pressed 2
    elif message.text.strip() == 'proverb' :
        answer = random.choice(thinks)
    # we send the user a message in the chat
    bot.send_message(message.chat.id, answer)

# launching the bot
bot.polling(none_stop=True, interval=0)