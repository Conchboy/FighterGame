import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序"""

    def __init__(self):
        print("游戏初始化")
        # 创建游戏窗口 (空间)
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟 (时间)
        self.clock = pygame.time.Clock()
        # 创建游戏精灵角色, 调用私有方法 (角色)
        self.__create_sprites()

    def __create_sprites(self):
        # 1. 创建背景精灵和精灵组
        background1 = Background()
        background2 = Background(True)

        self.back_group = pygame.sprite.Group(background1, background2)

        # 2. 创建敌人精灵和精灵组
        plane_sprites = GameSprite("./images/enemy1.png")
        plane_sprites1 = GameSprite("./images/enemy1.png")
        plane_sprites2 = GameSprite("./images/enemy1.png")
        self.sprites_group = pygame.sprite.Group(plane_sprites, plane_sprites2, plane_sprites1)

        # 3. 创建英雄
        self.hero = GameSprite("./images/me1.png", speed=2)
        self.hero.rect.y = SCREEN_RECT.height



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

    def __check_collision(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.sprites_group.update()
        self.sprites_group.draw(self.screen)
        self.hero.update()

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
