from sqlalchemy import insert, select

from bot.db.schemas import User, UserBalance
from bot.db.utils import Database


class DatabaseUser(Database):
    def __init__(self):
        super().__init__(module_name=__name__)

    async def get_user_id(self, tg_id):
        async with self.session_pool() as session:
            stmt = select(User.id).where(User.tg_id == tg_id)
            return (await session.execute(stmt)).scalar()

    async def create_user(self, tg_id, username):
        user_id = await self.get_user_id(tg_id)
        if not user_id:
            params = {
                'tg_id': tg_id,
                'username': username,
            }
            async with self.session_pool() as session:
                await session.execute(insert(User), params)
                await session.commit()

    async def get_user_balance(self, tg_id=None, user_id=None):
        if tg_id:
            stmt = select(UserBalance.btc, UserBalance.usdt).where(User.tg_id == tg_id)
        elif user_id:
            stmt = select(UserBalance.btc, UserBalance.usdt).where(
                UserBalance.user_id == user_id
            )
        else:
            raise Exception()  # TO DO
        async with self.session_pool() as session:
            return (await session.execute(stmt)).first()

    async def create_user_balance(self, user_id):
        user_balance = await self.get_user_balance(user_id=user_id)
        if not user_balance:
            params = {
                'user_id': user_id,
                'btc': 0.0015,  # tmp
                'usdt': 840,  # tmp
            }
            async with self.session_pool() as session:
                await session.execute(insert(UserBalance), params)
                await session.commit()


database_user = DatabaseUser()
