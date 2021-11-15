import csv

with open("./users.csv", mode="a+", newline="", encoding="utf8") as file:
    students = [
        ["005", "Juan", "Vilarrubia"],
        ["006", "Daniel", "Ballesteros"],
        ["007", "Dannel", "apellido"]
    ]
    csv_reader = csv.reader(file, delimiter=";")
    # file.seek(-1)
    # next(csv_reader)
    for i, row in enumerate(csv_reader):
        print(row)
    # WRITE:
    csv_writer = csv.writer(file, delimiter=";")
    csv_writer.writerow(["005", "Maria", "Perez"])
    

with open("./users.txt", mode="r") as file:
    data = file.read()
    # print(data)