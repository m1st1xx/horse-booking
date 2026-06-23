from aiogram import F
from aiogram.types import CallbackQuery

from telegram_bot.bot import dp

@dp.callback_query(
    F.data.startswith(
        "confirm:"
    )
)
async def confirm_booking(
    callback: CallbackQuery
):

    booking_id = int(
        callback.data.split(":")[1]
    )

    print(
        f"Подтверждена заявка {booking_id}"
    )

    await callback.answer(
        "Подтверждено"
    )

@dp.callback_query(
    F.data.startswith(
        "confirm:"
    )
)
async def confirm_booking(
    callback: CallbackQuery
):

    booking_id = int(
        callback.data.split(":")[1]
    )

    print(
        f"Подтверждена заявка {booking_id}"
    )

    await callback.answer(
        "Подтверждено"
    )
