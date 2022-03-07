# @tests.route("/create")
# def create_qs():
#     def get_data():
#         with open("pcep.json") as file:
#             return json.load(file)
#     qs = get_data()
#     for block in list(qs.values())[1:]:
#         for question in block:
#             q_id = uuid4().hex
#             for i, option in enumerate(question["options"]):
#                 o_id = uuid4().hex
#                 if i == question["answer"]:
#                     a = o_id
#                 option = Option(id=o_id, o=option, question_id=q_id)
#                 db.session.add(option)
                
#             question = Question(id=q_id, q=question["question"], a=a)
#             db.session.add(question)
#             # db.session.commit()
#     return "create"