import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot



async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="ok")


async def go_to():
    await bot.send_message(chat_id=chat_id, text='помой машину')


async def scheduler():
    aioschedule.every().friday.at("03:28").do(go_to)
    aioschedule.every().monday.at("03:28").do(go_to)


    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(5)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)
