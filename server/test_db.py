import sqlite3


con = sqlite3.connect("./bookshop.db")
cur = sqlite3.Cursor(con)

cur.execute('''
CREATE TABLE books (
    id TEXT PRIMARY KEY,
    title TEXT,
    author TEXT,
    genre TEXT,
    stock INTEGER
    );''')
