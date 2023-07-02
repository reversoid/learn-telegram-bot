from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, Text
from lexicon.lexicon import LEXICON_RU
from keyboards import yes_no_kb, play_kb
from services.services import get_bot_choice, get_winner, Winner

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['cmd_start'], reply_markup=yes_no_kb)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['cmd_help'], reply_markup=yes_no_kb)


@router.message(Text(LEXICON_RU['controls_buttons']['yes']))
async def process_agree_button(message: Message):
    await message.answer(text=LEXICON_RU['controls_buttons']['yes'], reply_markup=play_kb)


@router.message(Text(LEXICON_RU['controls_buttons']['no']))
async def process_disagree_button(message: Message):
    await message.answer(text=LEXICON_RU['controls_buttons']['no'])


@router.message(Text(text=[LEXICON_RU['play_buttons']['rock'],
                           LEXICON_RU['play_buttons']['paper'],
                           LEXICON_RU['play_buttons']['scissors']]))
async def process_play_buttons(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU["play_buttons"][bot_choice]}')
    winner: Winner = get_winner(message.text, bot_choice)
    if (winner == Winner.BOT):
        await message.answer(text=LEXICON_RU['play_result']['bot_won'], reply_markup=yes_no_kb)
    elif (winner == Winner.USER):
        await message.answer(text=LEXICON_RU['play_result']['user_won'], reply_markup=yes_no_kb)
    elif winner == Winner.DRAW:
        await message.answer(text=LEXICON_RU['play_result']['drawn'], reply_markup=yes_no_kb)
