# -*-coding:utf-8 -*-
# @Time : 2023/2/13 16:47
# @Author : wll
# @File : mpl_squares.py
# @SoftWare : Pycharm
import matplotlib
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
fix, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
# 设置图标标题并给坐标轴加上标签1
ax.set_title("square", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("value's square", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)
# ax.plot(squares)
plt.show()
