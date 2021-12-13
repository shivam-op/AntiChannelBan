from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command(["start", "start@ChannelBanRobot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hii {message.from_user.first_name} 😉️!</b>
 `Heya I'm A Anti Channel Telegram bot to delete and ban message sent by channel`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📢 Cʜᴀɴɴᴇʟ", url="https://t.me/electro_updates"
                    ),
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ 👥", url="https://t.me/electrobot_suppory"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧑‍💻 Dᴇᴠ 🧑‍💻", url="https://t.me/smartybhai"
                    )
                ]
            ]
        )
    )
