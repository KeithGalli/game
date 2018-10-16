import pygame
import sys
import random

BLUE = (0,0,255)
RED = (255,0,0)

pygame.init()

# Set screen info
WIDTH = 900
HEIGHT = 700
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.update()

game_over = False

score = 0

RAINSIZE = 50
rain_list = []

SPEED = 5
AMOUNT = 10

player_pos = (WIDTH/2, HEIGHT - 100)

myfont = pygame.font.SysFont("monospace", 35)

def intersect(obj1, obj2):
	x1 = obj1[0]
	y1 = obj1[1]
	x2 = obj2[0]
	y2 = obj2[1]

	if x1 < x2 and x2 < (x1 + RAINSIZE) or x2 < x1 and x1 < (x2 + RAINSIZE):
		return y1 < y2 and y2 < (y1 + RAINSIZE) or y2 < y1 and y1 < (y2 + RAINSIZE)
	return False 

def drop_rain(rain_list, size):
	delay = random.random()
	if len(rain_list) < 10 and delay < 0.1:
		x_pos = random.randint(0, WIDTH-RAINSIZE)
		y_pos = 5
		rain_list.append(pygame.Rect(x_pos, y_pos, RAINSIZE, RAINSIZE))

def draw_rain(rain_list):
	for rain in rain_list:
		pygame.draw.rect(screen, BLUE, rain)

def draw_player():
	pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], RAINSIZE, RAINSIZE))

def set_level(score):
	SPEED = 5
	AMOUNT = 10
	if score>30:
		SPEED = score/6
		AMOUNT = score/3
	return SPEED, AMOUNT
	
def update_positions(rain_list, score, game_over):
	for idx, rain in enumerate(rain_list):
		y_cor = rain[1]
		if y_cor > HEIGHT:
			rain_list.pop(idx)
			score += 1
		elif intersect(rain, player_pos):
			game_over = True
		else:
			x_cor = rain[0]
			rain.move_ip(0, SPEED)

	return (game_over, score)


clock = pygame.time.Clock()

while not game_over:
	# draw_board(board)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if player_pos[0]-RAINSIZE < 0:
					player_pos = (0, player_pos[1])
				else:
					player_pos = (player_pos[0]-RAINSIZE, player_pos[1])
			if event.key == pygame.K_RIGHT:
				if player_pos[0]+RAINSIZE > WIDTH-RAINSIZE:
					player_pos = (WIDTH-RAINSIZE, player_pos[1])
				else:
					player_pos = (player_pos[0]+RAINSIZE, player_pos[1])

	screen.fill((36,115,180))
	drop_rain(rain_list, AMOUNT)
	draw_rain(rain_list)
	draw_player()
	game_over, score = update_positions(rain_list, score, game_over)

	text = "Score:" + str(score)
	label = myfont.render(text, 1, (255,255,0))
	screen.blit(label, (WIDTH-200, HEIGHT-40))
	SPEED, AMOUNT = set_level(score)

	pygame.display.flip()
	clock.tick(30)

print("GAME OVER!")
print("Your Score:", score)