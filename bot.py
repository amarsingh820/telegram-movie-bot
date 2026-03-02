from pyrogram import Client, filters
import os

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))  # Jis channel me movie post karoge
ADMIN_ID = int(os.environ.get("ADMIN_ID"))      # ✅ Tumhara admin user ID

app = Client("moviebot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(CHANNEL_ID) & (filters.video | filters.document))
async def new_video(client, message):
    # Video ya document ki details nikalo
    if message.video:
        file_id = message.video.file_id
        file_name = message.video.file_name or "Unknown Video"
    elif message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name or "Unknown File"
    else:
        return
    
    # Link banao
    link = f"https://yoursite.com/stream/{file_id}"
    
    # Admin ko message bhejo
    try:
        await client.send_message(
            chat_id=ADMIN_ID,  # ✅ Admin ko bhejega
            text=f"✅ New Movie Posted!\n\n📁 **File Name:** {file_name}\n\n🔗 **Stream Link:**\n{link}\n\n📋 **File ID:**\n`{file_id}`",
            parse_mode="markdown"
        )
        print(f"✅ Message sent to admin for: {file_name}")
    except Exception as e:
        print(f"❌ Error sending message: {e}")

print("🤖 Bot is running...")
app.run()
