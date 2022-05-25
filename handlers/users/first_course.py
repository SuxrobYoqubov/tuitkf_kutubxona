from aiogram import types
from aiogram.types import CallbackQuery, Message
import logging
from keyboards.default.mainStart import kurs, mainStart
from keyboards.inline.bookInline import smester,kitob,booksMenu
from keyboards.inline.callback_data import book_callback
from loader import dp


@dp.message_handler(text_contains="Darslik adabiyotlar")
async def books(message: types.Message):
    await message.answer("Sizga qaysi kurs kitoblari kerak?", reply_markup=kurs)


@dp.message_handler(text_contains="1-bosqich")
async def select_category(message: Message):
    await message.answer("Sizga 1-bosqichni qaysi smestri kerak?", reply_markup=smester)

@dp.callback_query_handler(text_contains="first")
async def courses(call: CallbackQuery):
    await call.message.answer("Kitobni tanlang!", reply_markup=booksMenu)
    # Bundan oldingi menyuni o'chiradi
    await call.message.delete()
    await call.answer(cache_time=60)


# Kitob haqida malumot
@dp.callback_query_handler(book_callback.filter(item_name="kitob1"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Kitob mavjud emas, iltimos adminga murojat qiling", cache_time=60, show_alert=True)


@dp.callback_query_handler(book_callback.filter(item_name="kitob2"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Kitob mavjud emas, iltimos adminga murojat qiling", cache_time=60, show_alert=True)

@dp.callback_query_handler(book_callback.filter(item_name="kitob3"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Kitob mavjud emas, iltimos adminga murojat qiling", cache_time=60, show_alert=True)

@dp.callback_query_handler(book_callback.filter(item_name="kitob4"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Kitob mavjud emas, iltimos adminga murojat qiling", cache_time=60, show_alert=True)


# Ortga
@dp.message_handler(text_contains="Ortga")
async def books(message: types.Message):
    await message.answer("Sizga qaysi kurs kitoblari kerak?", reply_markup=mainStart)
