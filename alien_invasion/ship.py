'''
飞船
'''

import pygame
from log import Log

class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.img = pygame.image.load('images/ship.bmp')
        # 飞船初始化，显示在屏幕底部居中
        self.rect = self.img.get_rect() # 把飞船当做矩形来处理
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx # 飞船水平坐标等于屏幕水平居中坐标
        self.rect.bottom = self.screen_rect.bottom # 飞船底部坐标等于屏幕底部坐标
        self.x = self.rect.left
        self.moving_left = False
        self.moving_right = False
        self.log = Log()

    def blitme(self):
        self.screen.blit(self.img, self.rect)

    def update(self, x=0.5):
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= x
        elif self.moving_right  and self.rect.right < self.screen_rect.right:
            self.x += x

        self.rect.x = self.x
            
