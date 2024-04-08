import pygame
import sys
import random

import SETTINGS
from Map import Map
from Camera import Camera
import Player
from Rendergroup import Rendergroup
import Lightning
from MusicManager import MusicManager
from ui import UI
from Button import Button

FRAME_RATE = 120
PRINT_RATE = FRAME_RATE if FRAME_RATE else 600 

FRAME_RATE = SETTINGS.FRAMERATE

# Only used to display stuff without a camera class. Should be (0,0) when camera is used. 
# DRAW_OFFSET = (200, 500)

# Initialize Pygame
pygame.init()

# Initialize font(s)
pygame.font.init()
ui_font = pygame.font.Font(None, 24)

# Set up the screen
screen_width, screen_height = 800, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("WASD to move, press 1 to spawn object at player pos")

# Set up colors
BG_COLOR = (255, 63, 127)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (245, 18, 2)


# Set up clock
clock = pygame.time.Clock()

# Set up the music manager
music_manager = MusicManager()
# Songs
maingame = 'assets/music/Maingame.mp3'
menu = 'assets/music/Menu.mp3'
menuclick = 'assets/sounds/menuselect.mp3'
testsound = 'assets/sounds/testsound.mp3'
music_gameover = 'assets/music/GameOver.mp3'
sound_fadeaway = 'assets/sounds/fadeaway.mp3'

# Button setup
menu_button_font = pygame.font.Font(None, 48)
img_button_hover = pygame.image.load("assets/sprites/menu/Button_Hover.png")
img_button = pygame.image.load("assets/sprites/menu/Button.png")
# Scaling button assets
button_scale = .33
img_button_hover = pygame.transform.scale(img_button_hover, (int(img_button_hover.get_width() * button_scale), int(img_button_hover.get_height() * button_scale)))
img_button = pygame.transform.scale(img_button, (int(img_button.get_width() * button_scale), int(img_button.get_height() * button_scale)))

# Logo
logo_scale = .50
img_logo = pygame.image.load("assets/sprites/menu/logo.png")
img_logo = pygame.transform.scale(img_logo, (int(img_logo.get_width() * logo_scale), int(img_logo.get_height() * logo_scale)))
# Logo Text
logo_font = pygame.font.Font(None, 65)
textsurface_logo = logo_font.render("Lightning Bolt Town", True, (255, 255, 255))


# Buttons
play_button = Button(275, 300, img_button, "Play", menu_button_font)
options_button = Button(50, 475, img_button, "Options", menu_button_font)
quit_button = Button(505, 475, img_button, "Quit", menu_button_font)
back_button = Button(280, 400, img_button, "Back", menu_button_font)
scoreboard_button = Button(280, 600, img_button, "Scoreboard", menu_button_font)

buttons = [play_button, options_button, quit_button, scoreboard_button]


