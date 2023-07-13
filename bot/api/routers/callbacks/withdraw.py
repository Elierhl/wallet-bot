from typing import Union

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.common import constants, states
from bot.common.callbacks import NavigationCallback
from bot.markups import menu, withdraw
from bot.services.withdraw import withdraw_controller

router = Router(name="withdraw-callback-router")


@router.callback_query(NavigationCallback.filter(F.where == 'withdraw'))
async def withdraw_choose_currency_handler(query: CallbackQuery):
    await query.message.edit_text(
        constants.WITHDRAW['currency'],
        reply_markup=withdraw.withdraw_currency_markup(),
    )


@router.callback_query(NavigationCallback.filter(F.where == 'withdraw_BTC'))
async def withdraw_provide_address_handler(
    query: CallbackQuery, callback_data: NavigationCallback, state: FSMContext
):
    await withdraw_controller.provide_address(callback_data, state)
    await query.message.edit_text(
        constants.WITHDRAW['address'],
        reply_markup=withdraw.withdraw_step_back_markup('withdraw'),
    )


@router.callback_query(NavigationCallback.filter(F.where == 'withdraw_amount'))
@router.message(states.Withdraw.address)
async def withdraw_provide_amount_handler(
    message: Union[Message, CallbackQuery], state: FSMContext
):
    reply_markup_type = await withdraw_controller.provide_amount(message, state)
    if isinstance(message, CallbackQuery):
        message = message.message

    if reply_markup_type:
        await message.answer(
            constants.WITHDRAW['amount'],
            reply_markup=withdraw.withdraw_step_back_markup(reply_markup_type),
        )


@router.message(states.Withdraw.amount)
async def withdraw_confirmation_handler(message: Message, state: FSMContext):
    user_data = await withdraw_controller.get_confirmation(message, state)

    if user_data:
        await message.answer(
            constants.WITHDRAW['confirmation'].format(
                amount=user_data['amount'],
                currency=user_data['currency'],
                address=user_data['address'],
            ),
            reply_markup=withdraw.withdraw_confirmation_markup(),
        )
    else:
        await message.answer(
            constants.WITHDRAW['wrong_amount'],
            reply_markup=withdraw.withdraw_step_back_markup('withdraw_BTC'),
        )


@router.callback_query(NavigationCallback.filter(F.where == 'withdraw_proceed'))
async def withdraw_proceeding_handler(query: CallbackQuery, state: FSMContext):
    text = await withdraw_controller.proceed_withdrawal(state)
    await query.message.answer(text, reply_markup=menu.start_markup())
    await state.clear()
