from bot.common import constants
from bot.db.user import database_user
from bot.services.base import Controller
from bot.services.external.coingecko import coingecko_service


class MenuController(Controller):
    def __init__(self):
        super().__init__(module_name=__name__)

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

    async def get_transactions_list(self, tg_id, callback_data):
        transactions = await database_user.get_transactions(
            tg_id=tg_id, limit=10, offset=10 * (callback_data.number - 1)
        )
        if not transactions:
            return constants.TRANSACTIONS['empty_transactions']

        transactions_list = []
        for num, trans in enumerate(transactions, start=1):
            trans = trans[0]
            number = 10 * (callback_data.number - 1) + num
            row = f'#{number} Transaction {trans.id}, data {trans.data}\n'  # some formatting
            transactions_list.append(row)

        transactions_text = '\n'.join(transactions_list)
        total_transactions = await database_user.get_total_transactions(tg_id=tg_id)
        total_pages = total_transactions // 10 + 1

        return transactions_text, total_pages


menu_controller = MenuController()
