from Scoreboard import Scoreboard
import string
import re
import pygame
import sys

pygame.init()

FILLCOL = (20,20,20)
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Press keypad +/- to change font size  |  Click header to change sort")

clock = pygame.time.Clock()

fs = 24
font = pygame.font.Font(None, fs)
sb = Scoreboard((500,500), font)
sb.span = ((50,50), (600,600))

running = True
while running:
	# Event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP_PLUS:
				fs += 1
				sb.setFont(pygame.font.Font(None, fs))
			elif event.key == pygame.K_KP_MINUS:
				fs -= 1
				sb.setFont(pygame.font.Font(None, fs))
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4:  # Scroll up
				sb.scrollUp(event.pos)
			elif event.button == 5:  # Scroll down
				sb.scrollDown(event.pos)
			elif event.button == 1:  # Left click
				sb.checkClick(event.pos)

	screen.fill(FILLCOL)
	sb.update()

	screen.blit(sb.surface, sb.topleft)

	pygame.display.flip()
	clock.tick(60)

Scoreboard.export()