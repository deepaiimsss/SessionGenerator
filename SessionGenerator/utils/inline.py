from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="Generate Session", callback_data="gensession")],
        [
            InlineKeyboardButton(text="Support", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="Channel", url="https://t.me/Aliza_updates"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Pyrogram v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="Pyrogram v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="Telethon", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="Try Again", callback_data="gensession")]]
)
