from pyrogram import Client, filters
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

@Client.on_message(filters.command("price"))
async def price_handler(client, message):
    try:
        coin_symbol = message.text.split()[1].lower()
        coin_data = cg.get_price(ids=coin_symbol, vs_currencies='usd')
        
        if coin_symbol in coin_data:
            price = coin_data[coin_symbol]['usd']
            await message.reply(f"🪙 {coin_symbol.upper()} is currently ${price}")
        else:
            await message.reply("❌ Coin not found. Please check the coin symbol.")
    
    except IndexError:
        await message.reply("❌ Please provide a coin symbol, e.g., /price BTC.")
    except Exception as e:
        await message.reply(f"❌ Something went wrong: {e}")
