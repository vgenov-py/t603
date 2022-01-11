
import concurrent.futures
import requests as req
import time

url_1 = "https://flagcdn.com/w320/ng.png"

def get_flag(url):
    res = req.get(url).content
    with open(f"flags/{url[-6:]}", "wb") as file:
        file.write(res)

# all_countries = "https://restcountries.com/v3.1/all"
url_flags = [country["flags"]["png"] for country in req.get("https://restcountries.com/v3.1/all").json()]

start = time.perf_counter()

# Threadpoolexecutor permite guardar los valores en variables, tiene un método map disponible y al momento de utilizar submit arrancamos el proceso 

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(get_flag, url_flags)
    # future_1 = executor.submit(get_flag, url_1)
    # data = future_1.result()

finish = time.perf_counter()
print(finish- start)
