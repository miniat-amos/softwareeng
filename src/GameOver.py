import pygame
import sys

from MusicManager import MusicManager
import Player

PRINT_RATE = 30

# Only used to display stuff without a camera class. Should be (0,0) when camera is used. 
# DRAW_OFFSET = (200, 500)

# Initialize Pygame
pygame.init()

# Set up colors
BLACK = (20,20,20)
WHITE = (255, 255, 255)
RED = (245, 18, 2)

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Over!")

# Initialize font(s)
pygame.font.init()
ui_font = pygame.font.Font(None, 24)
gameover_font = pygame.font.SysFont("mvboli", 120)
gameover_alpha = 0
alpha_increase = .5


# Game over text
textsurface_gameover = gameover_font.render("Game Over", True, RED)
textsurface_gameover.set_alpha(gameover_alpha)
gameover_font_rect = textsurface_gameover.get_rect(center=(screen_width/2, screen_height/4))

# Set up the player
player = Player.Player("assets/sprites/entities/players/cowboy/")

# Set up clock
clock = pygame.time.Clock()

# Set up the music manager
music_manager = MusicManager()
# Songs
maingame = 'assets/music/Maingame.mp3'
menu = 'assets/music/Menu.mp3'
menuclick = 'assets/sounds/menuselect.mp3'
music_gameover = 'assets/music/GameOver.mp3'
music_manager.play_song(music_gameover, False, 1)

i = PRINT_RATE

# Game loop1
running = True
while running:
	# Event handling
	#print(gameover_alpha)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN and gameover_alpha >= 200:
			# Start decreasing opacity
			print("happens")
			alpha_increase *= -1

	screen.fill(BLACK)
	if gameover_alpha <= 200 or alpha_increase < 0:
		gameover_alpha += alpha_increase
		textsurface_gameover.set_alpha(gameover_alpha)
	if gameover_alpha <= 0:
		print("would move here")
		pass
        # Go to the main title screen
		
	screen.blit(textsurface_gameover, gameover_font_rect)

	# Refresh the display
	pygame.display.flip()

	# Cap the frame rate
	clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()