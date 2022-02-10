from flask import Flask, make_response, request, Response, redirect, render_template
import requests as req
import sys
sys.path.append("/home/kuga/cice/t603/dea")
from auth import Auth


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


if __name__ == "__main__":
    app.run(debug=True)