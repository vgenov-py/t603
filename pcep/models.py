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

class Question(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    q = db.Column(db.Text, unique=True, nullable=False)
    a = db.Column(db.String(32), nullable=True)

    options = db.relationship("Option", backref=db.backref("question", lazy=True))

    # @property Igual a option de arriba
    # def options(self):
    #     return Option.query.filter_by(question_id=self.id).all()

    def __repr__(self):
       return f"{self.q}"

class Option(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    o = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.String(32), ForeignKey("question.id"))

    def __repr__(self):
       return f"{self.o}"