from os import system
import time

def legend(phrase):
    a = ""
    for letter in phrase:
        a += letter
        print(a)
        time.sleep(0.05)
        system("clear")

