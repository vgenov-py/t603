from flask import Blueprint, render_template, make_response
from models import db
from sqlalchemy import ForeignKey
from uuid import uuid4
from random import shuffle

tests = Blueprint("tests", __name__)

class Test(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    user_id = db.Column(db.String(32), ForeignKey("user.id"))
    grade = db.Column(db.Float, nullable=True)

    questions = db.relationship("Question",secondary="test_question", backref=db.backref("test_question", lazy=True))
    answers = db.relationship("Test_question", backref=db.backref("test", lazy=True))

class Test_question(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    test_id = db.Column(db.String(32), ForeignKey("test.id"))
    question_id = db.Column(db.String(32), ForeignKey("question.id"))
    user_choice = db.Column(db.String(32), nullable=True)

    def __repr__(self):
        return self.user_choice


class Question(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    q = db.Column(db.Text, unique=True, nullable=False)
    a = db.Column(db.String(32), nullable=True)

    options = db.relationship("Option", backref=db.backref("question", lazy=True))

    @classmethod
    def dict_q_a(cls):
        return {question.id: question.a for question in cls.query.all()}

    def __repr__(self):
        return f"id:{self.id} - q:{self.q} - a: {self.a}"

class Option(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    o = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.String(32), ForeignKey("question.id"))

    def __repr__(self):
        return f"id:{self.id} - q:{self.o} - a: {self.question_id}"

@tests.route("/", methods=["GET", "POST"])
def query():
    questions = Question.query.all()
    shuffle(questions)
    (shuffle(question.options) for question in questions[0:10])
    res = make_response(render_template("test.html", questions=questions[0:10]))
    return res

@tests.route("/test_question")
def test_question():
    test = Test.query.first()
    print(test.questions)
    print(test.answers)
    # new_test_question = Test_question(id=uuid4().hex, test_id="3441570236a94d3b8d7a7d9409ab6faa", question_id="7447ebc5f9c849459c1fff5f9c628ab4", user_choice="e25e44bb5add4d46ac99ad9556b0f3bd")
    # db.session.add(new_test)
    # db.session.commit()
    return "TEST QUESTIONS"





