from aiogram import Router, types, F


router = Router()


@router.message(F.photo)
async def photo_handler(message: types.Message):
    await message.answer("I cant view photo!")
