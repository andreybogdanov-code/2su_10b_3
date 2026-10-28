# Следният код трябва да се разшири като:
# - Трябва да се добави атака която да е на случаен принцип за всеки от играчите. Числата трябва да са между 1 и 20
# - Трябва да се добави лекуване на всеки четен рунд за играчите със случайна стойност между 1 и 20.
#
# Задачата трябва да бъде качена и споделена в Github

import random

class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def attack(self, target):
        damage = random.randint(1, 20)
        target.take_damage(damage)

    def is_alive(self):
        return self.health > 0

john = Character('John', 100, 20)
alex = Character('Alex', 150, 20)

round_number = 1

while john.is_alive() and alex.is_alive():
    print('Round ' + str(round_number))

    john.attack(alex)

    if alex.is_alive():
        alex.attack(john)

    if round_number % 2 == 0:
        if john.is_alive():
            john.heal(random.randint(1, 20))

        if alex.is_alive():
            alex.heal(random.randint(1, 20))

    round_number += 1


print('Winner is')

if john.is_alive():
    print('John')
elif alex.is_alive():
    print('Alex')
