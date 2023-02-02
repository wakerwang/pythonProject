# coding:utf-8

from random import randint, choice
import random

numbers = [11, 23, 24, 53, 1, 10, 9, 3, 4, 5, 7, 6, 'a', 'b', 'e', 'f', 'g']
prize_numbers = random.sample(numbers, 5)
print(f"The winning number are {prize_numbers}.")
n = 1

while True:
    my_numbers = random.sample(numbers, 5)
    if my_numbers != prize_numbers:
        n += 1
        continue
    else:
        print(f"It takes you {n} times to win the lottery.")
        break
