import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from bot import markups
from bot.consts.phrases import MAIN_MENU
from bot.db.models import *
from bot.http_requests import coingecko_api, cryptocurrency_api

router = Router(name="commands-router")
logger = logging.getLogger(__name__)


@router.message(Command('start'))
async def start_cmd(message: Message, state: FSMContext, session: AsyncSession):
    params = {
        'tg_id': message.from_user.id,
        'username': message.from_user.username,
    }
    await session.execute(insert(User), params)
    await session.commit()

    stmt = select(User.id).where(User.tg_id == message.from_user.id)
    user_id = (await session.execute(stmt)).scalar()

    params = {
        'user_id': user_id,
        'btc': 0.0015,  # tmp
        'usdt': 840,  # tmp
    }
    await session.execute(insert(UserBalance), params)
    await session.commit()

    await message.answer(MAIN_MENU['start'], reply_markup=markups.start_markup())
    await state.clear()


@router.message(Command('menu'))
async def menu_cmd(message: Message, state: FSMContext):
    await message.answer(MAIN_MENU['menu'], reply_markup=markups.main_menu_markup())
    await state.clear()


@router.message(Command('my_wallet'))
async def my_wallet_cmd(message: Message, session: AsyncSession):
    stmt = select(UserBalance.btc, UserBalance.usdt).where(
        User.tg_id == message.from_user.id
    )
    balances = await session.execute(stmt)
    btc, usdt = balances.all()[0]

    if btc:
        btc_price = (await coingecko_api.get_price('bitcoin', 'rub'))['bitcoin']['rub']
        btc_rub_equivalent = MAIN_MENU['rub_equivalent'].format(
            rub=round(btc_price * btc)
        )
    else:
        btc_rub_equivalent = ''

    if usdt:
        usdt_price = (await coingecko_api.get_price('tether', 'rub'))['tether']['rub']
        usdt_rub_equivalent = MAIN_MENU['rub_equivalent'].format(
            rub=round(usdt_price * usdt)
        )
    else:
        usdt_rub_equivalent = ''

    await message.answer(
        MAIN_MENU['my_wallet'].format(
            btc=btc,
            usdt=usdt,
            btc_rub_equivalent=btc_rub_equivalent,
            usdt_rub_equivalent=usdt_rub_equivalent,
        ),
        reply_markup=markups.my_wallet_markup(),
    )
