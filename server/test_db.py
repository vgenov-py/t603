import sqlite3


con = sqlite3.connect("./bookshop.db")
cur = sqlite3.Cursor(con)

# cur.execute('''CREATE TABLE dogs (id TEXT PRIMARY KEY, name TEXT, breed TEXT, age INTEGER);''')
# cur.execute(f'''INSERT INTO dogs VALUES("D_0001", "Kuga", "Chucho", 7);''')
# a = cur.execute('''SELECT * FROM dogs;''')
# print(a)
# con.commit()

cur.execute('''
CREATE TABLE books (
    id TEXT PRIMARY KEY,
    title TEXT,
    author TEXT,
    genre TEXT,
    stock INTEGER
    );''')