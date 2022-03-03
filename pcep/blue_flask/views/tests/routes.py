from flask import render_template, Blueprint

tests = Blueprint("tests", __name__)

@tests.route("/test")
def test():
    return "<h1>TEST PAGE</h1>"

@tests.route("/all")
def all():
    return "<h1>ALL TESTS</h1>"
