import json
from hashlib import sha256
from models import User, Auth

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
    print("3. Restricted Area")

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
        def restricted_menu():
            print("Estás en una zona restringida")

