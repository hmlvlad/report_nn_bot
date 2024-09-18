import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN
from doc_in_img import reform_doc

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message()
async def cmd1_start(message):
    #111
    if message.document:
        print(message.document.file_id)
        file_info = await bot.get_file(message.document.file_id)
        downloaded_file = await bot.download_file(file_info.file_path)
        print(file_info.file_path[10:])
        src = file_info.file_path
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file.getvalue())
        await message.reply('Документ успешно сохранен!')
        reform_doc(file_info.file_path[10:])
        # await message.reply_document()
    else:
        await message.reply('Я не понял, что ты хочешь')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
