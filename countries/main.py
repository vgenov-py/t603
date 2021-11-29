import requests as req
import os

CWD = os.path.dirname(__file__)

url = "https://restcountries.com/v3.1/asll"

user = ""

def make_quiz(countries, region):
    countries = list(map(lambda country: {
        "name": country["name"]["common"],
    "capital": country["capital"][0],
    "population": country["population"],
    "area":country["area"]},
    res))
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

while user != "q":
    print("1. Buscar país")
    print("2. Descargar bandera")
    print("3. Jugar al cuestionario")
    print("Q. Salir")
    user = input(": ")
    if user == "1":
        country_name = input("País: ")
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        res = req.get(url)
        if res.status_code == 200:
            res = res.json()[0]
            country_lang = list(res["languages"].values())[0]
            print(f'Capital: {res["capital"][0]}')
            print(f'Población: {res["population"]}')
            print(f'Superficie: {res["area"]}')
            print(f'Lenguaje: {country_lang}')
            input("...")
        else:
            print("Something go wrong")

    elif user == "2":
        country_name = input("País: ")
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        res = req.get(url)
        if res.status_code == 200:
            country = res.json()[0]
            flag_url = country["flags"]["svg"]
            flag = req.get(flag_url)
            if flag.status_code == 200:
                with open(f"{CWD}/img/{flag_url[-6:]}", "wb") as file:
                    file.write(flag.content)
    elif user == "3":
        region = input("continente: ")
        res = req.get(f"https://restcountries.com/v3.1/region/{region}").json()
        quiz = make_quiz(res, region)
        user_a = []
        for q in quiz:
            print(q["q"])
            answer = input(": ")
            q["user"] = answer
            user_a.append({q["q"]: answer})
        print(quiz)
        print(user_a)            
        
