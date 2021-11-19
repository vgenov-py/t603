import requests as req

# location = input("Ciudad: ")
# res = req.get(f"https://www.metaweather.com/api/location/search/?query={location}").json()
# woeid = res[0]["woeid"]
# res = req.get(f"https://www.metaweather.com/api/location/{woeid}/").json()
# print(f"La temperatura de {location} es: ",res["consolidated_weather"][0]["the_temp"])

user = 2

def menu():
    print("Real weather".center(50, "-"))
    print("1. Buscar por ciudad".center(50, "-"))
    print("2. Buscar por coordenadas".center(50, "-"))
    print("3. Buscar por ciudad/coordenadas y fecha".center(50, "-"))
    print("Q. Para salir".center(50, "-"))

def forecast(location):
    woeid = req.get(f"https://www.metaweather.com/api/location/search/?query={location}").json()[0]["woeid"]
    forecast = req.get(f"https://www.metaweather.com/api/location/{woeid}/").json()["consolidated_weather"][0]["the_temp"]
    return forecast

while user != "q":
    menu()
    user = input("Opción: ")
    if user == "1":
        location = input("Ciudad: ")
        forecast_search = forecast(location)
        print(f"La sensación térmica para {location} es {forecast_search}")
        input("")
