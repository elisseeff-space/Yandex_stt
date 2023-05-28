import json

from aiogram import Bot
#from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

file = open('/home/pavel/cfg/config.json', 'r')
config = json.load(file)

#storage = MemoryStorage()

class BotLanguage:
    rows_qty_to_select = 5
    rows_offset = 0
    def __init__(self, lang):
        self.lang = lang
    def set(self, lang):
        self.lang = lang
    def get(self) -> str:
        return self.lang
    def add_rows_selected(self, rows_offset: int):
        self.rows_offset += rows_offset
    def clear_rows_selected(self):
        self.rows_offset = 0
    def get_offset(self) -> int:
        return int(self.rows_offset)
    def get_qty_to_select(self) -> int:
        return int(self.rows_qty_to_select)
    
my_lang = BotLanguage('auto')

#bot = Bot(token = config['rtlab_voice_bot_token'])
bot = Bot(token = config['ya_stt_bot'])

#dp = Dispatcher(bot, storage=storage)
dp = Dispatcher(bot)