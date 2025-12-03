# main.py
from pyrogram import Client, filters
from config import 8406520934:AAG6DBUXj-3Wye7dJAbfTGU_FjmOYeRfcDM, 35463925, ce55193ef9d3f6894cdf61a268947c09, COOKIE

# Create Telegram Client
app = Client("Teraboxdownloaderrr", bot_token=8406520934:AAG6DBUXj-3Wye7dJAbfTGU_FjmOYeRfcDM, api_id=35463925, api_hash=ce55193ef9d3f6894cdf61a268947c09)

# Start command
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(
        "Hello! Send me a TeraBox link and I will fetch the file for you."
    )

# Message handler for links
@app.on_message(filters.private)
async def handle_link(client, message):
    link = message.text.strip()
    if "terabox.com" in link:
        # Placeholder: Download logic here
        await message.reply_text(f"Processing your link: {link}\nDownloading soon...")
        # TODO: Implement TeraBox download using COOKIE / requests / API
    else:
        await message.reply_text("Send a valid TeraBox link!")

# Run the bot
app.run()
