import os
import sys
import time
from pyrogram import Client, __version__
from pyrogram.raw.all import layer

from bot2.config import API_HASH, API_ID, BOT_TOKEN, BOT_USERNAME
from bot2.logging import LOGGER

BotStartTime = time.time()
plugins = dict(root="bot2/plugins")

if os.path.exists("logs.txt"):
    with open("logs.txt", "r+") as f:
        f.truncate(0)


if sys.version_info[0] < 3 or sys.version_info[1] < 7:
    VERSION_ASCII = """
  =============================================================
  "You MUST need to be on python 3.7 or above, shutting down the bot...
  =============================================================
  """
    LOGGER(__name__).critical(VERSION_ASCII)
    sys.exit(1)

un = f"@{BOT_USERNAME}"

LOGGER(__name__).info(f"Pyrogram v{__version__} (Layer {layer}) started on {un}.")
LOGGER(__name__).info("Telegram Bot Started.")

bot = Client(
    "MultiFunctionBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins,
)  # https://docs.pyrogram.org/topics/smart-plugins
