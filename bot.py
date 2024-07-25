# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

API_ID='2719161'
API_HASH='7cee7c162f09ef31d18425ff64cb6552'
BOT_TOKEN='7140288884:AAHfZOdyTeZKJQmhDnqDL6fu7UlSXVZa1GY'
# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config.API_ID, 
    api_hash=Config.API_HASH, 
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
