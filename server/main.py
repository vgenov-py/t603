from flask import Flask, request
from funcs import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


DB="bookshop.json"

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