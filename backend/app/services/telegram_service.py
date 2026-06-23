from aiogram import Bot
import asyncio
from backend.app.config import settings


bot = Bot(
    token=settings.BOT_TOKEN
)


async def send_booking_notification(booking):

    text = f"""
Новая заявка

Имя: {booking.client_name}

Телефон: {booking.phone}

Пол: {booking.gender}

Количество человек: {booking.people_count}

Начало: {booking.booking_time}

Конец: {booking.end_time}

Длительность: {booking.duration} ч.
"""

    await bot.send_message(
        chat_id=settings.MANAGER_CHAT_ID,
        text=text
    )
