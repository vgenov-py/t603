from flask import Flask
from views.users.routes import users
from views.tests.routes import tests
from database import db
import os

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Some secret key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
    app.register_blueprint(users)
    app.register_blueprint(tests, url_prefix="/tests")
    db.init_app(app)
    return app

def set_db(app):
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app = create_app()
    if not os.path.isfile("db.db"):
        set_db(app)
    app.run(debug=True)