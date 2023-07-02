from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    bot: TgBot


def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config(bot=TgBot(token=env('BOT_TOKEN'), admin_ids=list(map(int, env.list('ADMIN_IDS')))))
