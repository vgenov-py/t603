import json
from hashlib import sha256

class User:
    def __init__(self, name, pwd):
        self.name = name
        pwd_e = sha256(pwd.encode()).hexdigest()
        self.pwd = pwd_e

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