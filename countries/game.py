import random

import requests as req

res = req.get("https://restcountries.com/v3.1/region/europe").json()

countries = list(map(lambda country: {
    "name": country["name"]["common"],
    "capital": country["capital"][0],
    "population": country["population"],
    "area":country["area"]},
  res))

def make_quiz(countries, region):
    by_area = sorted(countries, key=lambda country: country["area"])
    biggest, smallest = by_area[-1], by_area[0]
    
    quiz = [
        {
            "q": f"Cuántos países hay en {region}?",
            "a": f"{len(countries)}",
            "o": [
                len(countries) +7,
                len(countries),
                len(countries) -11
            ]
        },
        {
            "q": f"Cuál es el país más grande de {region}?",
            "a": f"{biggest['name']}",
            "o": [
                by_area[-1]['name'],
                by_area[6]['name'],
                by_area[-2]['name'],
            ]
        },
        {
            "q": f"Cuál es el país más chico de {region}?",
            "a": f"{smallest['name']}",
            "o": [
                by_area[0]['name'],
                by_area[-6]['name'],
                by_area[7]['name'],
            ]
        }
    ]
    return quiz
quiz = make_quiz(countries, "europa")
print(quiz)

# cual es la capital de malasya

# for country in countries:
#     if country["name"] == "Malasya":
#         return country["capital"]

# list(filter(lambda country: country["name"] == name, countries))[0]["capital"]
