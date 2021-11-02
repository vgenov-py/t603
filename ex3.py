
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
        print(student["score"])