from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

button_yes: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['controls_buttons']['yes'])
button_no: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['controls_buttons']['no'])

yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True, resize_keyboard=True)
