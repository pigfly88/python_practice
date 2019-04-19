class Settings:
    def __init__(self):
        # 打印日志
        self.debug = True
        # 标题
        self.title = 'Alien Invasion'
        # 窗口大小
        self.screen_height = 500
        self.screen_width = 500
        # 背景颜色
        self.bgcolor = (230, 230, 230)

        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        # 外星人
        self.alien_speed = 0.1