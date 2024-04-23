import pygame
import sys
import random
import math

import SETTINGS
from Map import Map
from Camera import Camera
import Player
from Rendergroup import Rendergroup
import Lightning
from ui import UI
from Button import Button
import Enemies
import Projectile
#import StaticMusicManager
import Loot
from Scoreboard import Scoreboard
from Scoreboard import EnterScore
from Scoreboard import Score
from datetime import datetime

from MusicManager import MusicManager #TEMP DELETE AFTER FIXING STATIC

FRAME_RATE = SETTINGS.FRAMERATE
PRINT_RATE = FRAME_RATE if FRAME_RATE else 600 

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
pygame.display.set_caption("Lightning Bolt Town")

# Set up colors
BG_COLOR = (255, 63, 127)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (245, 18, 2)


# Set up clock
clock = pygame.time.Clock()

# Set up the music manager
#music_manager = MusicManager.MusicManager()
# Songs
maingame = 'assets/music/Maingame.mp3'
menu = 'assets/music/Menu.mp3'
menuclick = 'assets/sounds/menuselect.mp3'
testsound = 'assets/sounds/testsound.mp3'
music_gameover = 'assets/music/GameOver.mp3'
sound_fadeaway = 'assets/sounds/fadeaway.mp3'
temp_master_volume:float  #used to store master volume while it is muted in game over

# Button setup
menu_button_font = pygame.font.Font(None, 48)
img_button_hover = pygame.image.load("assets/sprites/menu/Button_Hover.png")
img_button = pygame.image.load("assets/sprites/menu/Button.png")
img_button_hover_small = pygame.image.load("assets/sprites/menu/Button_Hover_Small.png")
img_button_small = pygame.image.load("assets/sprites/menu/Button_Small.png")

# Logo
logo_scale = .50
img_logo = pygame.image.load("assets/sprites/menu/logo.png")
img_logo = pygame.transform.scale(img_logo, (int(img_logo.get_width() * logo_scale), int(img_logo.get_height() * logo_scale)))
# Logo Text
logo_font = pygame.font.Font(None, 65)
textsurface_logo = logo_font.render("Lightning Bolt Town", True, (255, 255, 255))


# Buttons
play_button = Button(275, 300, img_button, img_button_hover, "Play", menu_button_font)
options_button = Button(50, 475, img_button, img_button_hover, "Options", menu_button_font)
quit_button = Button(505, 475, img_button, img_button_hover, "Quit", menu_button_font)
back_button = Button(280, 600, img_button, img_button_hover, "Back", menu_button_font)
scoreboard_button = Button(280, 600, img_button, img_button_hover, "Scoreboard", menu_button_font)

# Options menu buttons
volbutton_x1 = 130
volbutton_x2 = 595
volubtton_y = 90
volbutton_y_change = 100
mastervol_increase = Button(volbutton_x2, volubtton_y, img_button_small, img_button_hover_small, "+", menu_button_font)
mastervol_decrease = Button(volbutton_x1, volubtton_y, img_button_small, img_button_hover_small, "-", menu_button_font)
musicvol_increase = Button(volbutton_x2, volubtton_y + volbutton_y_change * 1, img_button_small, img_button_hover_small, "+", menu_button_font)
musicvol_decrease = Button(volbutton_x1, volubtton_y + volbutton_y_change * 1, img_button_small, img_button_hover_small, "-", menu_button_font)
soundfxvol_increase = Button(volbutton_x2, volubtton_y + volbutton_y_change * 2, img_button_small, img_button_hover_small, "+", menu_button_font)
soundfxvol_decrease = Button(volbutton_x1, volubtton_y + volbutton_y_change * 2, img_button_small, img_button_hover_small, "-", menu_button_font)

optionsmenu_buttons = [mastervol_increase, mastervol_decrease, musicvol_increase, musicvol_decrease, soundfxvol_increase, soundfxvol_decrease, back_button]

buttons = [play_button, options_button, quit_button, scoreboard_button]

