import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("TG_TOKEN")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_(message: Message) -> None:
    await message.answer(f"Ciao {message.from_user.full_name}!")


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot starting...")
    asyncio.run(main())
