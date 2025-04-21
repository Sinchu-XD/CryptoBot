from pyrogram import Client
from Config import API_ID, API_HASH, BOT_TOKEN
from Utils.Db import init_db
import Handlers.Price
import Handlers.PortFolio

app = Client("CryptoBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message()
async def start_handler(_, message):
    if message.text == "/start":
        await message.reply("👋 Welcome to CryptoBot!\nUse /price BTC, /add, /portfolio, /nft(soon), /whale(soon)")

app.run(init_db())
