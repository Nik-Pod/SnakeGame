import random
from kivy.app import App
from kivy.graphics import (Color, Rectangle)
from kivy.uix.widget import Widget
from kivy.config import Config # import need modules
from kivy.clock import Clock
import module as play1

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 500) # graphic settings
Config.set('graphics', 'height', 500)

arr = [[1 if (i >= 0 and i <= 1) or (i >= 12 and i <= 13) or (j >= 0 and j <= 1) or (j >= 12 and j <= 13) else 0 for j in range(0, 14)] for i in range(0, 14)]
# generate board array

def random_apple():
	global ax, ay
	while True:
		ax = random.randint(2, 11)
		ay = random.randint(2, 11)
		if arr[ay][ax] == 0: # generate random coordinates for apple
			arr[ay][ax] = 7
			break
	ax -= 2
	ay -= 2
	ay = 9 - ay

snake1 = [[1, 0], [1, 1]]
snake2 = [[8, 8]]
see1 = [[0 for j in range(3)] for i in range(3)] # create void arrays for all
see2 = [[0 for j in range(3)] for i in range(3)]
appels = []

class PlayWidget(Widget):
	def __init__(self, **kwargs):
		super(PlayWidget, self).__init__(**kwargs)

		for i in range(len(snake1)):
			with self.canvas:
				Color(0, 1., 0)
				Rectangle(size = (50, 50), pos = (snake1[i][0] * 50, snake1[i][1] * 50)) # mark snakes on visual board
		with self.canvas:
			Color(0, 1., 0)
			Rectangle(size = (50, 50), pos = (snake2[0][0] * 50, snake2[0][1] * 50))

		arr[9 - snake1[0][1] + 2][snake1[0][0] + 2] = 2
		arr[9 - snake2[0][1] + 2][snake2[0][0] + 2] = 2 # mark start snake
		arr[9 - snake1[1][1] + 2][snake1[1][0] + 2] = 3

		random_apple()
		appels.append([ax, ay]) # mark appels on board
		random_apple()
		appels.append([ax, ay])

		for i in arr:
			print(i)
		print(appels)

		with self.canvas:
			Color(1., 0, 0)
			Rectangle(size = (50, 50), pos = (appels[0][0] * 50, appels[0][1] * 50))
		with self.canvas: # make appels on visual board
			Color(1., 0, 0)
			Rectangle(size = (50, 50), pos = (appels[1][0] * 50, appels[1][1] * 50))

	def update(self, dt):
		cx = 0
		cy = 0
		for i in range(9 - snake1[len(snake1) - 1][1] + 2 - 1, 9 - snake1[len(snake1) - 1][1] + 2 + 2):
			for j in range(snake1[len(snake1) - 1][0] + 2 - 1, snake1[len(snake1) - 1][0] + 2 + 2): # field of vision first snake
				see1[cy][cx] = arr[i][j]
				cx += 1
				if cx == 3:
					cy += 1
					cx = 0

		#or i in see1:
		#	print(i)
		#print()

		for i in range(len(snake1) - 1):
			if i == 0:
				arr[snake1[0][1]][snake1[0][0]] = 0 # update coordinates for snake
				with self.canvas:
					Color(0, 0, 0)
					Rectangle(size = (50, 50), pos = (snake1[0][0] * 50, snake1[0][1] * 50))
			snake1[i][::] = snake1[i + 1]

		move1 = play1.snake(see1)
		if move1 == 'top':
			snake1[len(snake1) - 1][1] += 1
		elif move1 == 'bottom':
			snake1[len(snake1) - 1][1] -= 1
		elif move1 == 'right':
			snake1[len(snake1) - 1][0] += 1 # move snake head
		elif move1 == 'left':
			snake1[len(snake1) - 1][0] -= 1
		with self.canvas:
			Color(0, 1., 0)
			Rectangle(size = (50, 50), pos = (snake1[len(snake1) - 1][0] * 50, snake1[len(snake1) - 1][1] * 50))
		arr[snake1[len(snake1) - 2][1]][snake1[len(snake1) - 2][0]] = 2
		arr[snake1[len(snake1) - 1][1]][snake1[len(snake1) - 1][0]] = 3
		for i in arr:
			print(i)
		print()

class SnakeGameApp(App):
	def build(self):
		play = PlayWidget()
		Clock.schedule_interval(play.update, 3) # using for add widgets and release program
		return play

if __name__ == '__main__':
	SnakeGameApp().run() # run program