from enum import Enum
from typing import TypedDict


class Lexicon(TypedDict):
    cmd_start: str
    cmd_help: str


LEXICON_RU: Lexicon = {
    'cmd_start': 'Привет!\n Я — эхо бот, сделанный для демонстрации хендлеров',
    'cmd_help': 'Данный бот может ответить вам то, что вы написали',
    'no_echo': 'Не могу ответить('
}
