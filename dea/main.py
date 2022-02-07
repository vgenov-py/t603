from distutils.log import debug
from flask import Flask, make_response, redirect, request, Response

app = Flask(__name__)

def token(f):
    def i():
        if request.cookies["a"] == "c":
            return f()
        return redirect("http://localhost:5000")
    return i

@app.route("/")
def home():
    return "Home"

@app.route("/secret")
@token
def secret():
    res = make_response("Secret")
    res.set_cookie("a", "b")
    return res

if __name__ == "__main__":
    app.run(debug=True)