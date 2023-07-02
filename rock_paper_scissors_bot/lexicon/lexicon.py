from typing import TypedDict


class PlayButtons(TypedDict):
    rock: str
    paper: str
    scissors: str


class ControlsButtons(TypedDict):
    yes: str
    no: str


class PlayResult(TypedDict):
    user_won: str
    bot_won: str
    drawn: str


class Lexicon(TypedDict):
    cmd_start: str
    cmd_help: str
    play_buttons: PlayButtons
    controls_buttons: ControlsButtons
    play_result: PlayResult
    other_answer: str
    bot_choice: str


LEXICON_RU: Lexicon = {
    'cmd_start': '<b>Привет!</b>\nДавай с тобой сыграем в игру '
    '"Камень, ножницы, бумага"?\n\nЕсли ты, вдруг, '
    'забыл правила, команда /help тебе поможет!\n\n<b>Играем?</b>',

    'cmd_help': 'Это очень простая игра. Мы одновременно должны '
    'сделать выбор одного из трех предметов. Камень, '
    'ножницы или бумага.\n\nЕсли наш выбор '
    'совпадает - ничья, а в остальных случаях камень '
    'побеждает ножницы, ножницы побеждают бумагу, '
    'а бумага побеждает камень.\n\n<b>Играем?</b>',

    'play_buttons': {
        'rock': 'камень',
        'paper': 'бумага',
        'scissors': 'ножницы',
    },
    
    'bot_choice': 'Мой выбор',

    'controls_buttons': {
        'yes': 'Играем!',
        'no': 'Не хочу...'
    },

    'play_result': {
        'bot_won': 'Я победил! Сыграем еще?',
        'drawn': 'Ничья. Сыграем еще?',
        'user_won': 'Ты победил! Сыграем еще?',
    },

    'other_answer': 'Я тебя не понимаю...'    
}
