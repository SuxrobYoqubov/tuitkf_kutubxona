from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import book_callback



smester = InlineKeyboardMarkup(row_width=1)
first = InlineKeyboardButton(text="1-smester", callback_data=book_callback.new(item_name="first"))
smester.insert(first)

second = InlineKeyboardButton(text="2-smester", callback_data=book_callback.new(item_name="second"))
smester.insert(second)



kitob = {
    "🟢 kitob1": "kitob1",
    "🟢 kitob2": "kitob2",
    "🟢kitob3": "kitob3",
    "🟢kitob4": "kitob4",

}
booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in kitob.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
