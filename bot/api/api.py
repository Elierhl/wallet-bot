from aiogram import Router

from bot.api.routers.callbacks.deposit import router as deposit_callback_router
from bot.api.routers.callbacks.menu import router as menu_callback_router
from bot.api.routers.callbacks.wallet import router as wallet_callback_router
from bot.api.routers.callbacks.withdraw import router as withdraw_callback_router
from bot.api.routers.commands.menu import router as menu_command_router
from bot.api.routers.commands.start import router as start_command_router
from bot.api.routers.commands.wallet import router as wallet_command_router

router = Router(name="api-router")

router.include_router(menu_callback_router)
router.include_router(wallet_callback_router)
router.include_router(deposit_callback_router)
router.include_router(withdraw_callback_router)

router.include_router(menu_command_router)
router.include_router(start_command_router)
router.include_router(wallet_command_router)
