from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import book_callback



smester = InlineKeyboardMarkup(row_width=1)
first = InlineKeyboardButton(text="1-smester", callback_data=book_callback.new(item_name="first"))
smester.insert(first)

second = InlineKeyboardButton(text="2-smester", callback_data=book_callback.new(item_name="second"))
smester.insert(second)

# smester = {
#     "1-smester": "1-smester",
#     "2-smester": "2-smester",
#
# }
#
# booksMenu = InlineKeyboardMarkup(row_width=1)
# for key, value in smester.items():
#     booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
