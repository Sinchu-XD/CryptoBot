from pyrogram import Client, idle
import asyncio
import os
from Utils.Db import init_db
import importlib
import Handlers.Price
import Handlers.PortFolio

from Client import app

def load_plugins():
    plugin_dir = "Handlers"
    for file in os.listdir(plugin_dir):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = f"{plugin_dir}.{file[:-3]}"
            importlib.import_module(module_name)


@app.on_message()
async def start_handler(_, message):
    if message.text == "/start":
        await message.reply(
            "👋 Welcome to CryptoBot!\n\n"
            "Commands:\n"
            "• /price BTC\n"
            "• /add\n"
            "• /portfolio\n"
            "• /nft (Soon)\n"
            "• /whale (Soon)"
        )

async def main():
    await init_db()
    load_plugins()
    await app.start()
    print("✅ Bot Started")
    await idle()
    await app.stop()
    await asyncio.get_event_loop().create_future()

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        print("🛑 Bot stopped manually.")
