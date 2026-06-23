from aiogram import Bot
from aiogram import Dispatcher

from backend.app.config import settings

bot = Bot(
    token=settings.BOT_TOKEN
)

dp = Dispatcher()