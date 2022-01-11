import time
import threading
import requests as req
from requests.api import get
print("Empieza el programa")


# def get_data(data):
#     time.sleep(1)
#     return f"Se ha descargado la data de {data}"



# thread_1 = threading.Thread(target=get_data, args=["REST countries 1"])
# thread_2 = threading.Thread(target=get_data, args=["REST countries 2"])
# thread_3 = threading.Thread(target=get_data, args=["REST countries 3"])
# thread_4 = threading.Thread(target=get_data, args=["REST countries 4"])
# thread_1.start()
# thread_2.start()
# thread_3.start()
# thread_4.start()
# thread_1.join()
# thread_2.join()
# thread_3.join()
# thread_4.join()


url_1 = "https://flagcdn.com/w320/ng.png"
url_2 = "https://flagcdn.com/w320/uy.png"

url_flags = [country["flags"]["png"] for country in req.get("https://restcountries.com/v3.1/all").json()]

start_1 = time.perf_counter()

def get_flag(n_folder,url):
    res = req.get(url).content
    with open(f"flags_{n_folder}/{url[-6:]}", "wb") as file:
        file.write(res)

for url in url_flags:
    threading.Thread(target=get_flag, args=["1", url]).start()
    

finish_1 = time.perf_counter()

print(f"Threading: {finish_1 - start_1}")

# start_2 = time.perf_counter()
# for url in url_flags:
#     get_flag("2", url)

# finish_2 = time.perf_counter()
# print(f"Sync: {finish_2 - start_2}")
