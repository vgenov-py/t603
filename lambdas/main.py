import math

def saludar(name):
    return f"Hola {name}!"

# print(saludar)
lambda name: f"Hola {name}!"


calculator = {
    "add": lambda a,b: a + b,
    "substract": lambda a,b: a - b,
    "square": "lambda que obtine cuadrado",
    "cube":"lambda que obtiene cubo",
    "pi": 3.141592653589793
}


# result = []
# for num in a:
#     first = num**2
#     second = first**3
#     result.append(second)

a = [1,2,3,4]
# def square(num):
#     return num ** 2

# squares = map(lambda num: num**2, a)
# squares = list(map(square, a))
# print(squares)

# result = []
# for num in a:
#     if num % 2 == 0:
#         result.append(num)

# result = [num for num in a if num %2 == 0]

# evens = list(filter(lambda num: num %2 == 0,a))
# print(evens)

# lista = ["Marcelo", "Pedro", "German", "Alicia", "María", "Eusebio", "Rolando"] # Que empiecen con la letra M
# lista_m = ["Marcelo", "Maria"]

a = [1,2,3,4]
b = [5,6,7,8]

result = list(map(lambda num_a,num_b, num_c: num_a * num_b * num_c,a,b,[1,2,3,4]))
print(result)








