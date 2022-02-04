from flask import Flask, g, request, Response
from flask_cors import CORS
import sqlite3

from funcs import *
app = Flask(__name__)
CORS(app)
DATABASE = "./honey.db"
def con():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route("/newcollector")
def new_collector():
    return "hola"

@app.route("/api/<t_n>", methods=["GET", "POST"])
def get_tn(t_n):
    verb = request.method
    print(verb)
    if verb == "POST":
        # insert_into(con, t_n,request.form)
        print(request.form)
        return {"success": True}

    return Response(get_all(con, t_n), content_type="application/json")
    # return get_all(con, t_n)

@app.route("/api/<t_n>/<id>", methods=["GET", "PUT", "POST"])
def get_id_on_tn(t_n, id):
    if request.method == "GET":
        data = get_by_id(con, t_n, id)
        if data:
            return Response(data, content_type="application/json")
        else:
            return {"data": {"success": False}}
    elif request.method == "PUT":
        return "PUT"
    else:
        return "POST"

# @app.route("/api/collectors", methods=["GET", "POST"])
# def collectors():
#     verb = request.method
#     if verb == "POST":
#         # insert_into(con,"collectors",request.form)
#         print(request.form)
#         return {"success": True}

#         # return "Collector creado"
    
#     return Response(get_all(con, "collectors"), content_type="application/json")

# @app.route("/api/providers", methods=["GET", "POST"])
# def providers():
#     verb = request.method
#     if verb == "POST":
#         # insert_into(con,"providers",request.form)
#         print(request.form)
#         return {"success": True}
#     return get_all(con, "providers")

# @app.route("/api/purchases", methods=["GET", "POST"])
# def purchases():
#     return get_all(con, "purchases")

'''
date: ISO(YYYY/MM/DD)
price: float
quantity: float
id_collector: ID
id_provider: ID

UPDATE collectors SET quantity = quantity + {request.form["quantity"]} where id = "{request.form["id_collector"]}"}

INSERT INTO <TABLE> VALUES();
'''

@app.route("/daniel", methods=["POST"])
def daniel():
    t_n = "providers"
    cur = con().cursor()
    fields = tuple(field[1] for field in cur.execute(f"PRAGMA table_info({t_n})"))
    # print(fields)
    values = [gen_id(cur, t_n)]
    for field in fields[1:]:
        try:
            values.append(f"'{request.form[field]}'")
        except KeyError:
            return "Keys mal"
    
    cur.execute(f"INSERT INTO {t_n} VALUES{tuple(values)};")
    print(f"INSERT INTO {t_n} VALUES(".join(values) + ");")
    # print(f"INSERT INTO {t_n} VALUES({*values});")
    # con().commit()
    

    return "Testing"

@app.route("/api/buy", methods=["POST"])
def buy():
    pass

if __name__ == "__main__":
    app.run(debug=True, port=3000)