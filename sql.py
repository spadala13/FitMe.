import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("""CREATE TABLE users (
            id INTEGER NOT NULL,
            username TEXT NOT NULL,
            hash TEXT NOT NULL,
            recipes NUMERIC NOT NULL DEFAULT 0,
            PRIMARY KEY (id))""")

c.execute("""CREATE TABLE recipes (
            id INTEGER NOT NULL,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            date DATE NOT NULL,
            ingredients TEXT NOT NULL,
            directions TEXT NOT NULL,
            total INTEGER)""")

conn.commit()
conn.close()

