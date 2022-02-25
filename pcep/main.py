from click import option
from flask import Flask, make_response, session, request, render_template, Response
from uuid import uuid4
from hashlib import sha256
from models import db, User, Question, Option

app = Flask(__name__)
DB_URI = "multitest.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_URI}"
db.init_app(app)


@app.route("/")
def query():
    question = Question.query.first()
    print(Option.query.filter_by(question_id = question.id).all() == question.options)


    # db.session.commit()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)