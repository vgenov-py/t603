a = 2
import requests as req

# if a % 2 == 0:
#     print(a, " es par")
# else:
#     print(a, " es impar")

# age = 25

# is_adult = True if age >= 18 else False

# manolitos = 13

# box = "caja_grande" if manolitos >= 12 else "caja_chica" if manolitos >= 6 else "bolsa_de_papel"
# # print(box)



# a = [1,2,3,4]

# a_even = [num if num % 2 == 0 else None for num in a]
# for num in a_even:
#     if num:
#         print(num)

# pwd = "secreto"

# pwd_user = input("pwd: ")

# is_allowed = True if pwd_user == pwd else False
# if is_allowed:
#     print("contraseña correcta")

url = "https://restcountries.com/v3.1/region/europe"
all = req.get(url).json()

# countries_p = []
# for country in all:
#     if country["name"]["common"].lower().startswith("p"):
#             countries_p.append(country)

countries_p = list(filter(lambda country: country["name"]["common"].lower().startswith("p"), all))

countries_p = list(map(lambda country: country if country["name"]["common"].lower().startswith("p") else None, all))
# print(countries_p[0])
countries_p = [country for country in countries_p if country]
# print(countries_p[1]["name"]["common"])

# highest_area = 0
# biggest_c = None
# for c in all:
#     if c["area"] >= highest_area:
#         highest_area = c["area"]
#         biggest_c = c["name"]["common"]
# print(biggest_c)

# by_area = sorted(all, reverse=True, key=lambda country: country["capital"][0])
# print(by_area[0]["capital"][0], by_area[-1]["area"])

students = [
    {"name": "Vito", "age": 27},
    {"name": "Jorge", "age": 22},
    {"name": "Pedro", "age": 30},
]

print(sorted(students, key= lambda student: student["name"]))