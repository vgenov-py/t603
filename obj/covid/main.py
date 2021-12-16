import json
from std import Std
# import requests as req
import os

cwd = os.path.dirname(__file__)
# url = "https://datos.comunidad.madrid/catalogo/dataset/b3d55e40-8263-4c0b-827d-2bb23b5e7bab/resource/907a2df0-2334-4ca7-aed6-0fa199c893ad/download/covid19_tia_zonas_basicas_salud_s.json"
# res = req.get(url).json()
# with open(f"{cwd}/covid.json", "w",encoding="utf8") as file:
#         json.dump(res, file, ensure_ascii=False, indent=4)

def get_data(file):
    with open(f"{cwd}/{file}", encoding="utf8") as file:
        return json.load(file)

data = get_data("covid.json")["data"]

last_date = data[0]["fecha_informe"].split(" ")[0].replace("/", "-")

def data_by_date(dataset):
    result = {}
    for zone in dataset:
        idate = zone["fecha_informe"].split(" ")[0]
        if result.get(idate):
            result[idate].append(zone)
        else:
            result[idate] = [zone]
    return result

data_by_date = data_by_date(data)
def get_y(dataset):
    result = []
    for zone_list in dataset.values():
        result.append(sum(zone["casos_confirmados_totales"] for zone in zone_list))
    return result

y = get_y(data_by_date)

y.reverse()
x = [num for num in range(0, len(y))]

analyze_cct = Std(x, y)


# def get_y_line(std_object):
#     B = std_object.B
#     result = [B]
#     for _ in range(1, len(std_object.y)):
#         result.append(B + result[-1])
#     return result

# def get_y_line_2(std_object):
#     result = []
#     for week in std_object.x:
#         result.append(std_object.y_prediction(week))
#     return result
#     return [std_object.y_prediction(week) for week in std_object.x]

# print(analyze_cct.get_prediction_day(last_date, "2021-12-31"))

# plt.plot(analyze_cct.x,analyze_cct.y, analyze_cct.x, analyze_cct.lineals)
# plt.ylabel("Casos confirmados")
# plt.xlabel("Semanas")
# plt.show()


def get_tia(dataset, date):
    return tuple(zone["tasa_incidencia_acumulada_ultimos_14dias"] for zone in dataset if zone["fecha_informe"].split(" ")[0] == date)
    result = []
    for zone in dataset:
        if zone["fecha_informe"] == date:
            result.append(zone["tasa_incidencia_acumulada_ultimos_14dias"])
    return result


list_y_tia_20211214 = tuple(zone["tasa_incidencia_acumulada_ultimos_14dias"] for zone in data_by_date["2021/12/14"])
list_y_tia_20201215 = tuple(zone["tasa_incidencia_acumulada_ultimos_14dias"] for zone in data_by_date["2020/12/15"])
list_x_tia = tuple(num for num in range(0, len(list_y_tia_20201215)))

std_tia_20211214 = Std(list_x_tia, list_y_tia_20211214)
std_tia_20201215 = Std(list_x_tia, list_y_tia_20201215)

# print(std_tia_20211214.y_avg)
# print(std_tia_20201215.y_avg)
# print(std_tia_20211214.y_quasi_variance)
# print(std_tia_20211214.y_variance)

def ec_student(std_1, std_2):
    nu = std_1.y_avg -std_2.y_avg
    de_1 = ((std_1.n -1) * std_1.y_quasi_variance) + ((std_2.n -1) * std_2.y_quasi_variance)
    de_2 = std_1.n + std_2.n - 2
    de_3 = (1/std_1.n) +  (1/std_2.n)
    de = ((de_1 / de_2) * de_3)**0.5
    return nu/de
print(ec_student(std_tia_20211214, std_tia_20201215))