from flask import Flask, request, g
from funcs import *
import sqlite3 

app = Flask(__name__)

DB="./bookshop.db"

def con():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB)
    return db

@app.route("/")
def home():
    return {
        "/test": "Test the app",
        "/all": "To get all the books",
        "/book/<book_id>": "Get a book by ID"
    }

@app.route("/test", methods=["GET", "POST", "PUT"])
def test():
    
    if request.method == "GET":
        return f"Has utilizado el método {request.method}"
    elif request.method == "PUT":
        return dict(request.args)
    elif request.method == "POST":
        return dict(request.form)
    
    

@app.route("/all")
def all():
    return get_all(DB)

    








@app.route("/db_all")
def get_db_all():
    cur = con().cursor()
    result = {"data": []}
    fields = tuple(field[1] for field in cur.execute("PRAGMA table_info(books);"))
    query = "SELECT * FROM books"
    if request.args:
        query += f"ORDER BY {request.args['sort']};"
    else:
        query += ";"
    query = f"SELECT * FROM books ORDER BY {request.args['sort']}" if request.args else "SELECT * FROM books"
    for book in cur.execute(query):
        # dict_book = {}
        # for i, field in enumerate(fields):
        #     dict_book[field] = book[i]
        # result["data"].append(dict_book)
        result["data"].append(dict(zip(fields, book)))
    

    
    return result


@app.route("/book/<book_id>", methods=["GET", "DELETE", "PUT"])
def book_by_id(book_id):
    verb = request.method
    if verb == "GET":
        result = {}
        book_found = get_by_id(book_id)
        if book_found:
            result["success"] = True
            result["book"] = book_found
        else:
            result["success"] = False
        return result

    elif verb == "DELETE":
        if delete_by_id(book_id):
            return {"sucess": True}
        else:
            return {"sucess": False}
    
    elif verb == "PUT":
        if update_book(book_id, request):
            return "Libro actualizado"
        return "Libro no encontrado"


if __name__ == "__main__":
    app.run(debug=True)