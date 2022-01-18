import sqlite3
import json

from funcs import get_by_id

con = sqlite3.connect("./bookshop.db")
cur = sqlite3.Cursor(con)

# cur.execute('''CREATE TABLE dogs (id TEXT PRIMARY KEY, name TEXT, breed TEXT, age INTEGER);''')
# cur.execute(f'''INSERT INTO dogs VALUES("D_0001", "Kuga", "Chucho", 7);''')
# a = cur.execute('''SELECT * FROM dogs;''')
# print(a)
# con.commit()

# cur.execute('''
# CREATE TABLE books (
#     id TEXT PRIMARY KEY,
#     title TEXT,
#     author TEXT,
#     genre TEXT,
#     stock INTEGER
#     );''')
# INSERT INTO table VALUES ()
def get_all(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)

books = get_all("./bookshop.json")["data"]
b_1 = books[1]
print(tuple(b_1.values()))

# cur.execute(f"DELETE FROM books where stock >= 0")

# BULK INSERTION

# for book in books:
#     cur.execute(f"INSERT INTO books VALUES {tuple(book.values())}")

# con.commit()

# query = "INSERT INTO books VALUES"

# for i, book in enumerate(books):
#     if i < len(books) -1:
#         query += f"{tuple(book.values())},"
#     else:
#         query += f"{tuple(book.values())};"


# print(query)

# cur.execute(query)

# con.commit()