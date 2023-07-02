from typing import Any
from aiogram.filters import BaseFilter, Command
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.types import Message, BotCommand

# полученный у @BotFather
API_TOKEN: str = ''

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Создаем асинхронную функцию


async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи')]

    await bot.set_my_commands(main_menu_commands)


@dp.message(Command('change'))
async def handle_edit_menu(message: Message, bot: Bot):
    main_menu_commands = [
        BotCommand(command='/new',
                   description='Справка по работе бота'),
        BotCommand(command='/new2',
                   description='Поддержка'),]

    await bot.set_my_commands(main_menu_commands)

    await message.answer(text='Menu changed')
    
@dp.message(Command('del'))
async def handle_edit_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Menu deleted')


@dp.message()
async def handle_message(message: Message, bot: Bot):
    await message.answer(text='Hello')

if __name__ == '__main__':
    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота,
    dp.startup.register(set_main_menu)
    # Запускаем поллинг
    dp.run_polling(bot)
