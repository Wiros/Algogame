import pygame
from pygame.locals import *
Y_Size_Const = 80
X_Size_Const = 60
action_queue = []

class Player():
	def __init__(self, image, position):
		self.image = image
		self.position = position

	def moveto(self, x, y):
		self.position[0]=x
		self.position[1]=y
		objects.sort(key = lambda x: x.position[1])
		for o in objects:
			screen.blit(o.image, (o.position[0]*X_Size_Const, o.position[1]*Y_Size_Const))
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
	
def handle(p):
	clock = pygame.time.Clock()	# should probably be in a higher instance
	while(1):
		for event in pygame.event.get():
			print ("Its something")		# debug really
			if event.type == QUIT:
				return
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				return True
			elif event.type == KEYDOWN and event.key == K_UP:
				p.moveby(0,-1)
			elif event.type == KEYDOWN and event.key == K_DOWN:
				p.moveby(0,1)
			elif event.type == KEYDOWN and event.key == K_LEFT:
				p.moveby(-1,0)
			elif event.type == KEYDOWN and event.key == K_RIGHT:
				p.moveby(1,0)
			elif event.type == KEYDOWN and event.key == K_RETURN:
				return False
	clock.tick(60)

def test_handling():
	action_queue.append(objects[0])
	action_queue.append(objects[1])
	action_queue.append(objects[2])
	while(action_queue):
		if(handle(action_queue[0])):
			break
		action_queue.append(action_queue[0])
		action_queue.pop(0)
	action_queue.clear()

pygame.init()
if not pygame.key:	#	debug; not really important
	print ("Keyboard is fucked")
if not pygame.event:
	print ("Event is fucked")
Screen_init(1000,1000)	# arbitrarily decide what your game screen should look like, you chauvinist
set_background("background.jpg")
Objects_init(3)

print ("Succesfully imported module \"b_screen\"")