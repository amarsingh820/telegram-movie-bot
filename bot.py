from pyrogram import Client, filters
import os

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))  # -1001234567890

app = Client("moviebot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(CHANNEL_ID) & filters.video)
async def new_video(client, message):
    file_id = message.video.file_id
    file_name = message.video.file_name or "Unknown"
    
    # Link generate karo
    link = f"https://yourname.is-a.dev/stream/{file_id}"
    
    # Tumhe bhej do
    await client.send_message(
        chat_id="YOUR_USER_ID",  # Apna user ID daalo
        text=f"✅ New Movie!\n\n📁 {file_name}\n🔗 {link}"
    )

print("Bot is running...")
app.run()
