from bot.common import constants
from bot.db.user import database_user
from bot.services.external.coingecko import coingecko_service


class MenuController:
    async def initiate_user(self, message):
        tg_id = message.from_user.id
        username = message.from_user.username
        await database_user.create_user(tg_id, username)
        user_id = await database_user.get_user_id(tg_id)
        await database_user.create_user_balance(user_id)

    async def get_wallet_data(self, tg_id):
        btc, usdt = await database_user.get_user_balance(tg_id=tg_id)

        if btc:
            btc_price = (await coingecko_service.get_price('bitcoin', 'rub'))[
                'bitcoin'
            ]['rub']
            btc_rub_equivalent = constants.MAIN_MENU['rub_equivalent'].format(
                rub=round(btc_price * btc)
            )
        else:
            btc_rub_equivalent = ''

        if usdt:
            usdt_price = (await coingecko_service.get_price('tether', 'rub'))['tether'][
                'rub'
            ]
            usdt_rub_equivalent = constants.MAIN_MENU['rub_equivalent'].format(
                rub=round(usdt_price * usdt)
            )
        else:
            usdt_rub_equivalent = ''

        return {
            "btc": btc,
            "usdt": usdt,
            "btc_rub_equivalent": btc_rub_equivalent,
            "usdt_rub_equivalent": usdt_rub_equivalent,
        }


menu_controller = MenuController()
