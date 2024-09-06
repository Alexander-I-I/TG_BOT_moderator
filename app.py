import asyncio
import logging
import re
import os


from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command, CommandObject
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums.parse_mode import ParseMode
from aiogram.enums.chat_member_status import ChatMemberStatus
from dotenv import load_dotenv
from HANDLERS import check_message
from HANDLERS import ban_unban_mute_unmute

load_dotenv()
#токен
TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

router = Router()
router.message.filter(F.chat.type != "private")


@dp.message(F.chat.type == "private")
async def private(message: types.Message):
    await message.reply("😔 <b>Бот работает только в группах</b>")




async def main():
    dp.include_router(ban_unban_mute_unmute.router)
    dp.include_router(check_message.router)
    dp.include_router(router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())