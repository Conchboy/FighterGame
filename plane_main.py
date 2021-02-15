import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序"""

    def __init__(self):
        pygame.init()  # 这是为了处理程序无法正确启动pygame库的问题
        # 创建游戏窗口 (空间)
        pygame.display.set_caption("飞机大战来一局")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟 (时间)
        self.clock = pygame.time.Clock()
        # 创建游戏精灵角色, 调用私有方法 (角色)
        self.__create_sprites()
        # 设置定时器事件 -- 为了每秒创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 设置定时器事件 -- 为了英雄没半秒发射三发子弹
        pygame.time.set_timer(HERO_SHOOT_EVENT, 500)
        # 设定游戏初始分 为0,
        score_this_game = 0


    def __create_sprites(self):
        # 1. 创建背景精灵和精灵组
        background1 = Background()  # 这个background由于不用在外部调用, 所以不像下面的self.hero需要定义成属性
        background2 = Background(True) # 这里使用True作为参数, 用于定义第二屏的连接和滚动效果. 详见plain_sprite的background的初始化重写.
        self.back_group = pygame.sprite.Group(background1, background2)

        # 2. 创建敌人精灵和精灵组
        self.sprites_group = pygame.sprite.Group()

        # 3. 创建英雄的精灵和精灵组
        self.hero = Hero()  # 重要: hero对象需要在方法外部使用, 所以需要用self.hero来定义成属性
        self.hero_group = pygame.sprite.Group(self.hero)  # 记得把self.hero传递到精灵组

    def start_game(self):
        print("游戏开始...")
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SECOND)
            # 2. 事件监听
            self.__event_handler()
            # 3. 判断碰撞检测
            self.__check_collision()
            # 4. 更新绘制精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 1. 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.sprites_group.add(enemy)
            # 判断英雄发射子弹
            elif event.type == HERO_SHOOT_EVENT:
                self.hero.shoot()
        # 使用键盘提供的方法获取键盘按键 - 按键元组 (可以始终捕获按下的键值, 不用等待抬起, 重新按键)
        keys_pressed = pygame.key.get_pressed()
        # 判断元祖中对应的按键索引值"1"
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collision(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group, self.sprites_group, True, True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.sprites_group, True)
        # 判断是否有碰撞 --> 列表enemies有内容
        if len(enemies) > 0:
            # 英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.sprites_group.update()
        self.sprites_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
