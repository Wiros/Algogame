import pygame

screen = pygame.display.set_mode((1000,1000))
background = pygame.image.load("data/background.jpg").convert()

class Player():
	def __init__(self, image, position):
		self.image = image
		self.position = position

	def moveto(self, x, y):
		self.position[0]=x
		self.position[1]=y
		screen.blit(self.image,(x,y))
		for o in objects:
			if o != self :
				screen.blit(o.image, (o.position[0], o.position[1]))
			else:
				pass
		pygame.display.update()
		screen.blit(background, (0,0))

	def moveby(self, x, y):
		self.position[0]+=x
		self.position[1]+=y
		screen.blit(self.image,(self.position[0],self.position[1]))
		for o in objects:
			if o != self :
				screen.blit(o.image, (o.position[0], o.position[1]))
			else:
				pass
		pygame.display.update()
		screen.blit(background, (0,0))

objects = []
objects.append(Player(pygame.image.load("data/player.png").convert(), [0,0]))
screen.blit(background, (0,0))
pygame.display.update()

def animate(player):
	for x in range(50):
		for y in range(50):
			player.move(x*20,y*20)
			pygame.time.delay(50)
	pygame.display.update()


print ("Succesfully imported module \"b_screen\"")