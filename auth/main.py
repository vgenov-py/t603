import json


DB = "./users.json"

def get_users(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)

def create_user(data, json_file):
    with open(json_file, "w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

class Auth:
    def __init__(self, user, db):
        self.user = user
        self.db = db

    @property
    def users(self):
        with open(self.db, encoding="utf8") as file:
            return json.load(file)


    def create_user(self):
        data = self.users
        data["data"].append({"name":self.user.name, "pwd":self.user.pwd})
        with open(self.db, "w", encoding="utf8") as file:
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