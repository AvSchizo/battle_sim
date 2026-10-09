import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

import random

from math import pi, atan

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

# characters
characters = {}
for fi in list(PosixPath("characters").iterdir()):
	name = str(fi).split("/")[-1]
	characters[fi] = loadFunctionByName("classDef", f"characters/{name}/classDef.py", "Class")
#




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













###############
#  main loop  #
###############
while True:

	# calcs n shit



	# rendering
	screen.fill("lavender")




	pygame.display.update()
	clock.tick(60)