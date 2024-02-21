from config import TOKEN

from bd import addUser, addMessage, getUsers, getData

import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    #await message.answer(f'''
    #                    ID: {message.from_user.id} 
    #                    Username: {message.from_user.username} 
    #                    Date: {message.date} 
    #                    Chat ID: {message.chat.id} 
    #                    Language: {message.from_user.language_code}''')
    await addUser(message.from_user.id, message.from_user.username, message.date, message.chat.id, message.from_user.language_code)
    await addMessage(message.from_user.id, message.text, message.date)



@dp.message(Command('get_data'))
async def cmd_get_data(message: Message):
    txt = await getData(message.from_user.id)
    await message.answer(txt)
    await addMessage(message.from_user.id, message.text, message.date)

@dp.message(Command('get_list_of_users'))
async def cmd_get_list_of_users(message: Message):
    txt = await getUsers()
    await message.reply(txt)
    await addMessage(message.from_user.id, message.text, message.date)


@dp.message()
async def simple_message(message: Message):
    #await message.answer(message.text)
    await addMessage(message.from_user.id, message.text, message.date)
    



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
