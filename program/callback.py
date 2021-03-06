# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ูุชูุญ ูู ุชุดุบูู ุงูููุณููู ูุงูููุฏูู ูู ูุฌููุนุงุช ูู ุฎูุงู ูุญุงุฏุซุงุช ุงูููุฏูู ุงูุฌุฏูุฏุฉ ูู Telegram!!**

๐ก **ููุนุฑูุฉ ุฌููุน ุงูุงูุฑ ุงูุจูุช ุงุถุบุท ุนูู ยป ๐ ุฒุฑุงุฑ ุงูุงูุงูุฑ!**

๐ **ููุนุฑูู ุทุฑููู ุงุณุชุฎุฏุงู ุงุถุบุท ุนูู ูููู  ยป โ ุฒุฑุงุฑ ุงูุฏููู ุงูุงุณุงุณู!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ ุงุถุบุท ูุงุถุงูุชูู ุงูู ุฌุฑูุจูโ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("โุงูุฏููู ุงูุงุณุงุณู", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("๐ ุงูุงููุฑ", callback_data="cbcmds"),
                    InlineKeyboardButton("โค ุงููุงูู", url=f"https://t.me/Q_X_I_T"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฅ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "ุงููุจุฑูุฌ(dev eัlaะผ)", url="https://t.me/Q_X_I_T"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ **Basic Guide for using this bot:**

1.) **ุงููุง ูู ุจุฅุถุงูุฉ ุงูุจูุช ูู ูุฌููุนุชู.**
2.) **ุซุงููุง ูู ุจุฑูุนู ูุณุคู ูุงุนุทุงุฆู ุฌููุน ุงูุตูุงุญูุงุช ุนุฏุง ุงูุจูุงุก ูุชุฎููุง.**
3.) **ุจุนุฏ ุชุฑููุชู ุ ุงูุชุจ /reload ูู ูุฌููุนุฉ ูุชุญุฏูุซ ุจูุงูุงุช ุงููุณุคูู.**
3.) ูู ุจุฅุถุงูุฉ @{ASSISTANT_NAME} ูุฌุฑูุจู ุงู ุชูุชุจ .ุงูุถู ูุฏุนูุฉ ุญุณุงุจ ุงููุณุงุนุฏ.**
4.) **ูู ุจูุชุญ ุฏุฑุฏุดุฉ ุตูุชูู ุงููุง ูุจู ุชุดุบูู ูุฏูู/ุงุบููู/.**
5.) **ูู ุจุนุถ ุงูุฃุญูุงู ุ ูุชู ุฅุนุงุฏุฉ ุชุญููู ุงูุฑูุจูุช ุจุงุณุชุฎุฏุงู /reload ูููู ุฃู ูุณุงุนุฏู ุงูุฃูุฑ ูู ุญู ุจุนุถ ุงููุดููุงุช.**

๐ **ุฅุฐุง ูู ููุถู ุงููุณุชุฎุฏู ุจูุช ุฅูู ุฏุฑุฏุดุฉ ุงูููุฏูู ุ ูุชุฃูุฏ ูู ุชุดุบูู ุฏุฑุฏุดุฉ ุงูููุฏูู ุจุงููุนู ุ ุฃู ุงูุชุจ /userbotleave ุซู ุงูุชุจ /userbotjoin ุชูุฑุงุฑุง.**

๐ก **ุฅุฐุง ูุงูุช ูุฏูู ุฃุณุฆูุฉ ูุชุงุจุนุฉ ุญูู ูุฐุง ุงูุฑูุจูุช ุ ูููููู ุฅุฎุจุงุฑู ูู ุฎูุงู ุฏุฑุฏุดุฉ ุงูุฏุนู ุงูุฎุงุตุฉ ุจู ููุง: @{GROUP_SUPPORT}**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุงูุฑุฌูุน", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

ยป **press the button below to read the explanation and see the list of available commands !**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ท๐ป ุงูุงูุฑ ุงูุงุฏูู", callback_data="cbadmin"),
                    InlineKeyboardButton("๐ง๐ป ุงููุทูุฑ ุงูุงุณุงุณู", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("๐ ุงูุงูุฑ ุงูุดุชุบูู", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("๐ ุงูุฑุฌูุน", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the basic commands:

ยป /mplay (song name/link) - play music on video chat
ยป /vplay (video name/link) - play video on video chat
ยป /vstream - play live video from yt live/m3u8
ยป /playlist - show you the playlist
ยป /video (query) - download video from youtube
ยป /song (query) - download song from youtube
ยป /lyric (query) - scrap the song lyric
ยป /search (query) - search a youtube video link

ยป /ping - show the bot ping status
ยป /uptime - show the bot uptime status
ยป /alive - show the bot alive info (in group)

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุงูุฑุฌูุน", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the admin commands:

ยป .ุดุบู - ูุชุดุบูู ุงูุงุบุงูู๐
ยป .ููุฏูู - ูุชุดุบูู ุงูููุฏูููุงุช๐
ยป .ูุงูู - ูุชุดุบูู ูุงูู ๐
ยป .ุงูุถู - ูุงูุถูุงู ุญุณุงุจ ูุณุงุนุฏ ๐
ยป .ุงุฎุฑุฌ - ุฎุฑูุฌ ุญุณุงุจ ูุณุงุนุฏ ูู ุงูุฌุฑูุจ ๐
ยป .ุงููุงู - ูุงููุงู ุชุดุบูู ุงูุงุบููู ๐
ยป .reload - ุงุนุงุฏู ุชุดุบูู ุฎุงุตู ุจุงูุงุฏูู

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุงูุฑุฌูุน", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the sudo commands:

ยป /rmw - clean all raw files
ยป /rmd - clean all downloaded files
ยป /sysinfo - show the system information
ยป /update - update your bot to latest version
ยป /restart - restart your bot
ยป /leaveall - order userbot to leave from all group

โก __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุงูุฑุฌูุน", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nยป revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"โ๏ธ **settings of** {query.message.chat.title}\n\nโธ : pause stream\nโถ๏ธ : resume stream\n๐ : mute userbot\n๐ : unmute userbot\nโน : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("โน", callback_data="cbstop"),
                      InlineKeyboardButton("โธ", callback_data="cbpause"),
                      InlineKeyboardButton("โถ๏ธ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("๐", callback_data="cbmute"),
                      InlineKeyboardButton("๐", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("๐ Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("โ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
