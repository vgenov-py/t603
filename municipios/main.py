import requests as req
import csv
import json

# url = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json"
# res = req.get(url).json()
# # res = res.decode("utf8", errors="replace") # NOS DEVUELVE UNA STRING

# with open("data_de_internet.json", mode="w", encoding="utf8") as file:  # Escritura del fichero descargado
#     json.dump(res, file, indent=4, ensure_ascii=False)

# def get_by_ine(dataset, ine_code):
#     result = None
#     for mun in dataset[1:]:
#         if mun[2] == ine_code:
#             result = mun
#     return result


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


def to_json(dataset):
# municipio_codigo;municipio_nombre;municipio_codigo_ine;nuts4_codigo;nuts4_nombre;superficie_km2;densidad_por_km2
    result = {"muns":[]}
    dict_keys = dataset[0]
    for mun in dataset[1:]:
        pre_dict = {}
        for i, key in enumerate(dict_keys):
            if i == 5 or i == 6:
                pre_dict[key] = float(mun[i])
            else:
                pre_dict[key] = mun[i]
        result["muns"].append(pre_dict)
    return result



with open("muns.json", mode="w", encoding="utf8") as file:
    data_json =  to_json(data)
    json.dump(data_json, file, indent=4, ensure_ascii=False)







# sup total:
# print(get_sup_total_3(data))

# biggest mun:
# print(get_biggest_mun_2(data))

# print(benford(data))

# 8:




    








