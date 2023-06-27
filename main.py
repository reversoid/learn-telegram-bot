import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message, ContentType
from aiogram import F
from typing import TypedDict


class State(TypedDict):
    in_game: bool
    attempts: int | None
    wins: int
    secret_number: int | None


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = ''

MAX_ATTEMPTS = 10

game_state: State = {
    'in_game': False,
    'attempts': None,
    'wins': 0,
    'secret_number': None
}


def get_random_number():
    return random.randint(1, 100)


# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start']))
async def handle_start_bot(message: Message):
    await message.answer('Привет!\nТут мы играем в игру "Угадай число"\n Чтобы играть, напиши "Да". Чтобы отменить, пиши команду "/cancel"')

@dp.message(Command(commands=['help']))
async def handle_help(message: Message):
    await message.answer('Чтобы начать игру, введите "/start". Чтобы закончить игру, введите "/cancel"')


@dp.message(Command(commands=['cancel']))
async def handle_cancel(message: Message):
    game_state['attempts'] = None
    game_state['in_game'] = False
    game_state['secret_number'] = None
    await message.answer('Игра отменена')


@dp.message(Command(commands=['stat']))
async def handle_stat(message: Message):
    game_state['attempts'] = None
    game_state['in_game'] = False
    game_state['secret_number'] = None
    if (game_state['in_game']):
        return await message.answer(f'У вас {game_state["attempts"]} попыток и {game_state["wins"]} побед')
    return message.answer(f'У вас {game_state["wins"]} побед')

@dp.message(Text(text=['Да', 'Давай', 'Сыграем', 'Игра',
                       'Играть', 'Хочу играть'], ignore_case=True))
async def handle_start_game(message: Message):
    game_state['attempts'] = 0
    game_state['in_game'] = True
    game_state['secret_number'] = get_random_number()
    await message.answer('Играем! Угадай число')


@dp.message()
async def handle_play_game(message: Message):
    if not game_state['in_game']:
        return await message.answer('Чтобы начать игру, введите "/start". Чтобы закончить игру, введите "/cancel"')
    
    try:
        parsedInt = int(message.text)
        game_state['attempts'] = game_state['attempts'] + 1 
        if (game_state['attempts'] > MAX_ATTEMPTS):
            await message.answer('Вы проиграли, правильное число было ', game_state['secret_number'])
            game_state['attempts'] = None
            game_state['in_game'] = False
            game_state['secret_number'] = None
        
        elif parsedInt == game_state['secret_number']:
            await message.answer('Вы выиграли! Еще одна победа за вами.')
            game_state['attempts'] = None
            game_state['in_game'] = False
            game_state['secret_number'] = None
            game_state['wins'] = game_state['wins'] + 1
            
        elif game_state['secret_number'] > parsedInt:
            await message.answer('Загаданное число больше))')
            
        elif game_state['secret_number'] < parsedInt:
            await message.answer('Загаданное число меньше((')

    except:
        await message.answer('Я вас не понял. Введите просто число')    

if __name__ == '__main__':
    dp.run_polling(bot)
