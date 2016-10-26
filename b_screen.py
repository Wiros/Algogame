import pygame
from pygame.locals import *
Y_Size_Const = 80
X_Size_Const = 60


class Player():
	def __init__(self, image, position):
		self.image = image
		self.position = position

	def moveto(self, x, y):
		self.position[0]=x
		self.position[1]=y
		screen.blit(self.image,(x*X_Size_Const,y*Y_Size_Const))
		for o in objects:
			if o != self :
				screen.blit(o.image, (o.position[0]*X_Size_Const, o.position[1]*Y_Size_Const))
			else:
				pass
		pygame.display.update()
		screen.blit(background, (0,0))

	def moveby(self, x, y):
		self.position[0]+=x
		self.position[1]+=y
		self.moveto(self.position[0],self.position[1])

def Screen_init(size_x,size_y):
	global screen
	screen = pygame.display.set_mode((size_x,size_y))

def set_background(filename):
	screen.fill((0,0,0))
	global background
	background = pygame.image.load("data/"+filename).convert()
	screen.blit(background, (0,0))
	pygame.display.update()


def Objects_init(number):
	global objects
	objects = []
	for i in range(number):
		objects.append(Player(pygame.image.load("data/player.png").convert(), [0,0]))	# will probably want to load some different images

def Event_handling():
	i = 0	# not really important
	clock = pygame.time.Clock()	# should probably be in a higher instance
	while(1):
		for event in pygame.event.get():
			print ("Its something")		# debug really
			if event.type == QUIT:
				return
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				return
			elif event.type == KEYDOWN and event.key == K_UP:
				objects[i].moveby(0,-1)
			elif event.type == KEYDOWN and event.key == K_DOWN:
				objects[i].moveby(0,1)
			elif event.type == KEYDOWN and event.key == K_LEFT:
				objects[i].moveby(-1,0)
			elif event.type == KEYDOWN and event.key == K_RIGHT:
				objects[i].moveby(1,0)
			elif event.type == KEYDOWN and event.key == K_RETURN:
				i+=1 	# remember to change it in final version
				if(i == objects.__len__()):
					i=0
			else:
				pass
	clock.tick(60)

pygame.init()
if not pygame.key:	#	debug; not really important
	print ("Keyboard is fucked")
if not pygame.event:
	print ("Event is fucked")
Screen_init(1000,1000)	# arbitrarily decide what your game screen should look like, you chauvinist
set_background("background.jpg")
Objects_init(3)

print ("Succesfully imported module \"b_screen\"")
