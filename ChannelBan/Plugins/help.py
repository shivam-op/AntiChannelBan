from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command(["help", "help@ChannelBanRobot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hii {message.from_user.first_name} 😉️!</b>
 `There is nothing in help cmd just add the bot and give all rights then watch`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📢 Cʜᴀɴɴᴇʟ", url="https://t.me/electro_updates"
                    ),
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ 👥", url="https://t.me/electrobot_support"
                    )
                ]   
            ]
        )
    )
