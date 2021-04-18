from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.first_name}!
I am AVENGERS-MUSIC-BOT  VC Music Player, an open-source bot that lets you play music in your Telegram groups.
My music assistant ☺️ - @avengersmusicassistent
Maintained by @monumishra007 ❤
For source code Join our support group @avengers_help.
Use the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Command", url="https://telegra.ph/AVENGERS-MUSIC-BOT-04-18%B2%F0%9D%97%B2%F0%9D%97%BB%F0%9D%97%95%F0%9D%97%BC%F0%9D%98%81-04-03",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url="https://t.me/avengers_help"
                    ),
                    InlineKeyboardButton(
                        "🥺 REPO", url="https://github.com/MONU-MISHRA/AVENGERS-MUSIC-BOT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Join Channel", url="https://t.me/avengers_channel"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
