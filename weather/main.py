from os import write
import requests as req
import json

def menu():
    print("Real weather".center(50, "-"))
    print("1. Buscar por ciudad".center(50, "-"))
    print("2. Buscar por coordenadas".center(50, "-"))
    print("3. Buscar por ciudad/coordenadas y fecha".center(50, "-"))
    print("Q. Para salir".center(50, "-"))

 
# 40.234, -3.554
'''

    La descripción del clima (soleado, nuboso y lluvioso)
    La máxima
    La mínima
    Sensación térmica
    Humedad
    Velocidad del viento y dirección

'''


def get_data(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)

def write_data(data, json_file):
    with open(json_file, mode="w",encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


woeids = get_data("woeids.json")

def pretty_print(forecast):
    for k, v in forecast.items():
        print(f"{k.upper()}: {v}")



# date=2014/10/10
def forecast(location, **kwargs):
    if kwargs.get("coordinates"): 
        woeid = req.get(f"https://www.metaweather.com/api/location/search/?lattlong={location}").json()[0]["woeid"]
        forecast = req.get(f"https://www.metaweather.com/api/location/{woeid}/").json()["consolidated_weather"][0]
    else:
        woeid = woeids.get(location.lower())
        if not woeid:
            print("We didn't find woeid!")
            try:
                woeid = req.get(f"https://www.metaweather.com/api/location/search/?query={location}").json()[0]["woeid"]
            except IndexError:
                return None
            woeids[location] = woeid
            write_data(woeids, "woeids.json")
        forecast = req.get(f"https://www.metaweather.com/api/location/{woeid}/").json()["consolidated_weather"][0]
    forecast = {
        "desc": forecast["weather_state_name"],
        "max_temp": forecast["max_temp"],
        "min_temp": forecast["min_temp"],
        "st": forecast["the_temp"],
        "humidity": forecast["humidity"],
        "wind_speed_direction": f"{forecast['wind_speed']} | {forecast['wind_direction_compass']}" 
    }
    return forecast

def forecast_v_2(location, **kwargs): # ciudad/coords - date on - date off
    term = "query"
    woeid = woeids.get(location.lower())
    if not woeid:
        if kwargs.get("coords"):
            term = "lattlong"

        url = f"https://www.metaweather.com/api/location/search/?{term}={location}"
        woeid = req.get(url).json()
        if len(woeid) >= 1:
            for loc in woeid:
                woeids[loc["title"].lower()] = loc["woeid"]
            woeid = woeid[0]["woeid"]
            write_data(woeids, "woeids.json")
        else:
            return None

    # A partir de aquí podemos buscar por woeid:
    '''
    generar la url de llamada en base al woeid obtenido en el código anterior --> url = "weather..."
    '''
    url = f"https://www.metaweather.com/api/location/{woeid}/"
    date = kwargs.get("date")
    if date:
        url += date
    forecast = req.get(url).json()
    if type(forecast) == list: 
        forecast = forecast[0]
        if not len(forecast):
            return None
    forecast = forecast["consolidated_weather"][0]

    forecast = {
        "desc": forecast["weather_state_name"],
        "max_temp": forecast["max_temp"],
        "min_temp": forecast["min_temp"],
        "st": forecast["the_temp"],
        "humidity": forecast["humidity"],
        "wind_speed_direction": f"{forecast['wind_speed']} | {forecast['wind_direction_compass']}" 
    }

    return forecast

        

# forecast_v_2("kirkwall", date="2020/10/10")




user = "0"
while user != "q":
    menu()
    user = input("Opción: ")
    if user == "1":
        city = input("Ciudad: ")
        forecast_search = forecast_v_2(city)
        if forecast_search:
            print(f"La sensación térmica para {city}:")
            pretty_print(forecast_search)
        else:
            print(f"No hay pronóstico disponible para la localización: {city}")
        input("...")
    elif user == "2":
        lattlong = input("Coordenadas (latt, long): ")
        forecast_search = forecast_v_2(lattlong, coords=True)
        print(f"La sensación térmica:")
        pretty_print(forecast_search)
        input("...")

