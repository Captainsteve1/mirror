import os
import subprocess
import sys
import time

from pyrogram import Client, filters
from pyrogram.types import Message

from bot2.config import *
from bot2.helpers.decorators import dev_commands
from bot2.logging import LOGGER

prefixes = COMMAND_PREFIXES

commands = ["restart", f"restart@{BOT_USERNAME}"]


@Client.on_message(filters.command(commands, **prefixes))
@dev_commands
async def restart(client, message: Message):
    """
    Restart the bot.
    """

    LOGGER(__name__).info("Restarting the bot. Shutting down this instance")
    print("ok")
    await message.reply_text(
        "`Starting a new instance and shutting down this one`", quote=True
    )
    os.execl(sys.executable, sys.executable, "-m", "bot")
    sys.exit()
