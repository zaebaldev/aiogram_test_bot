from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

router = Router()


class Form(StatesGroup):
    name = State()
    surname = State()
    age = State()


@router.message(Command("survey"))
async def start_cmd(
    message: Message,
    state: FSMContext,
):
    await state.set_state(Form.name)
    await message.answer(
        text="Hi! Whats ur name?",
    )


@router.message(Form.name)
async def process_name(
    message: Message,
    state: FSMContext,
) -> None:
    await message.answer(
        text=f"Your name is {message.text}",
    )
    await state.update_data({"name": message.text})
    await state.set_state(Form.surname)


@router.message(Form.surname)
async def process_surname(
    message: Message,
    state: FSMContext,
) -> None:
    await state.update_data({"surname": message.text})
    await state.set_state(Form.age)
    await message.answer(
        text=f"Your surname is {message.text}",
    )


@router.message(Form.age)
async def process_age(
    message: Message,
    state: FSMContext,
) -> None:
    await state.update_data({"age": message.text})
    name = await state.get_value("name")
    surname = await state.get_value("surname")
    await message.answer(
        text=f"Your name is {name}\n Your surname is {surname}\nYour age is {message.text}",
    )
    await state.clear()
