from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message
import json, asyncio


file = open('/home/pavel/cfg/config.json', 'r')
config = json.load(file)

# Replace YOUR_TOKEN with your actual bot token
bot = Bot(token=config['VoskModelSTT_bot'])
dp = Dispatcher(bot)

# Define a handler for the /edit command
@dp.message_handler(commands=['edit'])
async def edit_message(message: types.Message):
    # Send a message to the chat
    sent_message = await bot.send_message(chat_id=message.chat.id, text='Original message')

    # Wait for 5 seconds
    await asyncio.sleep(5)

    # Edit the message with new text
    await bot.edit_message_text(chat_id=message.chat.id, message_id=sent_message.message_id, text='Edited message')

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)