import telebot
import time

# Creating an instance of the bot
bot = telebot.TeleBot('Here enter the token received from @botfather')
# b
CHANNEL_NAME = '@the_address_of_your_channel'

# c
f = open('data/fun.txt', 'r', encoding='UTF-8')
mem = f.read().split('\n')
f.close()

# d
for mem in mems:
    bot.send_message(CHANNEL_NAME, joke)
    # e
    time.sleep(3600)

bot.send_message(CHANNEL_NAME, "MEM IS OVER :-(")
