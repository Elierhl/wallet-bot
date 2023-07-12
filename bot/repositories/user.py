from sqlalchemy import select, insert

from bot.schemas.user import UserBalance, User


class UserRepository:
    async def get_user_balance(self, db_session, tg_id):
        stmt = select(UserBalance.btc, UserBalance.usdt).where(User.tg_id == tg_id)
        return (await db_session.execute(stmt)).all()[0]

    async def create_user_balance(self, user_id, db_session):
        params = {
            'user_id': user_id,
            'btc': 0.0015,  # tmp
            'usdt': 840,  # tmp
        }
        await db_session.execute(insert(UserBalance), params)
        await db_session.commit()

    async def create_user(self, tg_id, username, db_session):
        params = {
            'tg_id': tg_id,
            'username': username,
        }
        await db_session.execute(insert(User), params)
        await db_session.commit()

    async def get_user_id(self, tg_id, db_session):
        stmt = select(User.id).where(User.tg_id == tg_id)
        return (await db_session.execute(stmt)).scalar()


user_repository = UserRepository()
