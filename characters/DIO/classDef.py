class Class():

	def __init__(self):
		
		self.createSprites()

		self.pos = [0, 0]
		self.velocity = [0, 0]
		self.cramPush = [0, 0]

		self.health = 100

		self.timeEffects = []

		self.timeJuice = 0

		self.cooldowns = {
			"timestop": 0,
			"knife": 0,
		}

		self.startMovin()
	


	def update(self):

		pass
	


	def getCollisionRadius(self):
		
		if self.action == "idle":
			return 5
	


	def getSprite(self):
		
		if self.action == "idle":
			return self.sprites["idle"]
	


	def createSprites(returning=False):

		sp = {}

		# idle
		toAdd = []
		##
		img = pygame.surface.Surface((100, 100))
		img.fill("gold")
		off = [0, 0]
		toAdd.append([img, off])
		##
		sp["idle"] = toAdd
		#


		if returning:
			return sp
		else:
			self.sprites = sp
	


	def startMovin(self, dir=None, speed=10, returning=False):
		if dir == None:
			direction = random.randint(0, 359)*pi/180
		else:
			direction = dir
		
		thisList = [cos(direction), sin(direction)]
		
		if returning:
			return thisList
		else:
			for i in range(2):
				self.velocity[i] = thisList[i]
