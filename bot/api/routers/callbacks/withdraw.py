from typing import Union

from aiogram.fsm.context import FSMContext

from bot.common.callbacks import NavigationCallback
from aiogram.types import CallbackQuery, Message
from aiogram import F, Router

from bot.common import constants, states
from bot.services.markups import withdraw, menu
from bot.services.withdraw import withdraw_service

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
    await withdraw_service.provide_address(callback_data, state)
    await query.message.edit_text(
        constants.WITHDRAW['address'],
        reply_markup=withdraw.withdraw_step_back_markup('withdraw'),
    )


@router.callback_query(NavigationCallback.filter(F.where == 'withdraw_amount'))
@router.message(states.Withdraw.address)
async def withdraw_provide_amount_handler(
    message: Union[Message, CallbackQuery], state: FSMContext
):
    reply_markup_type = await withdraw_service.provide_amount(message, state)

    if reply_markup_type:
        await message.message.answer(
            constants.WITHDRAW['amount'],
            reply_markup=withdraw.withdraw_step_back_markup(reply_markup_type),
        )


@router.message(states.Withdraw.amount)
async def withdraw_confirmation_handler(message: Message, state: FSMContext):
    user_data = await withdraw_service.get_confirmation(message, state)

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
    text = await withdraw_service.proceed_withdrawal(state)
    await query.message.answer(text, reply_markup=menu.start_markup())
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
