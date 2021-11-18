import csv

DB = []

genres = ["Narrativa extranjera", "Divulgación científica", "Narrativa policíaca", "Ciencia ficción", "Autoayuda"]

user = "0"

def menu():
    print("Libería".center(50, "#"))
    print("# 1. Buscar por ISBN" + (" "* (49 - len("# 1. Buscar por ISBN"))) + "#")
    print("# 2. Buscar por Autor"+ (" "* (49 - len("# 2. Buscar por Autor"))) + "#")
    print("# 3. Buscar por Título"+ (" "* (49 - len("# 3. Buscar por Título"))) + "#")
    print("# 4. Buscar por Género"+ (" "* (49 - len("# 4. Buscar por Género"))) + "#")
    print("# 5. Actualizar registro"+ (" "* (49 - len("# 5. Actualizar registro"))) + "#")

    print("# Q. Terminar programa"+ (" "* (49 - len("# Q. Terminar programa"))) + "#")
    print("#"*50)

def look_for_id(user_isbn):
    for book in DB:
        if book["id"] == user_isbn:
            return book
    return None

def pretty_book(book):
    for k,v in book.items():
        print(f"{k}: {v}")

def get_by_term(term, search_term):
    result = []
    for book in DB:
        if book[term] == search_term:
            result.append(book)
    return result

def update_book(book):
    print("Si no desea modificar de a Enter")
    for k,v in list(book.items())[1:]:
        user = input(f"{k}: ")
        if user:
            book[k] = user

def read_csv(dataset, file_name):
    with open(file_name, mode="r", encoding="utf8") as file:
        csv_reader = csv.reader(file, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            new_dict = {
                "id": row[0],
                "author": row[1],
                "title": row[2],
                "genre": row[3]
            }
            DB.append(new_dict)

read_csv(DB, "books.csv")



def export_csv(dataset, file_name):
    with open(file_name, mode="w", encoding="utf8") as file:
        csv_writer = csv.writer(file, delimiter=";")
        csv_writer.writerow(["id", "author", "title", "genre"])
        for entry in dataset:
            csv_writer.writerow(entry.values())

