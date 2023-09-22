from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from SessionGenerator import Sakku
from SessionGenerator.utils import get_served_users


@Sakku.on_message(filters.command(["stats", "users"]) & filters.user(OWNER_ID))
async def get_stats(_, message: Message):
    users = len(await get_served_users())
    await message.reply_text(f"Current stats of {Sakku.name} :\n\n {users} users")
