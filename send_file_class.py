'''
Шлет файлы в телеграм
'''
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import RegexHandler
import telegram.bot as bot

class send_fl_tg:
    def __init__(self, chat_ids, token_bot):
        self.chat_ids = chat_ids        
        
        self.bot = bot.Bot(token = token_bot)
    
    def send_fl(self, file):
        for chat_id in self.chat_ids:
            self.bot.send_document(chat_id=chat_id,
                                   document=open(file, 'rb'))

if __name__ == '__main__':
    pass
