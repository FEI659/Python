import pygame
from pygame.locals import * 
import sys

class App:
	screen = None
	clearColor = (0,0,255) # クリアカラー.

	# コンストラクタ.
	def __init__(self):
		print("init App")

	# 初期化処理.
	def init(self, caption, size):
		# 初期化.
		pygame.init()
		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption(caption) # キャプション.

	# 起動.
	def launch(self):
		if self.screen is None:
			# no initialize?
			print("no initilize")
			return

		while True:
			# 塗りつぶし.
			self.screen.fill(self.clearColor)
			# 画面更新.
			pygame.display.update()

			# イベントハンドリング.
			for event in pygame.event.get():
				# 終了イベント.
				if event.type == QUIT:
					sys.exit()

	# クリアカラー設定.
	def setClearColor(self, color):
		self.clearColor = color

