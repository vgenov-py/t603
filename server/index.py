import requests as req

base_url = "http://localhost:5000"

data = req.get(base_url+"/all").json()

user = ""

while user != "q":
    print("1. Consultar libro por ID")
    print("2. Modificar libro")
    print("3. TEST")
    user = input(": ")
    if user == "1":
        book_id = input("ID del libro: ")
        book = req.get(f"{base_url}/book/{book_id}").json()
        if book:
            print(book["book"])
        else:
            print("No hemos encontrado el libro")

    elif user == "3":
        print(req.post(f"{base_url}/test", data={"name":"Vito", "n":8}).json())