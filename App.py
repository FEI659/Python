import pygame
from pygame.locals import * 
import sys

class App:
	surface = None # サーフェイス
	clearColor = (0,0,255) # クリアカラー.
	handlerUpdate = None # 更新コールバック関数
	handlerDraw = None # 描画コールバック関数
	clock = pygame.time.Clock() # フレームレート制御.
	frameRate = 60 # フレームレート.

	# コンストラクタ.
	def __init__(self):
		print("init App")

	# 初期化処理.
	def init(self, caption, size):
		# 初期化.
		pygame.init()
		self.surface = pygame.display.set_mode(size)
		pygame.display.set_caption(caption) # キャプション.

	# 起動.
	def launch(self):
		if self.surface is None:
			# no initialize?
			print("no initilize")
			return

		while True:
			# 塗りつぶし.
			self.surface.fill(self.clearColor)
			# 更新
			if self.handlerUpdate is not None:
				self.handlerUpdate()
			# 描画.
			if self.handlerDraw is not None:
				self.handlerDraw()
			pygame.display.update()

			# イベントハンドリング.
			for event in pygame.event.get():
				# 終了イベント.
				if event.type == QUIT:
					sys.exit()
			# wait
			self.clock.tick(self.frameRate)

	# フレームレート設定
	def setFrameRate(self, frameRate):
		self.frameRate = frameRate

	# クリアカラー設定.
	def setClearColor(self, color):
		self.clearColor = color

	# 更新メソッドのコールバック設定.
	def setHandlerUpdate(self, func):
		self.handlerUpdate = func

	# 描画メソッドのコールバック設定.
	def setHandlerDraw(self, func):
		self.handlerDraw = func

	# 円を描画.
	def drawCircle(self, x, y, radius, color):
		pygame.draw.circle(self.surface, color, (x, y), radius)