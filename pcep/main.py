import uuid
from venv import create
from flask import Flask, make_response, session, request, render_template, Response
from uuid import uuid4
from hashlib import sha256

from models import db, User, Question, Option, Test, Test_question
import json
from random import shuffle
DB_URI = "multitest.db"



def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_URI}"
    db.init_app(app)    
    return app

app = create_app()

def set_db(app):
    with app.app_context():
        db.create_all()


@app.route("/test_question")
def test_question():
    test = Test.query.first()
    print(test.questions)
    print(test.answers)
    # new_test_question = Test_question(id=uuid4().hex, test_id="3441570236a94d3b8d7a7d9409ab6faa", question_id="7447ebc5f9c849459c1fff5f9c628ab4", user_choice="e25e44bb5add4d46ac99ad9556b0f3bd")
    # db.session.add(new_test)
    # db.session.commit()
    return "TEST QUESTIONS"



@app.route("/", methods=["GET", "POST"])
def query():
    questions = Question.query.all()
    shuffle(questions)
    (shuffle(question.options) for question in questions[0:10])
    res = make_response(render_template("test.html", questions=questions[0:10]))
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
                
            question = Question(id=q_id, q=question["question"], a=a)
            db.session.add(question)
            # db.session.commit()
    return "create"

@app.route("/api/grade", methods=["GET", "POST"])
def coo():
    if request.method == "POST":
        q_a = Question.dict_q_a() # q_id q a "q_id": "q_a"
        
        answers = request.get_json()
        result = {"grade": 0, "answers":{}}
        for answer in answers:
            result["answers"][answer[1]] = False
            if q_a[answer[0]] == answer[1]:
                result["grade"] += 1
                result["answers"][answer[1]] = True

            
    return result



if __name__ == "__main__":
    app.run(debug=True)