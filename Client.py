from Config import API_ID, API_HASH, BOT_TOKEN
from pyrogram import Client


app = Client("CryptoBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
