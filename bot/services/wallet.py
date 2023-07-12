from bot.common import constants
from bot.repositories.user import user_repository
from bot.services.coingecko import coingecko_service


class WalletService:
    async def get_wallet_data(self, db_session, user_tg_id):
        btc, usdt = await user_repository.get_user_balance(db_session=db_session, tg_id=user_tg_id)

        if btc:
            btc_price = (await coingecko_service.get_price('bitcoin', 'rub'))['bitcoin']['rub']
            btc_rub_equivalent = constants.MAIN_MENU['rub_equivalent'].format(
                rub=round(btc_price * btc)
            )
        else:
            btc_rub_equivalent = ''

        if usdt:
            usdt_price = (await coingecko_service.get_price('tether', 'rub'))['tether']['rub']
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


wallet_service = WalletService()
