# coding:utf-8

from random import randint, choice
import random

numbers = [11, 23, 24, 53, 1, 10, 9, 3, 4, 5, 7, 6, 'a', 'b', 'e', 'f', 'g']

print("The winning number are following:")
for number in range(1, 5):
    prize_number = choice(numbers)
    print(prize_number)

jackpot = list(range(10)) + ['a', 'l', 'o', 't', 'n']  # list()函数的作用是将0~10之间的数转换成列表
print(jackpot)

winning_number = random.sample(jackpot, 4)
print(f"If your number is {winning_number}, then congrats! you win the lottery.")
