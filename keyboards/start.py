# from aiogram.types.reply_keyboard_markup import ReplyKeyboard
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_start_kb():
    # button1 = KeyboardButton(text="1")
    # button2 = KeyboardButton(text="2")
    # kb = ReplyKeyboardMarkup(
    #     keyboard=[
    #         [button1, button1],
    #         [button2],
    #     ]
    # )
    # return kb
    builder = ReplyKeyboardBuilder()
    for index in range(1, 11):
        builder.add(KeyboardButton(text=f"{index}"))
        # builder.button(text=f"Set {index}")
    builder.adjust(3)
    return builder.as_markup()
