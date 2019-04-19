import sys
import pygame
from log import Log 
from settings import Settings

def run():
    
    log = Log()
    log.info('开始')
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height)) # 窗口大小
    pygame.display.set_caption(settings.title) # 设置标题
    
    screen_rect = screen.get_rect()
    rect = pygame.Rect(screen_rect.centerx, screen_rect.bottom-5, 5, 5)
    
    while True:
        
        for event in pygame.event.get():
            # 鼠标点击关闭
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(settings.bgcolor)
        rect.y -= 1
        pygame.draw.rect(screen, (255, 0, 0), rect)
        pygame.display.flip() # 刷屏
        
run()