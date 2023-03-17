import telebot, wikipedia, re

# Creating an instance of the bot
bot = telebot.TeleBot('Here enter the token received from @botfather')

# Setting the English language
wikipedia.set_lang("eng")

# we clean the text of the article in wikipedia and limit it to a thousand characters
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # we get the first thousand characters
        wikitext=ny.content[:1000]
        # we divide by points
        wikimas=wikitext.split('.')
        # discarding everything after the last point
        wikimas = wikimas[:-1]
        # creating an empty variable for the text
        wikitext2 = ''
        # we go through the lines where there are no <<equals>> signs (that is, everything except the headers)
        for x in wikimas:
            if not('==' in x):
                # if there are more than three characters left in the string, add it to our variable and return the points lost when dividing the strings into place
            if(len((x.strip()))>3):
                wikitext2=wikitext2+x+'.'
            else:
                break
            # now, using regular expressions, we remove the markup
            wikitext2=re.sub('\([^()]*\)', '', wikitext2)
            wikitext2=re.sub('\([^()]*\)', '', wikitext2)
            wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
            # returning a text string
            return wikitext2
        # handling exceptions that the wikipedia module could return when querying
    except Exception as e:
        return 'There is no information about this in the encyclopedia'

# a function that processes the /start command
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Send me any word and I will find its meaning on Wikipedia')

# receiving messages from the user
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

# launching the bot
bot.polling(none_stop=True, interval=0)