
a = [2,2,3,4]

'''
Create
Read
Update
Delete

pass, break, continue
'''
# Create:

a.append(6)
a.insert(4, 5)

# Read:
# print(a)
# print(a[4])

# Update:

a[0] = 1

# Delete:
a.pop(0)
# print(a)
a.clear()

# print(a)



a = [1,2,3,4,5,6,7, 2, 5]
# método index:
i = 0
num_to_search = 2
while i < len(a):
    if num_to_search == a[i]:
        # print(i)
        i = len(a)
    i += 1

# método count:
i = 0
num_to_count = 10
count = 0

while i < len(a):
    if num_to_count == a[i]:
        count += 1
    i += 1

# print(f"El número {num_to_count} aparece {count} vez/es")

# a = [1,2,3,4]
# i = 0

# num_to_search = 2
# for num in a:
#     if num_to_search == num:
#         pass
#     i += 1

# count = 0
# num_to_count = 2

# for num in a:
#     if num_to_count == num:
#         count += 1
# print(count)

repeated_numbers = [1,2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98]
# result = set(repeated_numbers)
# print(result)



# for num in repeated_numbers:
#     if repeated_numbers.count(num) == 1:
#         result.append(num)
#     else:
#         if result.count(num) == 0:
#             result.append(num)

# print(result)

# b = (4,2,3,1)
# b_ordenada = sorted(b)
# print(type(b_ordenada))
# print("B ORIGINAL: ", b)




# Ejericio 5:
a = [5,41,3,1,3,2]

# [ __(1) for __(2) in __(3) ] 1 == 2 y 3 es de dónde sacamos 1 y 2
#
# squares = [num ** 2 for num in a]
# print(squares)

# for num in a:
#     squares.append(num ** 2)

# Ejercicio 6:
# 
# mean = sum(a)/len(a)

# Sumatoria de los números de lista A al cuadrado
# sorted([num ** 2 for num in a])
# print(sum([num ** 2 for num in a]))

# Ejercicio 7:

# a[a.index(max(a))] = 1000
# print(a)

## Conseguir max sin función max:

# max_num = 0

# for num in a:
#     if num > max_num:
#         max_num = num

# a[a.index(max_num)] = 1000

# a[a.index(sorted(a)[-1])] = 1000
# print(a)


a = [1,2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98]

# sumatoria_4_10_num = 0
# sumatoria_4_10_list = []

# for i, num in enumerate(a):
#     if i >= 4 and i<=10:
#         sumatoria_4_10_num += num
#         sumatoria_4_10_list.append(num)

# print(sumatoria_4_10_num == sum(sumatoria_4_10_list))

# sumatoria_4_10_list = sum([num for i, num in enumerate(a) if i >= 4 and i<=10])
# print(sumatoria_4_10_list)

sumatoria_4_10_list = sum([num for num in a[4:10]])




result = [1,1]
limit = 15

for _ in range(0, limit):
    result.append(result[-2] + result[-1])


dog_1 = ["Kuga", 8, "Chucho", False]
dog_2 = ["Max", 9, "Doberman", True]
dog_3 = ["Terrier", 10, "Caniche", True, True, "m"]

print(dog_2[2])

dog_1 = {
    "name": "Kuga",
    "age": 8,
    "breed": "Chucho",
    "chip" : False,
}

dog_2 = {
    "name": "Max",
    "age": 9,
    "breed": "Doberman",
    "chip" : True,
    "history" : [
        {
            "date": "2020/10/10",
            "total": 150,
            "observation": True,
            "meds": ["med_1", "med_2"]
        }
    ]
}

#type: dict|  list   |dict | list | str





