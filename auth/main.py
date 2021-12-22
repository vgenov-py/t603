import json
from hashlib import sha256
from models import User, Auth, Admin

'''
some_value + secret + random
'''

DB = "./users.json"

def get_users(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)

fn_users = get_users(DB)

def create_user(data, json_file):
    with open(json_file, "w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


auth = Auth(DB)
user = ""

def get_user():
    user_name = input("Name: ")
    user_pwd = input("PWD: ")
    return User(user_name, user_pwd)


while user != "q":
    print("1. Crear usuario")
    print("2. Log in")
    print("3. Modificar usuario")

    user = input("Choose: ")

    if user == "1":
        user_instance = get_user()
        auth.create_user(user_instance.user_dict)
    
    elif user == "2":
        user_instance = get_user()
        if auth.log_in(user_instance.user_dict):
            print("Te has logueado")
        else:
            print("Mal")

    elif user == "3":
        #@authentication 
        @auth.authentication
        @auth.is_admin   
        def update_user():
            for i, user in enumerate(auth.users["data"]):
                print(f"{i + 1}: {user['name']}")
            user = int(input(": ")) - 1
            new_name = input("Nuevo nombre: ")
            admin_instance = Admin("admin", "1234")
            print("Está seguro de que quiere realizar los cambios?")
            decision = input("(Y/N): ")
            if decision.lower() == "y":
                admin_instance.update_user(auth.users["data"][user]["name"], new_name, auth)
                print("Cambios realizados con éxito")
            else:
                print("No se han realizado los cambios")

    elif user == "4":
        @auth.authentication
        @auth.is_admin
        def print_admin():
            print("Eres admin")


