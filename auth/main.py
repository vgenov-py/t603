import json
from hashlib import sha256
from models import User, Auth


DB = "./users.json"

def get_users(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)

def create_user(data, json_file):
    with open(json_file, "w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


    
user = ""
while user != "q":
    print("1. Crear usuario")
    print("2. Log in")
    user = input("Choose: ")
    # if user == "1": # Function style
    #     user_name = input("Name: ")
    #     user_pwd = input("PWD: ")
    #     users = get_users(DB)
    #     users["data"].append({"name": user_name, "pwd": user_pwd})
    #     create_user(users, DB)
    if user == "1":
        user_name = input("Name: ")
        user_pwd = input("PWD: ")
        user_instance = User(user_name, user_pwd)
        auth = Auth(user_instance, DB)
        auth.create_user()