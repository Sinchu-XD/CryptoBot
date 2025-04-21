import aiosqlite

async def init_db():
    async with aiosqlite.connect("portfolio.db") as db:
        await db.execute("CREATE TABLE IF NOT EXISTS portfolio (user_id INTEGER, coin TEXT, amount REAL)")
        await db.commit()

async def add_coin(user_id, coin, amount):
    async with aiosqlite.connect("portfolio.db") as db:
        await db.execute("INSERT INTO portfolio (user_id, coin, amount) VALUES (?, ?, ?)", (user_id, coin, amount))
        await db.commit()

async def get_portfolio(user_id):
    async with aiosqlite.connect("portfolio.db") as db:
        cursor = await db.execute("SELECT coin, amount FROM portfolio WHERE user_id = ?", (user_id,))
        return await cursor.fetchall()
      
