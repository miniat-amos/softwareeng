from Scoreboard import Scoreboard
import string
import re
import pygame

# Scoreboard.loadScores()

# print(Scoreboard.toStr())

# Scoreboard.export()

pygame.init()

FILLCOL = (20,20,20)
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Press keypad +/- to change font size")

clock = pygame.time.Clock()

fs = 18
font = pygame.font.Font(None, fs)
sb = Scoreboard((500,500), (255,255,255), font)
sb.span = ((50,50), (600,600))

running = True
while running:
	# Event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP_PLUS:
				fs += 1
				sb.setFont(pygame.font.Font(None, fs))
			elif event.key == pygame.K_KP_MINUS:
				fs -= 1
				sb.setFont(pygame.font.Font(None, fs))

	screen.fill(FILLCOL)

	screen.blit(sb.surface, sb.topleft)

	pygame.display.flip()
	clock.tick(60)

Scoreboard.export()