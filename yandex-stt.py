import json
import logging

from aiogram.utils import executor

import admin
import audio_sqlite_db
import client
import other
from create_bot import dp

#from datetime import datetime

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(
    level=logging.INFO,
    filename="/home/pavel/github/Yandex_stt/log/yandex_stt_bot.log",
    format='%(asctime)s - %(levelname)s - %(message)s'
)
handler = logging.FileHandler('/home/pavel/github/Yandex_stt/log/yandex_stt_bot.log')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

file = open('/home/pavel/cfg/config.json', 'r')
config = json.load(file)
#rtlab_voice_bot_token

#now = datetime.now()

async def on_startup(_):
    logger.warning("Elisseeff Yandex STT Bot logging is ON!")
    audio_sqlite_db.sql_start(logger)

# Start the bot
if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    except (KeyboardInterrupt, SystemExit):
        pass