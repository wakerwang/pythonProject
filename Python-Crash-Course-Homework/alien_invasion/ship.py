# -*-coding:utf-8 -*-
# @Time : 2023/2/12 00:03
# @Author : wll
# @File : ship.py
# @SoftWare : Pycharm
import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self, ai_game):
        '''初始化飞船并设置其初始位置'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
