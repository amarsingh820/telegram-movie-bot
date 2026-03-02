from pyrogram import Client, filters
import os

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
ADMIN_ID = int(os.environ.get("ADMIN_ID"))

app = Client("moviebot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(CHANNEL_ID) & (filters.video | filters.document))
async def new_video(client, message):
    
    if message.video:
        file_id = message.video.file_id
        file_name = message.video.file_name or "Unknown Video"
    elif message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name or "Unknown File"
    else:
        return
    
    link = f"https://yoursite.com/stream/{file_id}"
    
    try:
        await client.send_message(
            chat_id=ADMIN_ID,  # ✅ Ye use karna hai, from_user.id NAHI
            text=f"✅ New Movie!\n\n📁 {file_name}\n\n🔗 Link:\n{link}\n\n📋 File ID:\n`{file_id}`"
        )
        print(f"✅ Sent: {file_name}")
    except Exception as e:
        print(f"❌ Error: {e}")

print("🤖 Bot is running...")
app.run()
