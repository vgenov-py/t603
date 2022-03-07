import uuid
from venv import create
from flask import Flask, make_response, session, request, render_template, Response
from uuid import uuid4
from hashlib import sha256

from models import db
from views.tests.routes import tests
from views.api.routes import api

import json
from random import shuffle
DB_URI = "multitest.db"



def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_URI}"
    app.register_blueprint(tests)
    app.register_blueprint(api, url_prefix="/api")

    db.init_app(app)    
    return app



def set_db(app):
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)