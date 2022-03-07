from flask import Blueprint, request
from models import db
from sqlalchemy import ForeignKey
from uuid import uuid4
from random import shuffle
from views.tests.routes import Question

api = Blueprint("api", __name__)

@api.route("/grade", methods=["GET", "POST"])
def coo():
    if request.method == "POST":
        q_a = Question.dict_q_a() # q_id q a "q_id": "q_a"
        
        answers = request.get_json()
        result = {"grade": 0, "answers":{}}
        for answer in answers:
            result["answers"][answer[1]] = False
            if q_a[answer[0]] == answer[1]:
                result["grade"] += 1
                result["answers"][answer[1]] = True

            
    return result

