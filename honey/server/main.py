from flask import Flask, render_template, request
import requests as req

app = Flask(__name__)
api_route = "http://localhost:3000/api"
@app.route("/")
def home():
    data = req.get("http://localhost:3000/api/collectors").json()["data"]

    return render_template("index.html", collectors=data)

@app.route("/<t_n>", methods=["GET", "POST"])
def get_data(t_n):
    verb = request.method
    is_created = False
    if verb == "POST":
        is_created = req.post(f"http://localhost:3000/api/{t_n}", data=request.form).json()["success"]

    data = req.get(f"http://localhost:3000/api/{t_n}").json()["data"]
    return render_template("index.html", data=data, name=t_n, is_created=is_created)

'''##############################JS:'''

@app.route("/js/<t_n>", methods=["GET", "POST"])
def get_data_js(t_n):
    return render_template("index_js.html")

@app.route("/<t_n>/<id>")
def get_by_id(t_n, id):
    register = req.get(f"http://localhost:3000/api/{t_n}/{id}").json()["data"]
    return render_template("id.html", register=register)
    


@app.route("/new/<t_n>")
def new_collector(t_n):
    return render_template("new.html", t_n=t_n, uri=f"http://localhost:5000/{t_n}")

'''##############################JS:'''

@app.route("/js/new/<t_n>")
def new_collector_js(t_n):
    return render_template("new_js.html")

@app.route("/buy", methods=["GET", "POST"])
def buy():
    if request.method == "POST":
        print(request.form)
        # print(request.form.get("date").replace("-", "/"))

        req.post(f"{api_route}/buy", data=request.form)
    elif request.method == "PUT":
        return "Si ha llegado PUT"
    return render_template("indexa.html")



if __name__ == "__main__":
    app.run(debug=True)