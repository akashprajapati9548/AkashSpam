from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_BUTTON = [
    [
        Button.url("🍁 ᴀᴋᴀsʜ", "https://t.me/WTF_NoHope"),
        Button.url("ᴀɴᴏɴʏᴍᴏᴜs 🕸️", "https://t.me/WTF_DyHunt")
    ],
    [
        Button.inline("🥀 ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs 🥀", data="help_back")
    ],
    [
        Button.url("✨ ᴜᴘᴅᴀᴛᴇ", "https://t.me/AnanyaBots"),
        Button.url("sᴜᴘᴘᴏʀᴛ ❄️", "https://t.me/AnanyaBotSupport")
    ],
    [
        Button.url("🌸 ᴊᴏɪɴ ғᴏʀ sᴜᴅᴏ 🌸", "https://t.me/AnanyaAllBots")
    ],
]

clients = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

for client in clients:
    @client.on(events.NewMessage(pattern="/start"))
    async def start(event):
        if event.is_private:
            KEX = await event.client.get_me()
            bot_name = KEX.first_name
            bot_id = KEX.id
            TEXT = (
                f"**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤‌‌‌‌‌‌‌‌★**\n"
                f"**┆**\n"
                f"**┊◍ ʜᴇʏ : [{event.sender.first_name}] **\n"
                f"**┆◍ ɪ ᴀᴍ : [{bot_name}](tg://user?id={bot_id}) **\n"
                f"**┊**\n"
                f"**┆● sᴀɴᴀᴛᴀɴɪ ʙᴏᴛ ᴠᴇʀsɪᴏɴ :** `0.2`\n"
                f"**┊● ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n"
                f"**╰─────────────────────────**\n"
                f"**──────────────────────────**\n"
                f"**⦿ Oᴡɴᴇʀ - [🩵 𝐀𝐊𝐀𝐒𝐇 🌸](https://t.me/WTF_NoHope) | [🩵 𝐀𝐍𝐎𝐍𝐘𝐌𝐎𝐔𝐒 🌸](https://t.me/WTF_DyHunt) **\n"
                f"**──────────────────────────**\n"
                f"**    ❖ Uᴘᴅᴀᴛᴇ's ⏤‌‌‌‌‌‌‌‌ [❖ ∣ Sᴀɴᴀᴛᴀɴɪ Nᴇᴛᴡᴏʀᴋ ∣ ❖](https://t.me/AnanyaBots) **\n"
                f"**──────────────────────────**"
            )
            await event.client.send_file(
                event.chat_id,
                "https://telegra.ph//file/7cfeff721589b61a2f634.jpg",
                caption=TEXT,
                buttons=START_BUTTON
            )
