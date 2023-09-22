from pyrogram import filters
from pyrogram.types import Message

from StringGenerator import Sakku
from StringGenerator.utils import add_served_user, keyboard


@Sakku.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"Hey {message.from_user.first_name},\n\n๏ This is {Sakku.mention},\nAn open source string session generator bot, written in python with the help of pyrogram ].",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
