from bot.repositories.user import user_repository


class UserService:
    async def initiate_user(self, message, db_session):
        tg_id = message.from_user.id,
        username = message.from_user.username,
        await user_repository.create_user(tg_id, username, db_session)
        user_id = await user_repository.get_user_id(tg_id, db_session)
        await user_repository.create_user_balance(user_id, db_session)


user_service = UserService()
