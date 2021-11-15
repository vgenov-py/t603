from bookshop import *

user = "0"

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