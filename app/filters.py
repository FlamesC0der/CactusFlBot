from aiogram.filters import Filter
from aiogram.types import Message


class IsAdmin(Filter):
    def __init__(self, admins_ids: list[int]):
        self.admins_ids = admins_ids

    async def __call__(self, message: Message):
        return message.from_user.id in self.admins_ids
