import pygame
# Rect类里面封装了简单的数字计算,
# 不需要执行pygame.init()就可以直接使用


hero_rect = pygame.Rect(100, 500, 120, 125)

print("英雄的原点: %d %d" % (hero_rect.x, hero_rect.y))

print("英雄的尺寸: %d %d" % (hero_rect.width, hero_rect.height))

print("%d %d" % hero_rect.size)
