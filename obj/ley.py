from os import system
import time

def legend(phrase, d):
    a = ""
    for letter in phrase:
        a += letter
        print(a)
        time.sleep(d)
        system("clear")

legend("The quick brown fox jumps over the lazy dogs", 0.08)
