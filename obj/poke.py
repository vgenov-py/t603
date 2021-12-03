import time 
from os import system
from random import choice
from ley import legend

elements = ["fire", "water", "grass"]




class Pokemon:
    # propiedades de la clase:
    counter = 0

    def __init__(self, name, element, HP):
        self.name = name
        self.element = element
        self.HP = [HP,HP]
        self.attacks = []
        self.is_alive = True
        Pokemon.counter += 1
    
    def learn(self, attack):
        self.attacks.append(attack)
    
    def receive_damage(self, attack):
        
        self.element, attack.element
        is_weakness = True
        weakness = True if is_weakness else False
        self.HP[0] -= attack.damage * 1.5 if weakness else attack.damage
        self.is_alive = True if self.HP[0] >= 0 else False
        return attack
        

    def __str__(self):
        return f'''Pokemon({self.name},{self.element},{self.HP})'''

class Attack:
    def __init__(self, name, element, damage):
        self.name = name
        self.element = element
        self.damage = damage
    
    def __repr__(self):
        return f'''Attack({self.name},{self.element},{self.damage})'''

# Pokemons instances:

charmander = Pokemon("Charmander", elements[0], 100.0)
squirtle = Pokemon("Squirtle", elements[1], 110.0)
pokemons = [charmander, squirtle]

# Attacks instances:

flamethrower = Attack("Flamethrower", elements[0], 25)
water_gun = Attack("Tackle", elements[1], 20)
razor_leaf = Attack("Razor leaf", elements[2], 20)


charmander.learn(flamethrower)
charmander.learn(water_gun)
charmander.learn(razor_leaf)
squirtle.learn(flamethrower)
squirtle.learn(water_gun)
squirtle.learn(razor_leaf)

def list_values(dataset):

    for i, value in enumerate(dataset):
        print(f"{i + 1}: {value}")
    i_selected = int(input(": "))
    return i_selected



def poke_battle(player, pc):
    winner = None
    while player.is_alive and pc.is_alive:
            print(f"{player.name}: {player.HP[0]}/{player.HP[1]}     {pc.name}: {pc.HP[0]}/{pc.HP[1]}")
            for i, attack in enumerate(player.attacks):
                print(f"{i + 1}. {attack.name}")
            
            attack = player.attacks[int(input(": ")) -1 ]
            pc.receive_damage(attack)
            pc_attack = player.receive_damage(choice(pc.attacks))
            if pc.is_alive and player.is_alive:
                    legend(f"{pc.name} ha recibido {attack.damage} de daño!")
                    # time.sleep(1)
                    legend(f"{player.name} ha recibido {pc_attack.damage} de daño!")
                    # time.sleep(1)

            else:
                if player.is_alive:
                    system("clear")
                    print(f"{pc.name} se ha desmayado!")
                    print("Has ganado la batalla!")
                    input(":")
                else:
                    system("clear")
                    print(f"{player.name} se ha desmayado!")
                    print("Has perdido la batalla!")
                    input(":")
                
            system("clear")
    return winner

user = ""
while user != "q":
    system("clear")
    print("1. Battalla pokemon")
    user = input(": ")
    system("clear")

    if user == "1":
        for i, pokemon in enumerate(pokemons):
            print(f"{i + 1}: {pokemon.name}")
        poke_index = int(input(": ")) -1
        player = pokemons[poke_index]
        winner = poke_battle(player, pokemons[poke_index -1])
        
        

    