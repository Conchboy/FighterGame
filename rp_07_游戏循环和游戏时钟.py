import pygame

# 游戏的初始化
pygame.init()

# 创建游戏窗口 480 * 700
screen = pygame.display.set_mode((480, 700))


# 绘制背景图像
# 1. 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2. bilt绘制图像
screen.blit(bg, (0, 0))
# 3. update更新屏幕显示
# pygame.display.update()

# 绘制英雄图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (170, 300))

# 可以在所有绘制工作完成之后统一完成image.update()方法
pygame.display.update()

# 设置游戏时钟
clock = pygame.time.Clock()

# 游戏循环 -->意味着游戏的正式开始
i = 0
while True:
    # 1. 设置刷新率(帧数 = 60)
    # tick方法可以定义循环体内部的代码执行的频率
    clock.tick(60)
    print(i)
    i += 1


    # 2. 检测用户交互
    # 3. 更新所有图像的位置
    # 4. 更新屏幕显示


pygame.quit()
