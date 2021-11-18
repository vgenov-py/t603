import json


# with open("./data.json", encoding="utf8") as file:
#     data_str = file.read()
#     data_json = json.loads(data_str)
#     print(type(data_json))


a = '''{
    "students" : [
        {
            "name":"Vito",
            "age": 10,
            "is_adult": false,
            "pays": null
        },
        {
            "name":"Marcelo",
            "age": 20,
            "is_adult": true,
            "pays": null
        }
    ],
    "teachers" : [
        {
            "name": "Pedro",
            "age": 25,
            "is_adult": true,
            "pays": null
        }
    ]
}
'''

b = json.loads(a)

c = json.dumps(b)
print(type(c))