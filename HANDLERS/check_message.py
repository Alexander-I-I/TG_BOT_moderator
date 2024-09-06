
from aiogram import Bot, types, F, Router
from aiogram.types import Message
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest


router = Router()
# counter = 0
@router.message(F.text)
async def censure(message: Message, bot: Bot):
    # reply_message = message.from_user.first_name
    # global counter
    #
    # if counter >= 2:
    #     with suppress(TelegramBadRequest):
    #         await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id,
    #                                        permissions=types.ChatPermissions(can_send_messages=False))
    #         await message.delete()
    #         await message.answer(f"Предупреждений больше не будет!!!\n🔇 Пользователь <b>{reply_message}</b> был заглушен!")

    with open('bad-word.text', 'r') as file:
        censored_letters = [line.strip() for line in file]
    for word in censored_letters:
        if word in message.text.lower():
            # counter += 1
            await message.delete()
            await message.answer(f"Юзер - <b>{message.from_user.first_name}</b>\nБез мата, пожалуйста ⛔")


