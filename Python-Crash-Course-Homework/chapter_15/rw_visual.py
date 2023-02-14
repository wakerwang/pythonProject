# -*-coding:utf-8 -*-
# @Time : 2023/2/14 14:54
# @Author : wll
# @File : rw_visual.py
# @SoftWare : Pycharm

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use("classic")
    # fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    fig, ax = plt.subplots(figsize=(15,9),dpi=128)
    ax.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolors='none')
    ax.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none')
    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_working = input("Make another work?(y/n):")
    if keep_working == 'n':
        break
