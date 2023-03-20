import telebot
import os
from fuzzywuzzy import fuzz

# Creating an instance of the bot
bot = telebot.TeleBot('Here enter the token received from @botfather')

# loading a list of phrases and answers into an array
mas = []
if os.path.exists('data/chatbot.txt'):
    f=open('data/chatbot.txt', 'r', encoding='UTF-8')
    for x in f:
        if(len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()

# using fuzzywuzzy, we calculate the most similar phrase and give the following list item as an answer
def answer(text):
    try:
        text=text.lower().strip()
        if os.path.exists('data/chatbot.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    # using fuzzywuzzy, we get how similar the two strings are
                    aa = (fuzz.token_set_ratio(q.replace('u: ',''), text))
                    if(aa > a and aa!= a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'

# command <<start>>
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "I'm in touch. write hello :3")

# we receive a message from the user
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # recording logs
    f = open('data/' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    s = answer(message.text)
    f.write('u: ' + message.txt + '\n' + s + '\n')
    f.close()
    # sending a response
    bot.send_message(message.chat.id, s)

# launching the bot
bot.polling(none_stop=True, interval=0)