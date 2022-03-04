from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    pwd = db.Column(db.String(64), nullable=False)
    token = db.Column(db.String(64), nullable=True)
    grades = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"{self.id},{self.email}"

# t_q = db.Table('Test_question',
#     db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True),
#     db.Column('question_id', db.String(32), db.ForeignKey('tag.id'), primary_key=True)
# )

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