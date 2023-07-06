from aiogram import Router, html
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.models import User

router = Router(name="commands-router")


@router.message(CommandStart())
async def cmd_start(message: Message, session: AsyncSession):
    query = select(User.name).where(User.user_id == 1)
    res = await session.execute(query)
    res = res.scalar()
    await message.answer(f"This is res = {res}")
