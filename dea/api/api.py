from flask import Flask, request, g, make_response
from flask_cors import CORS
import sqlite3
import utm
import funcs


app = Flask(__name__)
CORS(app)

DB = "./deas.db"

def con():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB)
        db.row_factory = sqlite3.Row
    return db


@app.route("/api")
def api():
    cur = con().cursor()
    for field in cur.execute("SELECT * FROM users;"):
        print(field)
    return "api"

@app.route("/api/token", methods=["PUT", "GET"])
def token():
    cur = con().cursor()
    verb = request.method 
    if verb == "PUT":
        email= request.args.get("email")
        pwd= request.args.get("pwd")
        token= request.args.get("token")

        user = next(cur.execute(f'''SELECT * FROM users WHERE email='{email}';'''), {})
        if dict(user).get("pwd") == pwd:
            cur.execute(f'''UPDATE users SET token='{token}' WHERE email='{email}';''')
            con().commit()
            return {"success": True, "id": user["id"], "token": token}
        return {"success": False, "msg": "User not found!"}

    elif verb == "GET":
        cookie_id = request.args.get("id")
        cookie_token = request.args.get("token")

        print(f"COOKIE_ID: {cookie_id}")
        user = next(cur.execute(f'''SELECT * FROM users WHERE id='{cookie_id}';'''), {})
        print(user)
        print(dict(user).get("token"))
        if dict(user).get("token") == cookie_token:
            print("TOKEN COORERECTORS")
            return {"success": True}

    return {"success": False}

@app.route("/api/finder")
def api_finder():
    user_lat, user_lon = request.args.values()
    user_x, user_y, n, l = utm.from_latlon(float(user_lat), float(user_lon))
    cur = con().cursor()
    result = []
    for dea in cur.execute("SELECT * FROM deas;"):
        dea = dict(dea)
        dea["distance"] = funcs.hypo(user_x, user_y, dea["x"], dea["y"])
        
        try:
            dea_lat, dea_lon = utm.to_latlon(dea["x"], dea["y"],30, "T")
            dea["latlon"] = f'''@{dea_lat},{dea_lon},20z'''
            result.append(dea)
        except:
            pass
    result.sort(key = lambda dea:dea["distance"])
    return {"data": result[0:5]}


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(debug=True, port=3000)