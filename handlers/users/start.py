from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainStart import mainStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"👨‍🎓 Assalomu alaykum, {message.from_user.full_name} !\n"
                         f"📖 TATU Qarshi filiali Axborot Resurs Markaziga xush kelibsiz.\n"
                         f"🔍 Bu yerda siz fanga oid bo'lgan barcha kitoblarni va badiiy asarlarni topishingiz mumkin.", reply_markup=mainStart)


