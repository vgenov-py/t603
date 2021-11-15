
# dog_1 = ["Kuga", 8, "Chucho", False]
# dog_2 = ["Max", 9, "Doberman", True]
# dog_3 = ["Terrier", 10, "Caniche", True, True, "m"]

# print(dog_2[2])

# dog_1 = {
#     "name": "Kuga",
#     "age": 8,
#     "breed": "Chucho",
#     "chip" : False,
# }

# dog_2 = {
#     "name": "Max",
#     "age": 9,
#     "breed": "Doberman",
#     "chip" : True,
#     "history" : [
#         {
#             "date": "2020/10/10",
#             "total": 150,
#             "observation": True,
#             "meds": ["med_1", "med_2"]
#         }
#     ]
# }

m_course = [{
	"name": "Patricia",
	"id" :  "001",
  "score": 8.1
},
{
	"name": "Nicole",
	"id" :  "002",
  "score": 6.6
},
{
	"name": "Javier",
	"id" :  "003",
  "score": 10
},
{
	"name": "Verónica",
	"id" :  "004",
  "score": 8.6
},
{
	"name": "Guillermo",
	"id" :  "005",
  "score": 4
},
{
	"name": "Pablo",
	"id" :  "006",
  "score": 9
},
{
	"name": "Patricia",
	"id" :  "007",
  "score": 2.3
}
]

a_course =[
{
	"name": "Germán",
	"id" :  "001",
    "score": 6.8
},
{
	"name": "Sara",
	"id" :  "002",
  "score": 8.8
},
{
	"name": "Jorge",
	"id" :  "003",
  "score": 3.3
},
{
	"name": "María",
	"id" :  "004",
  "score": 9.8
},
{
	"name": "Alicia",
	"id" :  "005",
  "score": 5.6
},
{
	"name": "Hernesto",
	"id" :  "006",
    "score": 6.8
}]

student_to_find = "HernEstO"

for student in a_course:
    if student["name"].lower() == student_to_find.lower():
        pass
        # print(student["score"])

count = 0
for student in (m_course + a_course):
    #  dict   | str   |   str |     bool    |
    if student["name"].lower().startswith("p"):
        count += 1

# print(f"Hay {count} estudiantes que empiezan con la letra P")

count = len([student for student in (m_course + a_course) if student["name"].lower().startswith("p")])
# print(count)

courses = m_course + a_course
# print("L118",m_course[-1])

highest_score = 0
student_highest= None

for student in courses:
    if student["score"] > highest_score:
        highest_score = student["score"]
        student_highest = student


# print(student_highest)




# print("L134",courses[-1])

for student in a_course:
    if student["name"].lower() == "alicia":
        student["score"] = 6.7

for student in m_course:
    student["id"] = "M" + student["id"]

for student in a_course:
    student["id"] = "A" + student["id"]

# print("L145",courses[-1])


# print(m_course[-2])
# print(a_course[-2])

suspended = []
approved = []

for student in courses:
    if student["score"] >= 6:
        approved.append(student)
    else:
        suspended.append(student)

user = input("ID: ")

student_i = None
for i, student in enumerate(courses):
    if student["id"] == user:
        for k, v in student.items():
            student_i = i
            student[k] = input(f"Current: {v} - New {k}: ")
        print(student)


print(courses[student_i])


# print([student["id"] for student in suspended])
# print([student["id"] for student in approved])

