import sqlite3 as sq

from config import db_name

db = sq.connect(db_name)
cur = db.cursor()

async def db_start():
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                tg_id INTEGER UNIQUE NOT NULL,
                username TEXT NOT NULL,
                group VARCHAR(7),
                running_cases_id TEXT,
                balance INTEGER DEFAULT 0
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS cases (
                id INTEGER PRIMARY KEY,
                description TEXT NOT NULL,
                customer_tg_id INT NOT NULL,
                date_of_appeal DATETIME NOT NULL,
                date_of_closing DATETIME,
                subject TEXT
    )
    ''')

    await db.commit()

# КОЛ-ВО СИМВОЛОВ группы 7 
async def create_user(tg_id, group):
    cur.execute(f'''
    INSERT INTO users(tg_id, group) VALUES ({tg_id}, {group})
    ''')
    await db.commit()
