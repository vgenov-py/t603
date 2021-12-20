import json
from hashlib import sha256

class User:
    def __init__(self, name, pwd):
        self.name = name
        pwd_e = sha256(pwd.encode()).hexdigest()
        self.pwd = pwd_e
    
    @property
    def user_dict(self):
        return {
            "name": self.name,
            "pwd":self.pwd
        }

class Auth:
    def __init__(self, db):
        self.db = db

    @property
    def users(self):
        with open(self.db, encoding="utf8") as file:
            return json.load(file)

    def create_user(self, user):
        users = self.users
        users["data"].append(user)
        with open(self.db, "w",encoding="utf8") as file:
            json.dump(users, file, ensure_ascii=False, indent=4)
        
    def log_in(self, user):
        db_user = next(filter(lambda db_user: db_user["name"] == user["name"], self.users["data"]), False)
        if db_user:
            return True if db_user["pwd"] == user["pwd"] else False
        else:
            return False