from lexicon.lexicon import LEXICON_RU
from random import choice
from enum import Enum
from typing import Literal

Choice = Literal['rock', 'scissors', 'paper']


def get_bot_choice() -> Choice:
    options: list[Choice] = 'rock', 'scissors', 'paper'
    return choice(options)


class Winner(Enum):
    USER = 1,
    BOT = 2,
    DRAW = 3


def _normalize_user_answer(answer: str) -> Choice:
    if answer == LEXICON_RU['play_buttons']['paper']:
        return 'paper'
    
    if answer == LEXICON_RU['play_buttons']['rock']:
        return 'rock'
    
    if answer == LEXICON_RU['play_buttons']['scissors']:
        return 'scissors'

    raise 'WRONG_USER_ANSWER'


def get_winner(user_answer: str, bot_choice: Choice) -> Winner:
    user_choice: Choice = _normalize_user_answer(user_answer)
    
    if (user_choice == bot_choice):
        return Winner.DRAW

    if user_choice == 'paper':
        if (bot_choice == 'rock'):
            return Winner.USER
        if (bot_choice == 'scissors'):
            return Winner.BOT

    if user_choice == 'scissors':
        if (bot_choice == 'rock'):
            return Winner.BOT
        if (bot_choice == 'paper'):
            return Winner.USER

    if user_choice == 'rock':
        if (bot_choice == 'scissors'):
            return Winner.USER
        if (bot_choice == 'paper'):
            return Winner.BOT

    raise 'WRONG_USER_CHOICE'