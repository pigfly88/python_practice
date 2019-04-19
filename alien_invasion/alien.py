import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.img = pygame.image.load('images/alien.bmp')
        self.rect = self.img.get_rect()
        screen_rect = screen.get_rect()
        self.rect.top = screen_rect.top - self.rect.height
        self.rect.x = random.randint(screen_rect.left, screen_rect.right - self.rect.width)
        self.speed = settings.alien_speed
        #self.x = float(self.rect.x) * random.random() * 3
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.img, self.rect)

    def update(self):
        #self.x += self.speed * random.random() * 3 * random.randint(-1, 1)
        #self.rect.x = self.x

        

        self.y += self.speed
        self.rect.y = self.y
