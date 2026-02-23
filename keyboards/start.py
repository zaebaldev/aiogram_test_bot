from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton


def get_start_kb():
    button1 = KeyboardButton(text="1")
    button2 = KeyboardButton(text="2")
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [button1, button1],
            [button2],
        ]
    )
    return kb
