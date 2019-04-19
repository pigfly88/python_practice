import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(ship.rect.centerx, ship.rect.top, settings.bullet_width, settings.bullet_height)
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

    def drawme(self):
            pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.rect.y -= 1
            

