from flask import Flask, make_response, session, request, render_template, Response
from uuid import uuid4
from hashlib import sha256
from models import db, User, Question, Option
import json
app = Flask(__name__)
DB_URI = "multitest.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_URI}"
app.config["SECRET_KEY"] = "secret"
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def query():
    result = 0
    questions = Question.query.all()
    # print(questions[2].a)
    # print([option for option in questions[2].options if option.id == questions[2].a])
    session["id"] = "session_cookie"
    res = make_response(render_template("index.html", questions=questions))
    res.set_cookie("id", "id_set_cookie")
    return res

@app.route("/create")
def create_qs():
    def get_data():
        with open("pcep.json") as file:
            return json.load(file)
    qs = get_data()
    for block in list(qs.values())[1:]:
        for question in block:
            q_id = uuid4().hex
            for i, option in enumerate(question["options"]):
                o_id = uuid4().hex
                if i == question["answer"]:
                    a = o_id
                option = Option(id=o_id, o=option, question_id=q_id)
                db.session.add(option)
                print(f"OPTION: {option}")
            question = Question(id=q_id, q=question["question"], a=a)
            db.session.add(question)
            # db.session.commit()

            print(question)
    return "create"

@app.route("/cookie", methods=["GET", "POST"])
def coo():
    print(request.cookies)
    return {"res":"cookie"}



if __name__ == "__main__":
    app.run(debug=True)