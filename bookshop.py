DB = [{ # Esto ha sido blah nano
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficción"
},
{
    "id": "ne_1",
    "title": "Lobo de mar",
    "author": "Jack London",
    "genre": "Narrativa extranjera"
},
{
    "id": "np_1",
    "title": "El legado de los huesos",
    "author": "Dolores Redondo",
    "genre": "Narrativa policíaca"
},
{
    "id": "dc_1",
    "title": "El error de Descartes",
    "author": "Antonio Damasio",
    "genre": "Divulgación científica"
},
{
    "id": "dc_2",
    "title": "El ingenio de los pájaros",
    "author": "Jennifer Ackerman",
    "genre": "Divulgación científica"
},
{
    "id": "ne_4",
    "title": "El corazón de las tinieblas",
    "author": "Joseph Conrad",
    "genre": "Narrativa extranjera"
},
{
    "id": "dc_5",
    "title": "Metro 2033",
    "author": "Dmitri Glujovski",
    "genre": "Divulgación científica"
},
{
    "id": "dc_6",
    "title": "Sidharta",
    "author": "Hermann Hesse",
    "genre": "Narrativa extranjera"
},
{
    "id": "el_1",
    "title": "Andres Trapiello",
    "author": "Las armas y las letras",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera"
},
]

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

while user != "q":
    menu()
    user = input(": ")
    if user == "1":
        user = input("ISBN: ")
        book_found = look_for_id(user)
        if book_found:
            pretty_book(book_found)
        else:
            print(f"No encontramos el libro con el ISBN: {user}")
        input()
    elif user == "4":
        for i, genre in enumerate(genres):
            print(f"{i + 1}. {genre}")

        user = int(input("Género: ")) -1
        user = genres[user]
        books = get_by_term("genre", user)
        for i, book in enumerate(books):
            pretty_book(book)
            print("-"*30)
            if i % 2 == 0:
                input("Siguiente: ")
        input()

    elif user == "5":
        user = input("Buscar libro a modificar por ID: ")
        book_to_update = look_for_id(user)
        if book_to_update:
            update_book(book_to_update)
        print(DB)


