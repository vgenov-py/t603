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
result = set(repeated_numbers)
print(result)

# for num in repeated_numbers:
#     if repeated_numbers.count(num) == 1:
#         result.append(num)
#     else:
#         if result.count(num) == 0:
#             result.append(num)

# print(result)




