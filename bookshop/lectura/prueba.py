from os import path

cwd = path.dirname(__file__)

with open(f"{cwd}/record.txt", mode="a") as file:
    file.writelines(["a", "b", "c", "d"])
