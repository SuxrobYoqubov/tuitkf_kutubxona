# from aiogram import types
# from aiogram.types import CallbackQuery, Message
#
# from keyboards.default.mainStart import kurs
# from keyboards.inline.bookInline import smester
# from loader import dp
#
#
# @dp.message_handler(text_contains="Darslik adabiyotlar")
# async def books(message: types.Message):
#     await message.answer("Sizga qaysi bosqich kitoblari kerak?", reply_markup=kurs)
#
#
# @dp.message_handler(text_contains="1-kurs")
# async def select_category(message: Message):
#     await message.answer("Qaysi smester kitoblari kerak?", reply_markup=smester)