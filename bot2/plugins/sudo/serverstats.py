import shutil
import time

import psutil
from pyrogram import Client, filters
from pyrogram.types import Message

from bot2 import BotStartTime
from bot2.config import *
from bot2.helpers.decorators import dev_commands, sudo_commands
from bot2.helpers.functions import get_readable_size, get_readable_time

prefixes = COMMAND_PREFIXES


commands = [
    "stats",
    f"stats@{BOT_USERNAME}",
    "serverstats",
    f"serverstats@{BOT_USERNAME}",
]


@Client.on_message(filters.command(commands, **prefixes))
@dev_commands
@sudo_commands
async def update(client, message: Message):

    currentTime = get_readable_time(time.time() - BotStartTime)
    total, used, free = shutil.disk_usage(".")
    total = get_readable_size(total)
    used = get_readable_size(used)
    free = get_readable_size(free)

    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    await message.reply_text(
        f"**≧◉◡◉≦ Bot is Up and Running successfully.**\n\n× Bot Uptime: `{currentTime}`\n× Total Disk Space: `{total}`\n× Used: `{used}({disk_usage}%)`\n× Free: `{free}`\n× CPU Usage: `{cpu_usage}%`\n× RAM Usage: `{ram_usage}%`",
        quote=True,
    )
