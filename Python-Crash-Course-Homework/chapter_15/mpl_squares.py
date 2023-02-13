# -*-coding:utf-8 -*-
# @Time : 2023/2/13 16:47
# @Author : wll
# @File : mpl_squares.py
# @SoftWare : Pycharm

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fix, ax = plt.subplots()
ax.plot(squares)
plt.show()
