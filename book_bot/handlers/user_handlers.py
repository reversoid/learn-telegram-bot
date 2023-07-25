from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON
from database.database import users_db, createUserStructure, getUserById
from services.file_service import book
from keyboards.pagination_kb import create_pagination_keyboard

router: Router = Router()

# Этот хэндлер срабатывает на команду /start


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'])
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = createUserStructure()


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])


@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message):
    user = getUserById(message.from_user.id)
    user['page'] = 1
    text = book[user['page']]
    await message.answer(text=text, reply_markup=create_pagination_keyboard('backward', f'{user["page"]}/{len(book)}', 'forward'))
