from pyrogram import Client as app, filters
import aiohttp
from Main import app

@app.on_message(filters.command("price"))
async def get_price(_, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /price BTC")

    coin = message.command[1].lower()

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()

    if coin in data:
        price = data[coin]["usd"]
        await message.reply(f"💰 Current price of **{coin.upper()}**: ${price}")
    else:
        await message.reply("❌ Coin not found.")
      
