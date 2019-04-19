import pygame
import sys
from bullet import Bullet
from log import Log

# 捕捉键盘和鼠标事件
def check_events(settings, screen, ship, bullets):
    log = Log()
    
    for event in pygame.event.get():
        # 鼠标点击关闭
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_LEFT: # 按下左方向键
                log.info('向左移动 - 开始')
                ship.moving_left = True
            elif event.key == pygame.K_RIGHT:
                log.info('向右移动 - 开始')
                ship.moving_right = True
            elif event.key == pygame.K_SPACE:
                log.info('发射子弹 - 开始')
                new_bullet = Bullet(settings, screen, ship)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                log.info('向左移动 - 停止')
                ship.moving_left = False
            elif event.key == pygame.K_RIGHT:
                log.info('向右移动 - 停止')
                ship.moving_right = False

# 更新屏幕上的图像，并切换到新屏幕
def update_screen(settings, screen, ship, aliens, bullets):
    screen.fill(settings.bgcolor) # 每次循环都重绘屏幕

    ship.blitme()
    for alien in aliens.sprites():
        alien.blitme()

    for bullet in bullets.sprites():
        bullet.drawme()


    pygame.display.flip() # 让最近绘制的屏幕可见