#
# a game by Adam Binks

import pygame, random
from object import Building, Bomber

class GameHandler:
	def __init__(self, data):
		self.newGame(data)
		self.timeTillNewBomber = 0


	def update(self, data, dt):
		data.screen.fill((60, 60, 60))
		data.buildings.update(data)
		
		data.particleSpawners.update(data)
		data.particles.update(data)

		if self.timeTillNewBomber <= 0:
			Bomber(data, random.randint(0, 1), random.randint(50, 300))
			self.timeTillNewBomber = 1
		data.bombers.update(data)
		data.bombs.update(data)




	def newGame(self, data):
		data.newGame()

		buildingImgs = []
		for buildingFileName in ['tall1', 'tall2', 'small1', 'small2', 'small3', 'factory1']:
			buildingImgs.append(data.loadImage('assets/buildings/%s.png' %(buildingFileName)))
		x = 4
		while x < data.WINDOWWIDTH:
			img = random.choice(buildingImgs)
			if x + img.get_width() < data.WINDOWWIDTH:
				Building(data, img, x)
				x += img.get_width()
			x += 4 # gap between buildings
