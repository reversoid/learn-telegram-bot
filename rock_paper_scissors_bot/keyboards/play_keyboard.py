from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

button_rock: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['play_buttons']['rock'])
button_paper: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['play_buttons']['paper'])
button_scissors: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['play_buttons']['scissors'])


play_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
play_kb_builder.add(button_rock, button_paper, button_scissors)
play_kb_builder.adjust(1)

play_kb: ReplyKeyboardMarkup = play_kb_builder.as_markup(resize_keyboard=True)
