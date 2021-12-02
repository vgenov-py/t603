elements = ["fire", "water", "grass"]



class Pokemon:
    # propiedades de la clase:
    counter = 0

    def __init__(self, name, element, HP):
        self.name = name
        self.element = element
        self.HP = HP
        self.attacks = []
        Pokemon.counter += 1
    
    def learn(self, attack):
        self.attacks.append(attack)
    
    def receive_damage(self, attack):
        self.HP -= attack.damage

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

# Attacks instances:

flamethrower = Attack("Flamethrower", elements[0], 25)

charmander.learn(flamethrower)

def receive_damage(target, attack):
    target.HP -= attack.damage

print("Vida de Squirtle antes de ser atacado",squirtle.HP)
receive_damage(squirtle, charmander.attacks[0])
print("Vida de Squirtle después de ser atacado con la función receive_damage",squirtle.HP)
squirtle.receive_damage(charmander.attacks[0])
print("Vida de Squirtle después de ser atacado con el método receive_damage",squirtle.HP)

