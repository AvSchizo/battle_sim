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
	


	def update(self):

		pass
	


	def createSprites(returning=False):

		sprites = {}

		# idle
		toAdd = []
		##
		img = pygame.surface.Surface((100, 100))
		img.fill("gold")
		off = [0, 0]
		toAdd.append([img, off])
		##
		sprites["idle"] = toAdd
		#


		if returning:
			return sprites
		else:
			self.sprites = sprites
