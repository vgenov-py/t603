from flask import render_template, Blueprint
from database import db

users = Blueprint("users", __name__)
#app = Flask(__name__)

class User(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return f"Name: {self.name}"

@users.route("/login")
def login():
    print(User.query.all())
    # new_user = User(id="2", name="Biagio")
    # db.session.add(new_user)
    # db.session.commit()
    return render_template("index.html")

@users.route("/signup")
def signup():
    return "<h1>SIGN UP PAGE</h1>"

@users.route("/all")
def all():
    return "<h1>ALL USERS</h1>"