def play():

    gameover_ticks = 0
    gameover_delay = 200
    dying = False
    
    # Set up the player
    player = Player.Player("assets/sprites/entities/players/cowboy/")

    # Create UI
    ui = UI(player)

    # Set up the camera
    camera = Camera(player, screen_width, screen_height)

    music_manager.play_song(maingame, True, .5)

    render_group = Rendergroup()

    # Pass in reference to player object, as well as the vertical render distance 
    # Render distance should be set to (screen height / 2) normally
    map = Map(camera, render_group, 4, 60)
    map.setStartPosOf(player)

    player.map = map

    Lightning.setMap(map)

    lightning_bolt_list:list[Lightning.Lightning] = []

    l_pressed = False

    i = PRINT_RATE

    current_frame = 0

    # Game loop1
    running = True
    while running:

        # Check for game over
        if player.health <= 0 and not dying:
            music_manager.play_soundfx(sound_fadeaway, 0.25)
            music_manager.set_volume(0)
            dying = True

        if dying:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill(BLACK)
            render_group.appendTo(player, 3)
            render_group.render(screen, camera)

            # Fading the player via an opacity rect
            fadescreen = pygame.Surface((screen_width, screen_height))  # the size of your rect
            fadescreen.set_alpha(gameover_ticks)                # alpha level
            fadescreen.fill((0,0,0))           # this fills the entire surface
            screen.blit(fadescreen, (0,0))    # (0,0) are the top-left coordinates
            
            # Refresh the display
            pygame.display.flip()
            clock.tick(FRAME_RATE)

            # To have some time before going to game over screen
            gameover_ticks += 1
            if gameover_ticks >= gameover_delay:
                game_over()
        else:


            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                music_manager.volume_check(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        music_manager.play_soundfx(testsound, 1)
                    if event.key == pygame.K_o:
                        music_manager.play_song(menu, True, 0.5)
                    if event.key == pygame.K_i:
                        music_manager.play_song(maingame, True, 0.5)

            if (pygame.key.get_pressed()[pygame.K_l]):
                if (l_pressed == False):
                    newl = Lightning.Lightning("assets/sprites/entities/enemies/lightning/", (player.rect.centerx, player.rect.top-SETTINGS.HEIGHT), FRAME_RATE * 5)
                    lightning_bolt_list.append(newl)
                l_pressed = True
            else:
                l_pressed = False
            
            # Spawn new lightning bolts
            current_frame += 1
            if (current_frame == FRAME_RATE):	
                current_frame = 0				# once per second:
                newr = random.randrange(0,5,1)		# 20% random chance to
                if (newr == 0):						# spawn new lightning (with 5 second duration)
                    l_x = random.randrange(-100,SETTINGS.WIDTH+100, 1)
                    if (player.direction_y == "up"):
                        l_y = player.rect.centery-SETTINGS.HEIGHT
                    else:
                        l_y = player.rect.centery+SETTINGS.HEIGHT
                    newl = Lightning.Lightning("assets/sprites/entities/enemies/lightning/",
                                    (l_x, l_y), FRAME_RATE * 5)
                    lightning_bolt_list.append(newl)
            

            # Object updates
            player.update()
            player.set_points_increase_only(-player.rect.centery)
            player.button_functions() # Functions for player values
            map.tick() # Update map	
            player.button_functions() #just functions for player values and stuff

            # Update lighting bolts and add them to the render group
            for l in lightning_bolt_list:
                l.update(player)
                if (l.alive):
                    render_group.appendSky(l)
                else:
                    lightning_bolt_list.remove(l)


            # Rendering prep
            screen.fill(BG_COLOR)
            map.playerCheck(player)
            camera.update()

            # Rendering
            map.fillRendergroup(render_group)
            render_group.appendTo(player, 3)
            render_group.render(screen, camera) # Render everything within the render group

            # Drawing the UI last
            ui.draw(screen, ui_font, WHITE)

            # Refresh the display
            pygame.display.flip()

            # Rendering cleanup
            render_group.clearAll()
            
            i -= 1
            
            if i < 1:
                # print(map.getStats())
                print(clock.get_fps())
                #print(map.getStats())
                # print("Player Health =", player.health)
                i = PRINT_RATE

            
            
            # Cap the frame rate
            clock.tick(FRAME_RATE)

    # Quit Pygame
    pygame.quit()
    sys.exit()


def options():
    # Insert our main branch options configurations once ready
    # Rendering
    while True:

        # Getting mouse data
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        screen.fill(BLACK)
        back_button.draw(screen, mouse_pos)
        pygame.display.flip()
        # Check for clicking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Cycle through the buttons that can be clicked -> perform their action
                if back_button.is_clicked(mouse_pos):
                    music_manager.play_soundfx(menuclick, .5)
                    main_menu()
        clock.tick(FRAME_RATE)

def quit():
    pygame.quit()
    exit()

def scoreboard():
    print("You clicked scoreboard - insert your scoreboard code here!")

def main_menu():

    music_manager.play_song(menu, True, 1)

    # Game loop
    while True:

        # Getting mouse data
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        # Rendering
        screen.fill(BLACK)

        # Logo
        screen.blit(img_logo, (315, 25))
        screen.blit(textsurface_logo, (275 + ((240 - textsurface_logo.get_width()) // 2), 50 + 27))

        # Check for hover
        for button in buttons:
            button.draw(screen, mouse_pos)

        # Check for clicking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Cycle through the buttons that can be clicked -> perform their action
                if play_button.is_clicked(mouse_pos):
                    music_manager.play_soundfx(menuclick, .5)
                    play()
                if options_button.is_clicked(mouse_pos):
                    music_manager.play_soundfx(menuclick, .5)
                    options()
                if quit_button.is_clicked(mouse_pos):
                    music_manager.play_soundfx(menuclick, .5)
                    quit()
                if scoreboard_button.is_clicked(mouse_pos):
                    music_manager.play_soundfx(menuclick, .5)
                    scoreboard()
                

        pygame.display.flip()
        clock.tick(FRAME_RATE)

def game_over():

    # Called after the player fades away 

    # Creating both fonts
    gameover_font = pygame.font.SysFont("mvboli", 120)
    gameover_directions_font = pygame.font.SysFont("mvboli", 50)

    # Setting alpha related variables
    gameover_alpha = 0
    alpha_increase = .75

    # Setting up text surfaces
    textsurface_gameover = gameover_font.render("Game Over", True, RED)
    textsurface_directions = gameover_directions_font.render("Press any key to continue", True, RED)

    # Setting initial alpha (to zero)
    textsurface_gameover.set_alpha(gameover_alpha)
    textsurface_directions.set_alpha(gameover_alpha)

    # Setting rectangles
    gameover_font_rect = textsurface_gameover.get_rect(center=(screen_width/2, screen_height/2.5))
    directions_font_rect = textsurface_gameover.get_rect(center=(screen_width/2, screen_height/1.5))

    # Play the game over music
    music_manager.play_song(music_gameover, True, .5)
    running = True

    # Game loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and gameover_alpha >= 200:
                # Start decreasing opacity after keyboard hit
                alpha_increase *= -1

        screen.fill(BLACK)

        # Logic to increase or decrease alpha
        if gameover_alpha <= 200 or alpha_increase < 0:
            gameover_alpha += alpha_increase
            textsurface_gameover.set_alpha(gameover_alpha)
            textsurface_directions.set_alpha(gameover_alpha)

        # Back to main menu upon fade out
        if gameover_alpha <= 0:
            main_menu()
            
        # Drawing the text
        screen.blit(textsurface_gameover, gameover_font_rect)
        screen.blit(textsurface_directions, directions_font_rect)

        # Refresh the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FRAME_RATE)

    # Quit Pygame
    pygame.quit()
    sys.exit()

main_menu()
