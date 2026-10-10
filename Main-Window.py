import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

import random

from math import pi, atan

## characters
from pathlib import PosixPath
import importlib
import importlib.util
import sys

def importFromPath(moduleName, filePath):
	spec = importlib.util.spec_from_file_location(moduleName, filePath)
	module = importlib.util.module_from_spec(spec)
	sys.modules[moduleName] = module
	spec.loader.exec_module(module)
	return module

def loadFunctionByName(moduleName, filePath, functionName):
	module = importFromPath(moduleName, filePath)
	return getattr(module, functionName)

# assigning
characters = {}
for fi in list(PosixPath("characters").iterdir()):
	name = str(fi).split("/")[-1]
	characters[fi] = loadFunctionByName("classDef", f"characters/{name}/classDef.py", "Class")
##


def characterMovement(character, velocity=None, radius=None):

	if velocity == None:
		try:
			vel = character.velocity
		except AttributeError:
			vel = [0, 0]
	else:
		vel = velocity
	
	if radius == None:
		try:
			r = character.getCollisionRadius()
		except AttributeError:
			r = 1
	else:
		r = radius
	
	
	def shit():
		




playpen = [
	[[-1000, 1000], [1000, 1000]],
	[[1000, 1000], [1000, -1000]],
	[[1000, -1000], [-1000, -1000]],
	[[-1000, -1000], [-1000, 1000]],
]


def findDirection(velocities):

	vel = []

	le = len(velocities)
	for e in range(2):
		av = 0
		for i in range(le):
			av += velocities[i]
		av /= le
		vel.append(av)
	
	# no velocity
	if vel[0] == 0 and vel[1] == 0:
		return 0

	# cardinals
	if vel[0] == 0:
		if vel[1] > 0:
			return pi/2
		else:
			return 3*pi/2
	if vel[1] == 0:
		if vel[0] > 0:
			return 0
		else:
			return pi

	# real maths
	baseDir = atan(vel[1]/vel[0])

	if vel[0] < 0:
		baseDir += pi
	
	return baseDir






# setup
def setup(charList):
	toReturn
	for char in charList:
		try:
			toReturn.append(characters[char])
		except IndexError:
			print(f"no character in characters named {char}")
	
	return toReturn

playing = setup(["DIO"])











currentFrame = 0
###############
#  main loop  #
###############
while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
	
	currentFrame += 1

	# calcs n shit
	if currentFrame == 1:
		for char in playing:
			char.startMovin()



	# rendering
	screen.fill("lavender")

	for char in playing:
		char.draw()




	pygame.display.update()
	clock.tick(60)
