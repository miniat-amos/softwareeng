import pygame
from datetime import datetime
from Scoreboard import UsernameTextBox
from Scoreboard import Scoreboard

pygame.init()

Scoreboard.loadScores()

FILLCOL = (20,20,20)
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Press keypad +/- to change font size  |  Click header to change sort")

clock = pygame.time.Clock()

tb = UsernameTextBox(pygame.font.Font(None, 64))
tb.topleft = (100, 100)

running = True
while running:
	# Event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				tb.checkClick(event.pos)
		elif event.type == pygame.KEYDOWN:
			if tb.typing: 
				if event.key == pygame.K_BACKSPACE:
					tb.backspace()
				elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					tb.addScore(0, datetime.now())
				else:
					tb.keyInput(event.unicode)

	tb.update()
	screen.blit(tb.surface, tb.topleft)

	pygame.display.flip()
	clock.tick(60)

Scoreboard.export()