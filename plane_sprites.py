import random
import pygame


# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SECOND = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建一个英雄发射子弹事件常亮
HERO_SHOOT_EVENT = pygame.USEREVENT + 1


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
    def __init__(self, is_alt=False):  # is_alt 是判断第二屏图像的参数. 默认为False;
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
        # 重写speed, y轴出现位置bottom=0, 以及x轴的随机位置 (我感觉应该在对象中实现)
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)
        self.rect.bottom = 0
        self.speed = random.randint(1, 3)

    def update(self):
        # 1. 调用父类的方法, 保持垂直方向上飞行
        super().update()
        # 2. 判断是否敌机飞出了屏幕, 如果飞出则删除对象释放内存
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵类"""
    def __init__(self):
        # 调用父类的初始化方法, 加载图像, 默认速度为0
        super().__init__("./images/me1.png", speed=0)
        # 定义英雄的初始位置:
        # x方向在屏幕的中心;
        self.rect.centerx = SCREEN_RECT.centerx
        # Y方向距离屏幕底部120像素
        self.rect.bottom = SCREEN_RECT.height - 120
        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        # 英雄需要水平移动, 且不能移出屏幕
        self.rect.x += self.speed
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width
        # 英雄每隔0.5秒发射一次, 每次三颗子弹
        # 使用计时器触发发射

    def shoot(self):
        for i in (0, 1, 2):
            # 1. 创建子弹精灵
            bullet = Bullet()
            # 2. 设置子弹精灵的位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            # 3. 将子弹精灵加到子弹精灵组中
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    """子弹类"""
    def __init__(self):
        # 调用父类方法, 设置子弹图片, 设置初始速度
        super().__init__("./images/bullet1.png", speed=-2)

    def update(self):
        # 调用父类方法, 使子弹含垂直方向飞行
        super().update()
        # 判断子弹是否飞出屏幕, 飞出则销毁
        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        pass
