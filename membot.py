import telebot
import time

# Creating an instance of the bot
bot = telebot.TeleBot('Here enter the token received from @botfather')
# the channel address starts with @
CHANNEL_NAME = '@the_address_of_your_channel'

# uploading memes
f = open('data/fun.txt', 'r', encoding='UTF-8')
mem = f.read().split('\n')
f.close()

# until the memes run out, we send them to the chat
for mem in mems:
    bot.send_message(CHANNEL_NAME, joke)
    # pause at 1 hour
    time.sleep(3600)

bot.send_message(CHANNEL_NAME, "MEM IS OVER :-(")
