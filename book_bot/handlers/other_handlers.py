from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

router: Router = Router()

@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(message.chat.id)
    except TypeError:
        await message.reply(LEXICON_RU['no_echo'])