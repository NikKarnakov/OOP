import logging

from aiogram import Dispatcher

from data.config import admins


async def on_startup_notyfy(dp: Dispatcher):
    for admin in admins:
        try:
            text = 'Бот начал работу'
            await dp.bot.send_message(chat_id=admin,text=text)
        except Exception as err:
            logging.exception(err)
