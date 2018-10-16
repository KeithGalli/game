import pygame
import sys
import random

# number = random.randint(0,10)
# print(number)

pygame.init()

screen = pygame.display.set_mode((700,700))

game_over = False

clock = pygame.time.Clock()

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	pygame.display.update()

	clock.tick(30)