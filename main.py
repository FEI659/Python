import pygame
from pygame.locals import * 
import sys
import random
import App

# 定数.
SCREEN_CAPTION = u"My Pygame Application"
SCREEN_WIDTH = 640 # 画面幅
SCREEN_HEIGHT = 480 # 画面高さ
SCREEN_COLOR = (0,0,0) # 画面カラー.
FRAME_RATE = 60	# フレームレート.
# 色定数
COLOR_BLACK		= (0,0,0) # 黒
COLOR_WHITE		= (255,255,255) # 白
COLOR_RED		= (255,0,0) # 赤
COLOR_BLUE		= (0,0,255) # 青
COLOR_GREEN		= (0,255,0) # 緑
COLOR_CYAN		= (0,255,255) # シアン
COLOR_YEWLLOW	= (255,255,0) # 黄
COLOR_MAGENTA	= (255,0,255) # マゼンタ

# 変数
app = None
# TEST:
x = 0
y = 0
speedX = 8
speedY = 3

# 初期化
def init():
	global app
	app = App.App()
	app.init(SCREEN_CAPTION, (SCREEN_WIDTH, SCREEN_HEIGHT))
	app.setClearColor(SCREEN_COLOR) # クリアカラー.
	app.setHandlerUpdate(update)
	app.setHandlerDraw(draw)
	app.setFrameRate(FRAME_RATE)
	app.launch() # 起動.

# 更新.
def update():
	if (app is None):
		return

	# TEST:
	global x
	global y
	global speedX
	global speedY

	tx = x + speedX
	ty = y + speedY
	if ( tx < 0 or tx > SCREEN_WIDTH):
		speedX = int(speedX * (random.random() + 0.5) * -1)
		tx = x + speedX
	if ( ty < 0 or ty > SCREEN_HEIGHT):
		speedY = int(speedY * (random.random() + 0.5) * -1)
		ty = y + speedY
	x = tx
	y = ty

# 描画.
def draw():
	# TEST:
	global x
	global y
	app.drawCircle(x, y, 30, COLOR_RED)
	
init()
