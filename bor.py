import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

TOKEN = "7637645429:AAE8sNWZcdhTzlRftFbs1DsL40vC_PdPzQo"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo_message(message: Message):
    await message.answer(f"Ви написали: {message.text}")

async def main():
    print("Бот запущено!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


    @dp.message(commands=['start'])
    async def start_command(message: Message):
        await message.answer("Привіт! Я твій бот.")
