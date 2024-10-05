import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from Script import script
from info import ADMINS

@Client.on_message(filters.command("admin_cmds") & filters.user(ADMINS))
async def admin_cmds(client, message):
    buttons = [
        [KeyboardButton("/refresh"), KeyboardButton("/set_muc")],
        [KeyboardButton("⚡ powered by @MoviesHubFree4You")]
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
   
    sent_message = await message.reply(
        "<b>Admin All Commands [auto delete 2 min] 👇</b>",
        reply_markup=reply_markup,
    ) 
    #  2 minutes (120 seconds)
    await asyncio.sleep(120)
    await sent_message.delete()
    await message.delete()
