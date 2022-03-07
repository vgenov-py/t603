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
