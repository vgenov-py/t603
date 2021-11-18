import requests as req
import csv

# url = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/ee750429-1e05-411a-b026-a57ea452a34a/download/municipio_comunidad_madrid.csv"
# res = req.get(url).content
# res = res.decode("utf8", errors="replace") # NOS DEVUELVE UNA STRING

# with open("data.csv", mode="w", encoding="utf8") as file:  # Escritura del fichero descargado
#     file.write(res)

def get_by_ine(dataset, ine_code):
    result = None
    for mun in dataset[1:]:
        if mun[2] == ine_code:
            result = mun
    return result


# 3. Obtener superficie total:

def get_sup_total(dataset):
    counter = 0
    for i, mun in enumerate( dataset[1:]):
        counter = counter + float(mun[-2])
    return counter
        
def get_sup_total_2(dataset):
    result = []
    for mun in dataset[1:]:
        result.append(float(mun[-2]))
    return sum(result)

def get_sup_total_3(dataset):
    result = [float(mun[-2]) for mun in dataset[1:]]
    return sum(result)
    # return sum([float(mun[-2]) for mun in dataset])

def get_biggest_mun(dataset):
    big_mun = None
    sup_to_beat = 0
    for mun in dataset[1:]:
        if float(mun[-2]) > sup_to_beat:
            big_mun = mun
            sup_to_beat = float(mun[-2])
    return big_mun

def get_biggest_mun_2(dataset):
    max_sup = max([float(mun[-2]) for mun in dataset[1:]])
    for mun in dataset[1:]:
        if float(mun[-2]) == max_sup:
            return mun

def benford(dataset):
    densities = [mun[-2] for mun in dataset[1:]]
    result = {}
    for num in range(1,10):
        result[str(num)] = 0
    print(result)
    for density in densities:
        result[density[0]] += 1/len(densities)
    
    for k,v in result.items():
        print(f"{k}: {v}")
        
with open("./data.csv", mode="r", encoding="utf8") as file:
    data = list(csv.reader(file,delimiter=";"))

# sup total:
# print(get_sup_total_3(data))

# biggest mun:
# print(get_biggest_mun_2(data))

# print(benford(data))









    








