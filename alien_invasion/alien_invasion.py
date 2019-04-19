import sys
import pygame
from pygame.sprite import Group
from log import Log 
from settings import Settings
from ship import Ship
from alien import Alien
import funcs

def run():
    gameover = False
    log = Log()
    log.info('开始')
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height)) # 窗口大小
    pygame.display.set_caption(settings.title) # 设置标题

    ship = Ship(screen) # 初始化飞船
    bullets = Group()
    aliens = Group()
    alien = Alien(settings, screen)
    aliens.add(alien)
        
    while True:
        # 监听键盘和鼠标事件
        funcs.check_events(settings, screen, ship, bullets)
        if gameover:
            log.info('Game Over!')
            break
        else:
            ship.update()       
            aliens.update()
            bullets.update()

            for bullet in bullets:
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
                
            pygame.sprite.groupcollide(bullets, aliens, True, True)

            for alien in aliens:
                if alien.rect.colliderect(ship):
                    gameover = True
                if alien.rect.top >= settings.screen_height:
                    aliens.remove(alien)

            if len(aliens) == 0:
                settings.alien_speed += 0.02
                alien = Alien(settings, screen)
                aliens.add(alien)
            
            

            funcs.update_screen(settings, screen, ship, aliens, bullets)
        
        
        
run()