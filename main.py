import sqlite3
from vkbottle.bot import Bot, Message
import asyncio
from functions import isInDB, load_data, find_id
from datetime import datetime

token = '93ffbc4048b9d780354f6003146b650a6a988944b0deabda03ed8b7585105f11a1f28b91cd5fb33b552b2'
bot = Bot(token=token)


@bot.on.message(text="/setdostup <user_id> <dostup> <rank>")
async def set_dostup(message: Message, user_id=None, dostup=None, rank=None):
    users_info = await bot.api.users.get(message.from_id)
    id = users_info[0].id
    current_datetime = datetime.now()
    uid = user_id.split("|")
    uid = uid[0].split("[")
    uid = uid[1].split("id")
    uid = int(uid[1])
    if isInDB(uid) == False:
        if isInDB(id) == True:
            if find_id(id) >= 1:
                load_data(user_id=uid, dostup=dostup, date_of_dostup=current_datetime, rank=rank)
                await message.answer(f"Пользователю [id{uid}|{users_info[0].first_name + ' ' + users_info[0].last_name}] был выдан доступ {dostup}")
            else:
                await message.answer("У вас недостаточно прав!")
    else:
        if isInDB(id) == True:
            if find_id(id) >= 1:
                await message.answer(f"Пользователь [id{uid}|{users_info[0].first_name + ' ' + users_info[0].last_name}] уже зарегистрирован")
            else:
                await message.answer("У вас недостаточно прав!")

bot.run_forever()