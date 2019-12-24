from bot import telegram_chatbot
from random import randint

bot = telegram_chatbot("config.cfg")

def between(x, min, max):
    return x >= min & x <= max

def make_reply(msg):
    reply = None

    if msg == "!tetas":

        value = randint(1,256)

        if(between(value,1,9)):
            reply = "http://porngif.top/gif/prsa/000" + str(value) + ".gif"
        if(between(value,10,99)):
            reply = "http://porngif.top/gif/prsa/00" + str(value) + ".gif"
        if(between(value,100,255)):
            reply = "http://porngif.top/gif/prsa/0" + str(value) + ".gif"
        value = 0

    if msg == "!culos":

        value = randint(1,155)

        if(between(value,1,9)):
            reply = "http://porngif.top/gif/zadky/000" + str(value) + ".gif"
        if(between(value,10,99)):
            reply = "http://porngif.top/gif/zadky/00" + str(value) + ".gif"
        if(between(value,100,155)):
            reply = "http://porngif.top/gif/zadky/0" + str(value) + ".gif"
        value = 0

    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["chat"]["id"]
            reply = make_reply(message)
            bot.send_gif(reply, from_)