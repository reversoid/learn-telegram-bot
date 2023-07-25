from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from services.file_service import book
from lexicon.lexicon import LEXICON


def create_bookmarks_keyboard(*pages: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    for page in sorted(pages):
        kb_builder.row(InlineKeyboardButton(
            text=f'{page} - {book[page][:100]}', callback_data=str(page)))

    kb_builder.row(InlineKeyboardButton(
        text=LEXICON['edit_bookmarks_button'], callback_data='edit_bookmarks'), InlineKeyboardButton(
        text=LEXICON['cancel'], callback_data='cancel'), width=2)

    return kb_builder.as_markup()


def create_edit_keyboard(*pages: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    for page in sorted(pages):
        kb_builder.row(InlineKeyboardButton(
            text=f'{LEXICON["del"]} {page} - {book[page][:100]}', callback_data=f'{page} del'))

    kb_builder.row(InlineKeyboardButton(
        text=LEXICON['cancel'], callback_data='cancel'))

    return kb_builder.as_markup()
