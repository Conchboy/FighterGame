import pygame
import random

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SECOND = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=2):
        # !!主动调用父类的初始化方法 super().__init__()
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上运动
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self, is_alt=False):
        # 1. 调用父类方法实现背景的创建(image/rect/speed)
        super().__init__("./images/background.png")

        # 2. 判断是否是交替图像, 如果是,需要设置初始位置
        if is_alt:
            self.rect.y = - SCREEN_RECT.height

    def update(self):
        #  1. 调用父类的方法实现
        super().update()
        # 2. 判断是否移出屏幕, 如果移出屏幕, 那么将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):
    """敌机精灵"""
    # 初始化Enemy类
    def __init__(self):
        # 调用父类的初始化方法, 创建敌机精灵, 并确定敌机的图像
        super().__init__("./images/enemy1.png")
    # 重写speed和x轴的随机位置 (我感觉应该在对象中实现)
        self.rect.x = random.randint(20, 450)
        self.speed = random.randint(1, 5)

    def update(self):
        # 1. 调用父类的方法实现
        super().update()
        # 2. 判断是否敌机飞出了屏幕, 如果飞出则删除对象释放内存
        if self.rect.y > SCREEN_RECT.height:
            del self
