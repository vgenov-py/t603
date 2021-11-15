# fichero = open("./lectura/test.txt")

# lectura = fichero.read()


# # Análisis del fichero:

# mama = lectura[(lectura.find("mamá")):]
# print(mama)

# fichero.close()

with open("./test.txt", mode="r") as file:
    a = file.read()
    print(a)
    # for i in range(1,11):
    #     file.write(f"{i}\n")