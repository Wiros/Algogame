#!/usr/bin/env python
import pygame

pygame.init()

display_width = 800
display_height= 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Madalopak Adventures")
clock = pygame.time.Clock()

playerImage = pygame.image.load("data/player.png")

def player(x,y):
	gameDisplay.blit(playerImage,(x,y))


x = (display_width * 0.45) 
y = (display_height * 0.8)

x_change = 0
y_change = 0

crashed = False

while not crashed:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
			elif event.key == pygame.K_UP:
				y_change = -5
			elif event.key == pygame.K_DOWN:
				y_change = 5
			elif event.key == pygame.K_RIGHT:
				x_change = 5

	
	x += x_change
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			x_change = 0
			
	y += y_change
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
			y_change = 0
	
	
	gameDisplay.fill(blue)
	player(x,y)	
	pygame.display.update()

	clock.tick(60)

pygame.quit()
quit()
