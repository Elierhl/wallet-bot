import logging
import re
from typing import Union

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot import markups
from bot.classes import states
from bot.classes.common import NavigationCallback
from bot.consts.phrases import DEPOSIT, MAIN_MENU, NETWORKS, WITHDRAW
from bot.db.models import *
from bot.http_requests import coingecko_api, cryptocurrency_api

router = Router(name="callbacks-router")
logger = logging.getLogger(__name__)


@router.callback_query(NavigationCallback.filter(F.where == 'menu'))
async def menu_handler(query: CallbackQuery):
    await query.message.edit_text(
        MAIN_MENU['menu'], reply_markup=markups.main_menu_markup()
    )


@router.callback_query(NavigationCallback.filter(F.where.in_(['support', 'settings'])))
async def menu_generator_handler(
    query: CallbackQuery, callback_data: NavigationCallback
):
    await query.message.edit_text(
        MAIN_MENU[callback_data.where],
        reply_markup=markups.undeveloped_menu_markup(),
    )


@router.callback_query(NavigationCallback.filter(F.where == 'my_wallet'))
async def my_wallet_handler(query: CallbackQuery, session: AsyncSession):
    stmt = select(UserBalance.btc, UserBalance.usdt).where(
        User.tg_id == query.from_user.id
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

    await query.message.edit_text(
        MAIN_MENU['my_wallet'].format(
            btc=btc,
            usdt=usdt,
            btc_rub_equivalent=btc_rub_equivalent,
            usdt_rub_equivalent=usdt_rub_equivalent,
        ),
        reply_markup=markups.my_wallet_markup(),
    )


@router.callback_query(NavigationCallback.filter(F.where == 'deposit'))
async def deposit_choose_currency_handler(query: CallbackQuery):
    await query.message.edit_text(
        DEPOSIT['currency'],
        reply_markup=markups.deposit_currency_markup(),
    )


@router.callback_query(NavigationCallback.filter(F.where == 'deposit_BTC'))
async def deposit_proceeding_handler(
    query: CallbackQuery, callback_data: NavigationCallback
):
    currency = callback_data.where.split('_')[1]
    address = await cryptocurrency_api.give_address(
        tg_id=query.from_user.id,
        currency=currency,
    )
    await query.message.edit_text(
        DEPOSIT['address'].format(
            currency=currency,
            network=NETWORKS[currency],
            address=address,
        ),
        reply_markup=markups.back_to_main_menu_markup(),
    )


@router.callback_query(NavigationCallback.filter(F.where == 'withdraw'))
async def withdraw_choose_currency_handler(query: CallbackQuery):
    await query.message.edit_text(
        WITHDRAW['currency'],
        reply_markup=markups.withdraw_currency_markup(),
    )


@router.callback_query(NavigationCallback.filter(F.where == 'withdraw_BTC'))
async def withdraw_provide_address_handler(
    query: CallbackQuery, callback_data: NavigationCallback, state: FSMContext
):
    await state.update_data(currency=callback_data.where.split('_')[1])
    await state.set_state(states.Withdraw.address)
    await query.message.edit_text(
        WITHDRAW['address'],
        reply_markup=markups.withdraw_step_back_markup('withdraw'),
    )


@router.callback_query(NavigationCallback.filter(F.where == 'withdraw_amount'))
@router.message(states.Withdraw.address)
async def withdraw_provide_amount_handler(
    message: Union[Message, CallbackQuery], state: FSMContext
):
    if isinstance(message, Message):
        if re.fullmatch(r'\w{34}', message.text) and isinstance(message, Message):
            await state.update_data(address=message.text)
            await state.set_state(states.Withdraw.amount)
            await message.answer(
                WITHDRAW['amount'],
                reply_markup=markups.withdraw_step_back_markup('withdraw_BTC'),
            )
        else:
            await message.answer(
                WITHDRAW['wrong_address'],
                reply_markup=markups.withdraw_step_back_markup('withdraw'),
            )

    elif isinstance(message, CallbackQuery):
        await message.message.answer(
            WITHDRAW['amount'],
            reply_markup=markups.withdraw_step_back_markup('withdraw_BTC'),
        )


@router.message(states.Withdraw.amount)
async def withdraw_confirmation_handler(message: Message, state: FSMContext):
    if re.fullmatch(r'\d*\.?\d+', message.text):
        await state.update_data(amount=message.text)
        user_data = await state.get_data()
        await message.answer(
            WITHDRAW['confirmation'].format(
                amount=user_data['amount'],
                currency=user_data['currency'],
                address=user_data['address'],
            ),
            reply_markup=markups.withdraw_confirmation_markup(),
        )
    else:
        await message.answer(
            WITHDRAW['wrong_amount'],
            reply_markup=markups.withdraw_step_back_markup('withdraw_BTC'),
        )


@router.callback_query(NavigationCallback.filter(F.where == 'withdraw_proceed'))
async def withdraw_proceeding_handler(query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    response = await cryptocurrency_api.send_crypto(
        amount=user_data['amount'],
        currency=user_data['currency'],
        address=user_data['address'],
    )
    if response:
        text = WITHDRAW['success']
    else:
        text = WITHDRAW['failed']

    await query.message.answer(text, reply_markup=markups.start_markup())
    await state.clear()


# @router.callback_query(NavigationCallback.filter(F.where == 'SQL'))
# async def cc_api_handler(query: CallbackQuery, session: AsyncSession):
#     stmt = select(User.username).where(User.id == 1)
#     res = await session.execute(stmt)
#     res = res.scalar()
#     await query.message.edit_text(
#         f'This is your name: {res} and tg_id: {query.from_user.id}',
#         reply_markup=markups.start_markup()
#     )
