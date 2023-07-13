from sqlalchemy import insert, select

from bot.common.logger import Logger
from bot.db.schemas import User, UserBalance


class DatabaseUser:
    def __init__(self):
        self.logger = Logger("DatabaseUser").get_logger()

    async def get_user_id(self, tg_id, db_session):
        stmt = select(User.id).where(User.tg_id == tg_id)
        return (await db_session.execute(stmt)).scalar()

    async def create_user(self, tg_id, username, db_session):
        user_id = await self.get_user_id(tg_id, db_session)
        if not user_id:
            params = {
                'tg_id': tg_id,
                'username': username,
            }
            await db_session.execute(insert(User), params)
            await db_session.commit()

    async def get_user_balance(self, db_session, tg_id=None, user_id=None):
        if tg_id:
            stmt = select(UserBalance.btc, UserBalance.usdt).where(User.tg_id == tg_id)
        elif user_id:
            stmt = select(UserBalance.btc, UserBalance.usdt).where(
                UserBalance.user_id == user_id
            )
        else:
            raise Exception()
        return (await db_session.execute(stmt)).all()[0]

    async def create_user_balance(self, user_id, db_session):
        user_balance = await self.get_user_balance(db_session, user_id=user_id)
        if not user_balance:
            params = {
                'user_id': user_id,
                'btc': 0.0015,  # tmp
                'usdt': 840,  # tmp
            }
            await db_session.execute(insert(UserBalance), params)
            await db_session.commit()


database_user = DatabaseUser()
