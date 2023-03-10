# -*-coding:utf-8 -*-
# @Time : 2023/2/14 16:56
# @Author : wll
# @File : die.py
# @SoftWare : Pycharm

from random import randint


class Die:
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
