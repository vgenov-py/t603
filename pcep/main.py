from flask import Flask, session, request, render_template
from uuid import uuid4
from hashlib import sha256
from models import db, User

app = Flask(__name__)
DB_URI = "multitest.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_URI}"
db.init_app(app)

@app.route("/")
def query():
    print(User.query.all())
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)