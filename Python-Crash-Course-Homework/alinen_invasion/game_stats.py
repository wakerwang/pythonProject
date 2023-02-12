# -*-coding:utf-8 -*-
# @Time : 2023/2/12 22:54
# @Author : wll
# @File : game_stats.py
# @SoftWare : Pycharm

class GameStats:
    """跟踪游戏的统计信息"""
    def __init__(self,ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active =True

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
