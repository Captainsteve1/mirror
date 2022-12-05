import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from bot2.config import *
from bot2.helpers.decorators import dev_commands

prefixes = COMMAND_PREFIXES
commands = ["ip", f"ip@{BOT_USERNAME}"]


@Client.on_message(filters.command(commands, **prefixes))
@dev_commands
async def ipinfo(client, message: Message):
    """
    Give ip of the server where bot is running.
    """

    response = requests.get("http://ipinfo.io/ip").text
    await message.reply_text(f"IP Address of the server is: `{response}`", quote=True)
