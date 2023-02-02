# coding:utf-8

from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

sides = Die()
for i in range(1, 10):
    sides.roll_die()
sides = Die(10)
for i in range(1, 10):
    sides.roll_die()
sides = Die(20)
for i in range(1, 10):
    sides.roll_die()
