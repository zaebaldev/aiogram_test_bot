from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.methods.send_chat_action import SendChatAction
from aiogram.enums.chat_action import ChatAction

router = Router()


@router.message(F.photo)
async def photo_handler(message: types.Message):
    await message.answer("I cant view photo!")


@router.message(Command("image"))
async def image_cmd(message: types.Message):
    # img_url = (
    #     "https://cs14.pikabu.ru/post_img/2023/10/10/6/og_og_1696928113214795976.jpg"
    # )
    image = FSInputFile("/home/alien/Pictures/icon - edid this.png")
    await message.answer_photo(
        photo=image,
        caption="my photo",
    )


@router.message(Command("doc"))
async def document_cmd(message: types.Message):
    doc = FSInputFile(
        "/home/alien/Documents/4de4b51c-b503-460b-9b01-41bbeb2114ba_Python_Basic_Course.pdf"
    )
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.CHOOSE_STICKER,
    )
    await message.answer_document(
        document=doc,
        caption="my document",
    )
