from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db
import os

ADMIN_ID = 123456789

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здравствуйте, напишите команду /help чтобы узнать команды', reply_markup=kb_client)
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/+dyXHMIiEnr9lYmQ6')


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    commands_list = [
        '/start - начать общение с ботом',
        '/help - показать список доступных команд',
        '/Режим_работы - узнать режим работы',
        '/Меню - показать меню',
    ]
    await bot.send_message(message.chat.id, '\n'.join(commands_list))




@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, '24/7')

@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

# @dp.message_handler()
# async def handle_invalid_command(message: types.Message):
#     await bot.send_message(message.chat.id, "Sorry, I didn't understand that command. Please type /help to see the list of available commands.")



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_start, commands=['help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])