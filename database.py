import aiosqlite
from datetime import date

DB = "users.db"

async def init():
    async with aiosqlite.connect(DB) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER,
            date TEXT,
            used INTEGER
        )
        """)
        await db.commit()


async def can_use(user_id):
    today = str(date.today())

    async with aiosqlite.connect(DB) as db:
        cur = await db.execute(
            "SELECT used FROM users WHERE user_id=? AND date=?",
            (user_id, today)
        )
        row = await cur.fetchone()

        if not row:
            await db.execute(
                "INSERT INTO users VALUES (?, ?, ?)",
                (user_id, today, 0)
            )
            await db.commit()
            return True

        return row[0] < 1


async def add_use(user_id):
    today = str(date.today())

    async with aiosqlite.connect(DB) as db:
        await db.execute("""
        UPDATE users
        SET used = used + 1
        WHERE user_id=? AND date=?
        """, (user_id, today))
        await db.commit()