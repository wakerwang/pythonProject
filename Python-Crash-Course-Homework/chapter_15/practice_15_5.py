# -*-coding:utf-8 -*-
# @Time : 2023/2/14 15:37
# @Author : wll
# @File : practice_15_3.py
# @SoftWare : Pycharm
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use("classic")
    # fig, ax = plt.subplots()
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    point_numbers = range(rw.num_points)

    ax.plot(rw.x_value, rw.y_value, linewidth=1)
    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolors='none')
    ax.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none')
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_working = input("Make another work?(y/n):")
    if keep_working == 'n':
        break
