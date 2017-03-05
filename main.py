import pygame
from pygame.locals import * 
import sys
import App

# 定数.
SCREEN_CAPTION = u"My Pygame Application"
SCREEN_SIZE = (640, 480) # 画面サイズ.
SCREEN_COLOR = (0,0,0) # 画面カラー.

app = App.App()
app.init(SCREEN_CAPTION, SCREEN_SIZE)
app.setClearColor(SCREEN_COLOR)
app.launch()