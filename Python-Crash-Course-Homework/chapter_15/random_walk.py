# -*-coding:utf-8 -*-
# @Time : 2023/2/14 14:45
# @Author : wll
# @File : random_walk.py
# @SoftWare : Pycharm

from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        # 所有的随机都从0开始
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """计算随机漫步的所有点"""
        while len(self.x_value) < self.num_points:
            # 决定前进方向以及这个方向上的步数
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个点的x值和y值
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)

    def get_step(self):
        """决定漫步的方向和距离。"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk_prictice_4(self):
        """计算随机漫步的所有点"""
        while len(self.x_value) < self.num_points:
            # 决定前进方向以及这个方向上的步数
            x_direction = choice([1, -1])
            x_distince = choice([0, 1, 2, 3, 4])
            x_step = choice(range(1, 9))

            y_direction = choice([1, -1])
            y_distince = choice([0, 1, 2, 3, 4])
            y_step = choice(range(1, 9))

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个点的x值和y值
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)
