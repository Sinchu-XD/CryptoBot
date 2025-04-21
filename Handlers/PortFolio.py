from pyrogram import filters, Client as app
from Utils.Db import add_coin, get_portfolio
import aiohttp

@app.on_message(filters.command("add"))
async def add_coin_to_portfolio(_, message):
    if len(message.command) != 3:
        return await message.reply("Usage: /add BTC 0.5")

    coin = message.command[1].lower()
    try:
        amount = float(message.command[2])
    except ValueError:
        return await message.reply("Invalid amount.")

    await add_coin(message.from_user.id, coin, amount)
    await message.reply(f"✅ Added {amount} {coin.upper()} to your portfolio.")

@app.on_message(filters.command("portfolio"))
async def show_portfolio(_, message):
    portfolio = await get_portfolio(message.from_user.id)
    if not portfolio:
        return await message.reply("🪙 Your portfolio is empty.")

    msg = "📊 **Your Portfolio**\n\n"
    total_usd = 0

    async with aiohttp.ClientSession() as session:
        for coin, amount in portfolio:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
            async with session.get(url) as resp:
                data = await resp.json()

            if coin in data:
                price = data[coin]["usd"]
                total = round(price * amount, 2)
                total_usd += total
                msg += f"🔸 {coin.upper()}: {amount} ≈ ${total}\n"

    msg += f"\n💵 **Total:** ${round(total_usd, 2)}"
    await message.reply(msg)
  
