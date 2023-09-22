import asyncio
import importlib

from pyrogram import idle

from SessionGenerator import LOGGER, Sakku
from SessionGenerator.modules import ALL_MODULES


async def Sakku_boot():
    try:
        await Sakku.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("SessionGenerator.modules." + all_module)

    LOGGER.info(f"@{Sakku.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(Sakku_boot())
    LOGGER.info("Stopping String Gen Bot...")
