
import datetime as dt

def outer(f_to_deco): # <-- decorador
    def inner(name):
        return f"{f_to_deco(name)}!"
    return inner


@outer
def greeting(name):
    return f"Hola {name}"


def regards():
    return "Chau"

# print(regards())




def log(f):
    def i(*args):
        with open("./calls.log", "a", encoding="utf8") as file:
            file.write(f"{dt.datetime.now()}| {f.__name__}\n")
        return f(*args)
    return i

@log
def add(a, b):
    return a + b

class Daniel:
    def __init__(self, name):
        self.name = name

def substract(a, b):
    return a - b

@log
def greeting():
    return "Hola"

print(add(1,2))
print(substract(1,2))

print(greeting())