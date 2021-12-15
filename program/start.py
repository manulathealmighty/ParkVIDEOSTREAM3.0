from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Welcome {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **𝖠𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗉𝗅𝖺𝗒 𝗆𝗎𝗌𝗂𝖼 𝖺𝗇𝖽 𝗏𝗂𝖽𝖾𝗈 𝗈𝗇 𝗀𝗋𝗈𝗎𝗉𝗌 𝗍𝗁𝗋𝗈𝗎𝗀𝗁 𝗍𝗁𝖾 𝗇𝖾𝗐 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆'𝗌 𝗏𝗂𝖽𝖾𝗈 𝖼𝗁𝖺𝗍𝗌!**

💡 **𝖥𝗂𝗇𝖽 𝗈𝗎𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖡𝗈𝗍'𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝗁𝗈𝗐 𝗍𝗁𝖾𝗒 𝗐𝗈𝗋𝗄 𝖻𝗒 𝖼𝗅𝗂𝖼𝗄𝗂𝗇𝗀 𝗈𝗇 𝗍𝗁𝖾 » 📚 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖻𝗎𝗍𝗍𝗈𝗇!**

🔖 **𝗧𝗼 𝗸𝗻𝗼𝘄 𝗵𝗼𝘄 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗰𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 » ❓ 𝗕𝗮𝘀𝗶𝗰 𝗚𝘂𝗶𝗱𝗲 𝗯𝘂𝘁𝘁𝗼𝗻!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("❤️ 𝖣𝗈𝗇𝖺𝗍𝖾/𝖢𝗈𝗇𝗍𝖺𝖼𝗍", url=f"https://t.me/ucant_surpassmebruh"),
                ],
                [
                    InlineKeyboardButton(
                        "🔆 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📢 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Source Code", url="https://github.com/manulathealmighty/ParkVIDEOSTREAM3.0"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ Chat Group", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📢 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 PyTgCalls version: `{pytover.__version__}`\n✨ Uptime Status: `{uptime}`\n\n**Thank you very much for adding me here❕ I will entertain you by playing video & music on your group's video chat** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "❤️ **𝚃𝚑𝚊𝚗𝚔𝚜 𝚏𝚘𝚛 𝚊𝚍𝚍𝚒𝚗𝚐 𝚖𝚎 𝚝𝚘 𝚝𝚑𝚎 𝙶𝚛𝚘𝚞𝚙 !**\n\n"
                "**𝙿𝚛𝚘𝚖𝚘𝚝𝚎 𝚖𝚎 𝚊𝚜 𝚊𝚍𝚖𝚒𝚗𝚒𝚜𝚝𝚛𝚊𝚝𝚘𝚛 𝚘𝚏 𝚝𝚑𝚎 𝙶𝚛𝚘𝚞𝚙, 𝚘𝚝𝚑𝚎𝚛𝚠𝚒𝚜𝚎 𝙸 𝚠𝚒𝚕𝚕 𝚗𝚘𝚝 𝚋𝚎 𝚊𝚋𝚕𝚎 𝚝𝚘 𝚠𝚘𝚛𝚔 𝚙𝚛𝚘𝚙𝚎𝚛𝚕𝚢, 𝚊𝚗𝚍 𝚍𝚘𝚗'𝚝 𝚏𝚘𝚛𝚐𝚎𝚝 𝚝𝚘 𝚝𝚢𝚙𝚎 /𝚞𝚜𝚎𝚛𝚋𝚘𝚝𝚓𝚘𝚒𝚗 𝚏𝚘𝚛 𝚒𝚗𝚟𝚒𝚝𝚎 𝚝𝚑𝚎 𝚊𝚜𝚜𝚒𝚜𝚝𝚊𝚗𝚝.**\n\n"
                "**𝙾𝚗𝚌𝚎 𝚍𝚘𝚗𝚎, 𝚝𝚢𝚙𝚎** /𝚛𝚎𝚕𝚘𝚊𝚍",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📢 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("🔆 Support", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("👤 Assistant", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )
