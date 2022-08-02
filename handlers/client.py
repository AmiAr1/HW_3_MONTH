from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from config import bot
from database.bot_dp import sql_command_random
from parser import news


# @dp.message_handler(commands=['pin'], commands_prefix='!/')
async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply("какое сообщение хочешь закрепить? ответь на него")


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply(f"Hi {message.from_user.full_name}")


# @dp.message_handler(commands=["mem"])
async def mem_bot(message: types.Message):
    photo = open("media/maxresdefault.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)


# @dp.message_handler(commands=['quiz'])
async def quiz_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Which direction will you choose? "
    answers = [
        'python', "C++", "C#", "java"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="питон",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def show_random_user(message: types.Message):
    await sql_command_random(message)


async def parser_news(message: types.Message):
    data = news.parser()
    for item in data:
        await bot.send_message(
            message.from_user.id,
            f"{item['title']}\n"
            f"{item['link']}"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(mem_bot, commands=["mem"])
    dp.register_message_handler(quiz_handler, commands=['quiz'])
    dp.register_message_handler(show_random_user, commands=['random'])
    dp.register_message_handler(parser_news, commands=['news'])
