from aiogram import types

from loader import dp


@dp.message_handler(text='/help')
async def command_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}! \n'\
        f'/help - вызвать меню помощи\n/start - начать работу бота\n/gen - сгенерировать гороскоп. Свой знак зодиака записать в виде sign:')