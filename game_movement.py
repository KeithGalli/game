import pygame
import sys
import random

# number = random.randint(0,10)
# print(number)

pygame.init()

width = 700
height = 700

screen = pygame.display.set_mode((width,height))

game_over = False

clock = pygame.time.Clock()

player_pos = width/2
pygame.draw.rect(screen, (255,0,0), (player_pos, height-50, 30, 30))

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player_pos = player_pos-20
			if event.key == pygame.K_RIGHT:
				player_pos = player_pos+20


	screen.fill((0,0,0))
	pygame.draw.rect(screen, (255,0,0), (player_pos, height-50, 30, 30))

	pygame.display.update()

	clock.tick(30)