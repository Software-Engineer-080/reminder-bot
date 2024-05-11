from storage import owner
from aiogram.types import Message
from aiogram.filters import BaseFilter


class IsOwner(BaseFilter):

    def __init__(self) -> None:
        pass

    async def __call__(self, message: Message) -> bool:

        user_id = message.from_user.id

        return user_id == owner
