# @author Aril Psxat

from module import Telegram

bot = Telegram('BOT_TOKEN', 'TIME_ZONE')

while True:
    if bot.centMessage:
        if bot.cektMessage(mtext=['/start']):
            bot.postReq('sendMessage', text=['ManggisMs'], chat_id=[bot.ai])
