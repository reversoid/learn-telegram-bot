from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove, KeyboardButtonPollType, WebAppInfo)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем кнопку
web_app_btn: KeyboardButton = KeyboardButton(
    text='Start Web App',
    web_app=WebAppInfo(url="https://moofy.ru/"))

# Создаем объект клавиатуры
web_app_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[web_app_btn]],
    resize_keyboard=True)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '5681787061:AAF7n_XVkofeyf1QrMGXeSXAlx6-1rYycV0'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=web_app_keyboard)

if __name__ == '__main__':
    dp.run_polling(bot)
