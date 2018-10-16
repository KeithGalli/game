import pygame
import sys
import random

def intersect(player_x, player_y, enemy_x, enemy_y):

	if player_x < enemy_x and enemy_x < (player_x + player_size) or enemy_x < player_x and player_x < (enemy_x + enemy_size):
		return player_y < enemy_y and enemy_y < (player_y + player_size) or enemy_y < player_y and player_y < (enemy_y + enemy_size)
	return False 

pygame.init()

width = 700
height = 700

screen = pygame.display.set_mode((width,height))

game_over = False

clock = pygame.time.Clock()

player_x = width/2
player_y = height-50
player_size = 30
pygame.draw.rect(screen, (255,0,0), (player_x, player_y, player_size, player_size))

enemy_size = 100
enemy_x = random.randint(0, width-enemy_size)
enemy_exists = True
enemy_y = 20

pygame.draw.rect(screen, (0,0,255), (enemy_x, enemy_y, enemy_size, enemy_size))

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player_x = player_x-20
			if event.key == pygame.K_RIGHT:
				player_x = player_x+20


	screen.fill((0,0,0))
	pygame.draw.rect(screen, (255,0,0), (player_x, player_y, player_size, player_size))

	if enemy_exists:
		enemy_y += 5
		pygame.draw.rect(screen, (0,0,255), (enemy_x, enemy_y, enemy_size, enemy_size))
		if intersect(player_x, player_y, enemy_x, enemy_y):
			game_over = True
		if enemy_y > height: # Off the screen, reset enemy
			enemy_exists = False

	else:
		enemy_exists = True
		enemy_x = random.randint(0,width-enemy_size)
		enemy_y = 20
		pygame.draw.rect(screen, (0,0,255), (enemy_x, enemy_y, enemy_size, enemy_size))


	pygame.display.update()

	clock.tick(30)