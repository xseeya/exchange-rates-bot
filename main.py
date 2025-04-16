from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import CommandStart

from keyboard import *

from db import Session, Exchange

from aiogram.enums import ParseMode


main_router = Router()

@main_router.message(CommandStart())
async def cmd_cancel(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')
    
@main_router.message(F.text == 'Для Максима')
async def cmd_for_maxim(message: Message):
    if message.from_user.id == 1352162193:
        await message.answer(f'Что лучше, thun thun thun sahur или Tralalero tralala?', reply_markup=kb_main)
    else:
        await message.answer(f'Вы не Максим', reply_markup=kb_main)
        
@main_router.message(F.text == 'Курс валют')
async def cmd_rates(message: Message):
    with Session() as db:
        rates = db.query(Exchange).first()
    await message.answer(f'<b>Курс валют:</b>\n'
                         f'<blockquote><code>{rates.usd_to_rub}</code>'
                         f'\n<code>{rates.eur_to_rub}</code>'
                         f'\n<code>{rates.cny_to_rub}</code></blockquote>\n\n'
                         f'<blockquote>Последнее обновление в {rates.time}</blockquote>', parse_mode=ParseMode.HTML,
                         reply_markup=kb_main)
    
@main_router.message(F.text == 'Профиль')
async def cmd_rates(message: Message):
    await message.answer(f'<blockquote> 👤 Юзернейм: {message.from_user.username}\n'
f'🆔 Твой ID: {message.from_user.id}\n'
f'📛 Твоё имя: {message.from_user.full_name}\n'
f'🌐 Язык Telegram: {message.from_user.language_code}</blockquote>\n\n'
'👨‍💻 Разработчик: @xseeyya', parse_mode=ParseMode.HTML, reply_markup=kb_main)
    