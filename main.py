import pygame
from pygame.locals import * 
import sys

# 定数.
SCREEN_SIZE = (640, 480) # 画面サイズ.

# 初期化.
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(u"Pygame Init Testing.")

while True:
    screen.fill((0,0,255))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()