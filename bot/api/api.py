from aiogram import Router

from bot.api.routers.callbacks.deposit import router as deposit_callback_router
from bot.api.routers.callbacks.menu import router as menu_callback_router
from bot.api.routers.callbacks.withdraw import router as withdraw_callback_router
from bot.api.routers.commands import router as commands_router

router = Router(name="api-router")

router.include_router(commands_router)
router.include_router(menu_callback_router)
router.include_router(deposit_callback_router)
router.include_router(withdraw_callback_router)
