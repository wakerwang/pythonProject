# -*-coding:utf-8 -*-
# @Time : 2023/2/14 14:13
# @Author : wll
# @File : catter_squares.py
# @SoftWare : Pycharm

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn')
fix, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# 设置图标标题并给坐标轴加上标签1
ax.set_title("square", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("value's square", fontsize=14)

ax.axis([0, 1100, 0, 1100000])
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')