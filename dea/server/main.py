from ast import Return
from flask import Flask, make_response, request, Response, redirect, render_template
import requests as req
import sys
sys.path.append("/Volumes/Datos/t603/dea")
from auth import Auth

api_uri = "http://localhost:3000/api"
SECRET = "4cfa98d37472801305b5d4a85bc98e6a9b4b0213de8762c35336a2b1a586c055"
auth = Auth(SECRET, request,"http://localhost:3000/api/token","http://localhost:5000/login", redirect_uri="http://localhost:5000/secret")
app = Flask(__name__)



@app.route("/login")
@auth.authenticate
def login():
    print(request.url)
    res = make_response(render_template("index.html"))
    return res
    

@app.route("/secret")
@auth.authorize
def secret():
    print(request.cookies)
    return "secret"

@app.route("/finder", methods=["GET", "POST"])
def finder():
    verb = request.method
    if verb == "POST":
        user_lat, user_lon = request.args.values()
        res_api = req.get(f"{api_uri}/finder?lat={user_lat}&lon={user_lon}").json()
        return res_api
    return make_response(render_template("index.html"))


if __name__ == "__main__":
    app.run(debug=True)