enemy_projectile_list:list[Projectile.Projectile] = []


def play():

    gameover_ticks = 0
    gameover_delay = 200
    dying = False
    
    # Set up the player
    player = Player.Player("assets/sprites/entities/players/cowboy/")

    # Create UI
    ui = UI(player)

    # Set up the camera
    camera = Camera(player, SETTINGS.WR_WIDTH, SETTINGS.WR_HEIGHT)

    MusicManager.play_song(maingame, True)

    render_group = Rendergroup()

    # Pass in reference to player object, as well as the vertical render distance 
    # Render distance should be set to (screen height / 2) normally
    map = Map(camera, render_group, 4, 60)
    map.setStartPosOf(player)
    print(player.pos)

    player.map = map

    Lightning.setMap(map)

    lightning_bolt_list:list[Lightning.Lightning] = []
    enemy_list:list[Enemies.Enemy] = []
    #enemy_projectile_list:list[Projectile.Projectile] = []

    l_pressed = False
    p_pressed = False
    k_pressed = False
    left_bracket_pressed = False
    right_bracket_pressed = False
    loot_list:list[Loot.Loot] = []

    l_pressed = False
    o_pressed = False

    i = PRINT_RATE

    current_frame = 0

    pre_screen = pygame.Surface((SETTINGS.WR_WIDTH, SETTINGS.WR_HEIGHT))

    # Game loop1
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            MusicManager.master_volume_game_change(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    MusicManager.play_soundfx(testsound)
                if event.key == pygame.K_o:
                    MusicManager.play_song(menu, True)
                if event.key == pygame.K_i:
                    MusicManager.play_song(maingame, True)

        # Check for game over
        if player.health <= 0 and not dying:
            MusicManager.play_soundfx(sound_fadeaway)
            global temp_master_volume
            temp_master_volume = MusicManager.master_volume
            MusicManager.set_mastervol(0)
            dying = True

        if dying:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            diescreen = pygame.Surface((SETTINGS.WR_WIDTH, SETTINGS.WR_HEIGHT))
            diescreen.fill(BLACK)
            render_group.appendTo(player, 3)
            render_group.render(diescreen, camera)
            pygame.transform.scale(diescreen, (screen_width, screen_height), screen)



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
                game_over(player.points, datetime.now())
        
        # Not dying
        else:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                MusicManager.master_volume_game_change(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        MusicManager.play_soundfx(testsound, 1)
                    if event.key == pygame.K_o:
                        MusicManager.play_song(menu, True, 0.5)
                    if event.key == pygame.K_i:
                        MusicManager.play_song(maingame, True, 0.5)

            if (pygame.key.get_pressed()[pygame.K_l]):
                if (l_pressed == False):
                    newl = Lightning.Lightning("assets/sprites/entities/enemies/lightning/", (player.x, player.top-SETTINGS.WR_HEIGHT), FRAME_RATE * 5)
                    lightning_bolt_list.append(newl)
                l_pressed = True
            else:
                l_pressed = False

            if (pygame.key.get_pressed()[pygame.K_p]):
                if (p_pressed == False):
                    newp = Projectile.Projectile("assets/sprites/entities/projectiles/bullet.png", (16,16), (player.xi + 10, player.top-.25*SETTINGS.WR_HEIGHT), 1, 1, 20, random.randint(0,359))
                    enemy_projectile_list.append(newp)
                p_pressed = True
            else:
                p_pressed = False

            if (pygame.key.get_pressed()[pygame.K_k]):
                if (k_pressed == False):
                    newe = Enemies.MeleeEnemy("assets/sprites/entities/enemies/zombie/", map, (10,10), (player.xi + 10, player.top-.25*SETTINGS.WR_HEIGHT), 100, 20)#, 1)
                    enemy_list.append(newe)
                k_pressed = True
            else:
                k_pressed = False
            if (pygame.key.get_pressed()[pygame.K_LEFTBRACKET]):
                if (left_bracket_pressed == False):
                    newe = Enemies.RangedEnemy("assets/sprites/entities/enemies/skeleton/", map, (16,16), (player.xi + 10, player.top-.25*SETTINGS.WR_HEIGHT), 100, 20, enemy_projectile_list)
                    enemy_list.append(newe)
                left_bracket_pressed = True
            else:
                left_bracket_pressed = False

            if (pygame.key.get_pressed()[pygame.K_RIGHTBRACKET]):
                if (right_bracket_pressed == False):
                    newe = Enemies.SummonerEnemy("assets/sprites/entities/enemies/leg_thing/", map, (32,32), (player.xi + 10, player.top-.25*SETTINGS.WR_HEIGHT), 100, 20, lightning_bolt_list)
                    enemy_list.append(newe)
                right_bracket_pressed = True
            else:
                right_bracket_pressed = False

            if (pygame.key.get_pressed()[pygame.K_o]):
                if (o_pressed == False):
                    newc = Loot.Loot((player.rect.centerx, player.rect.top-100), 10)
                    loot_list.append(newc)
                o_pressed = True
            else:
                o_pressed = False

            # Spawn new lightning bolts
            current_frame += 1
            if (current_frame == FRAME_RATE):	
                current_frame = 0				# once per second:
                newr = random.randrange(0,5,1)		# 20% random chance to
                print(newr)
                if (newr == 0):						# spawn new lightning (with 5 second duration)
                    l_x = random.randrange(0,SETTINGS.WR_WIDTH, 1)
                    if (player.direction_y == "up"):
                        l_y = player.yi - random.randrange(SETTINGS.WR_HEIGHT, SETTINGS.WR_HEIGHT + 30, 1)
                    else:
                        l_y = player.yi + random.randrange(SETTINGS.WR_HEIGHT, SETTINGS.WR_HEIGHT + 30, 1)
                    newl = Lightning.Lightning("assets/sprites/entities/enemies/lightning/",
                                    (l_x, l_y), FRAME_RATE * 5)
                    lightning_bolt_list.append(newl)

            # Spawn new enemies
            if (current_frame == math.floor(FRAME_RATE/2)):	
                # once per second:
                newr = random.randrange(0,5,1)		# 1/6 random chance to
                if (newr == 0):						# spawn new enemy
                    enemy_type = random.randrange(1,100,1)
                    newe:Enemies.Enemy
                    position_good:bool = False
                    while (position_good == False):
                        e_x = random.randrange(5,SETTINGS.WR_WIDTH-5, 1)
                        #if (player.direction_y == "up"):
                        e_y = player.yi - random.randrange(SETTINGS.WR_HEIGHT, SETTINGS.WR_HEIGHT + 30, 1)
                        #else:
                        #    e_y = player.yi + random.randrange(SETTINGS.WR_HEIGHT, SETTINGS.WR_HEIGHT + 30, 1)
                        if (enemy_type <= 50):
                            newe = Enemies.MeleeEnemy("assets/sprites/entities/enemies/zombie/", map, (10,10), (e_x, e_y), 100, 20)#, 1)
                        elif (enemy_type <= 85):
                            newe = Enemies.RangedEnemy("assets/sprites/entities/enemies/skeleton/", map, (16,16), (e_x, e_y), 100, 20, enemy_projectile_list)
                        else:
                            newe = Enemies.SummonerEnemy("assets/sprites/entities/enemies/leg_thing/", map, (32,32), (e_x, e_y), 100, 20, lightning_bolt_list)
                        if isinstance(newe, Enemies.SummonerEnemy):
                            position_good = True
                        else:
                            room_index = map.getRectRoomIndex(newe.get_rect())
                            temp_good:bool = True
                            for i in range (room_index-1, room_index+1):
                                if (map.getRoom(i).collision_boolean(newe)):
                                    temp_good = False
                            position_good = temp_good
                    enemy_list.append(newe)

            # Object updates
            player.update()
            #player.set_points_increase_only(-player.y)
            player.button_functions() # Functions for player values
            map.collide_loot(player)
            map.tick() # Update map	
            player.button_functions() #just functions for player values and stuff

            # Update lighting bolts and add them to the render group
            for l in lightning_bolt_list:
                l.update(player)
                if (l.alive):
                    render_group.appendSky(l)
                else:
                    lightning_bolt_list.remove(l)
                    # Update lighting bolts and add them to the render group

            for e in enemy_list:
                e.update(player)
                if (e.alive):
                    if isinstance(e, Enemies.SummonerEnemy):
                        render_group.appendSky(e)
                    else:
                        render_group.appendEntity(e)
                else:
                    enemy_list.remove(e)

            for ep in enemy_projectile_list:
                ep.update(player)
                if (ep.alive) and camera.render_area.colliderect(ep.get_rect()):
                    render_group.appendSky(ep)
                else:
                    enemy_projectile_list.remove(ep)

            # Rendering prep
            pre_screen.fill(BG_COLOR)
            map.playerCheck(player)
            camera.update()

            # Rendering
            map.fillRendergroup(render_group)
            render_group.appendTo(player, 3)
            for lo in loot_list:
            #render_group.appendTo(lo, 2)   this doesn't seem to work but it renders properly in Map
                if (lo.update(player)) == True:
                    loot_list.remove(lo)
            render_group.render(pre_screen, camera) # Render everything within the render group

            pygame.transform.scale(pre_screen, (screen_width, screen_height), screen)

            # Drawing the UI last
            ui.draw(screen, ui_font, WHITE)

            # Refresh the display
            pygame.display.flip()

            # Renderng cleanup
            render_group.clearAll()
            
            i -= 1
            
            if i < 1:
                # print(map.getStats())
                # print(clock.get_fps())
                # print("Player Health =", player.health)
                i = PRINT_RATE

                
                
            # Cap the frame rate
            clock.tick(FRAME_RATE)

    # Quit Pygame
    quit()


def options():
    # Insert our main branch options configurations once ready
    # Rendering
    #enter_score(15, datetime.now())
    back_button.setPos(280, 400)

    while True:

        # Text surface init
        ts_mastervol = menu_button_font.render("Master Volume: " + str(round(100 * MusicManager.master_volume)) + "%", True, WHITE)
        ts_musicvol = menu_button_font.render("Music Volume: " + str(round(100 * MusicManager.music_volume)) + "%", True, WHITE)
        ts_soundfxvol = menu_button_font.render("Sound FX Volume: " + str(round(100 * MusicManager.soundfx_volume)) + "%", True, WHITE)

        ts_mastervol_centerx = (screen_width - ts_mastervol.get_rect().width) // 2
        ts_musicvol_centerx = (screen_width - ts_musicvol.get_rect().width) // 2
        ts_soundfxvol_centerx = (screen_width - ts_soundfxvol.get_rect().width) // 2

        # Getting mouse data
        mouse_pos = pygame.mouse.get_pos()

        screen.fill(BLACK)

        # Drawing text for each set of buttons
        
        screen.blit(ts_mastervol, (ts_mastervol_centerx, 100))
        screen.blit(ts_musicvol, (ts_musicvol_centerx, 200))
        screen.blit(ts_soundfxvol, (ts_soundfxvol_centerx, 300))

        # Check for hover
        for button in optionsmenu_buttons:
            button.draw(screen, mouse_pos)
        pygame.display.flip()
        # Check for clicking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Cycle through the buttons that can be clicked -> perform their action
                if back_button.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    main_menu()
                elif mastervol_increase.is_clicked(mouse_pos):
                    MusicManager.change_mastervol(0.1)
                    MusicManager.play_soundfx(menuclick)
                elif mastervol_decrease.is_clicked(mouse_pos):
                    MusicManager.change_mastervol(-0.1)
                    MusicManager.play_soundfx(menuclick)
                elif musicvol_increase.is_clicked(mouse_pos):
                    MusicManager.change_musicvol(0.1)
                    MusicManager.play_soundfx(menuclick)
                elif musicvol_decrease.is_clicked(mouse_pos):
                    MusicManager.change_musicvol(-0.1)
                    MusicManager.play_soundfx(menuclick)
                elif soundfxvol_increase.is_clicked(mouse_pos):
                    MusicManager.change_soundfxvol(0.1)
                    MusicManager.play_soundfx(menuclick)
                elif soundfxvol_decrease.is_clicked(mouse_pos):
                    MusicManager.change_soundfxvol(-0.1)
                    MusicManager.play_soundfx(menuclick)

        clock.tick(60)

def quit():
    pygame.quit()
    Scoreboard.export()
    sys.exit()

def scoreboard(default_score:Score = False):
    margins = 50
    
    sb_size = (
        SETTINGS.WIDTH - 2*margins,
        SETTINGS.HEIGHT - 3*margins - back_button.rect.height
    )

    sb = Scoreboard(sb_size)

    sb.topleft = (margins, margins)

    back_button.setPos(
        SETTINGS.WIDTH // 2 - back_button.rect.width // 2, 
        sb.bottom + margins
    )

    if default_score:
        sb.setDefaultIndex(default_score)
        print("Set default score", sb.default_indices)
    
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_PLUS:
                    fs += 1
                    sb.font = pygame.font.Font(None, fs)
                elif event.key == pygame.K_KP_MINUS:
                    fs -= 1
                    sb.font = pygame.font.Font(None, fs)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    MusicManager.play_soundfx(menuclick)
                    main_menu()
                if event.button == 4:  # Scroll up
                    sb.scrollUp(event.pos)
                elif event.button == 5:  # Scroll down
                    sb.scrollDown(event.pos)
                elif event.button == 1:  # Left click
                    sb.checkClick(event.pos)

        screen.fill(BLACK)
        sb.update()

        screen.blit(sb.surface, sb.topleft)

        back_button.draw(screen, pygame.mouse.get_pos())

        pygame.display.flip()
        clock.tick(SETTINGS.FRAMERATE)

def main_menu():

    MusicManager.play_song(menu, True)

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
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Cycle through the buttons that can be clicked -> perform their action
                if play_button.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    play()
                if options_button.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    options()
                if quit_button.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    quit()
                if scoreboard_button.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    scoreboard()
                

        pygame.display.flip()
        clock.tick(FRAME_RATE)

def game_over(score:int, date:datetime):

    # Called after the player fades away 

    # Creating both fonts
    gameover_font = pygame.font.SysFont("mvboli", 120)
    gameover_directions_font = pygame.font.SysFont("mvboli", 50)

    # Setting alpha related variables
    gameover_alpha = 0
    alpha_increase = .75 * 4

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
    MusicManager.set_mastervol(temp_master_volume)
    MusicManager.play_song(music_gameover, False)
    running = True

    # Game loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
            enter_score(score, date)
            
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


def enter_score(score_n:int, date:datetime):
    margins = 50
    es = EnterScore((
        SETTINGS.WIDTH - 2*margins,
        120
    ))
    es.setScore(score_n)
    es.setDate(date)

    es.topleft = (margins, margins)
    es.span = ((margins, margins), (margins + es.width, margins+es.row_height*2))
    
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    es.checkClick(event.pos)
            elif event.type == pygame.KEYDOWN:
                if es.typing: 
                    if event.key == pygame.K_BACKSPACE:
                        es.backspace()
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if es.addScore():
                            scoreboard(es.getScore())
                        else:
                            print("Score submission failed")
                    else:
                        es.keyInput(event.unicode)
        
        screen.fill(BLACK)
        es.update()
        
        screen.blit(es.surface, es.topleft)

        pygame.display.flip()
        clock.tick(SETTINGS.FRAMERATE)

    


main_menu()

