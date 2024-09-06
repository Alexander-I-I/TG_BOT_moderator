
from aiogram import Bot, types, F, Router
from aiogram.types import Message


router = Router()

@router.message(F.text)
async def censure(message: Message):
    with open('bad-word.text', 'r') as file:
        censored_letters = [line.strip() for line in file]
    for word in censored_letters:
        if word in message.text.lower():
            await message.delete()
            await message.answer(f"Уважаемый <b>{message.from_user.first_name}</b>\nБез мата, пожалуйста ⛔")