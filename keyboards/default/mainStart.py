
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="π Darslik adabiyotlar"),
            KeyboardButton(text="π Badiiy adabiyotlar"),
        ],
        [
            KeyboardButton(text="βοΈAdmin bilan bog'lanish"),

        ],
    ],
    resize_keyboard=True
)
kurs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-bosqich"),
            KeyboardButton(text="2-bosqich"),
        ],
        [
            KeyboardButton(text="3-bosqich"),
            KeyboardButton(text="4-bosqich"),

        ],
        [
            KeyboardButton(text="π Ortga"),

        ],
    ],
    resize_keyboard=True
)
