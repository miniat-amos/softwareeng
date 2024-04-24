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

# Songs
maingame = 'assets/music/Maingame.mp3'
menu = 'assets/music/Menu.mp3'
menuclick = 'assets/sounds/menuselect.mp3'
testsound = 'assets/sounds/testsound.mp3'
music_gameover = 'assets/music/GameOver.mp3'
sound_fadeaway = 'assets/sounds/fadeaway.mp3'
temp_master_volume:float  #used to store master volume while it is muted in game over

### Button setup ##
# Main menu
menu_button_font = pygame.font.Font(None, 48)
img_button_hover = pygame.image.load("assets/sprites/menu/Button_Hover.png")
img_button = pygame.image.load("assets/sprites/menu/Button.png")
img_button_hover_small = pygame.image.load("assets/sprites/menu/Button_Hover_Small.png")
img_button_small = pygame.image.load("assets/sprites/menu/Button_Small.png")
# Player buttons
cowboy_button_image = pygame.image.load("assets/sprites/menu/cowboy_button.png")
cowboy_button_image_hover = pygame.image.load("assets/sprites/menu/cowboy_button_hover.png")
ninja_button_image = pygame.image.load("assets/sprites/menu/ninja_button.png")
ninja_button_image_hover = pygame.image.load("assets/sprites/menu/ninja_button_hover.png")
roadrunner_button_image = pygame.image.load("assets/sprites/menu/roadrunner_button.png")
roadrunner_button_image_hover = pygame.image.load("assets/sprites/menu/roadrunner_button_hover.png")
# Buttons
play_button = Button(275, 300, img_button, img_button_hover, "Play", menu_button_font)
options_button = Button(50, 475, img_button, img_button_hover, "Options", menu_button_font)
quit_button = Button(505, 475, img_button, img_button_hover, "Quit", menu_button_font)
back_button = Button(280, 600, img_button, img_button_hover, "Back", menu_button_font)
scoreboard_button = Button(280, 600, img_button, img_button_hover, "Scoreboard", menu_button_font)

# Logo
logo_scale = .50
img_logo = pygame.image.load("assets/sprites/menu/logo.png")
img_logo = pygame.transform.scale(img_logo, (int(img_logo.get_width() * logo_scale), int(img_logo.get_height() * logo_scale)))
# Logo Text
logo_font = pygame.font.Font(None, 65)
textsurface_logo = logo_font.render("Lightning Bolt Town", True, WHITE)

# Difficulty options buttons
difficulty = Button(0,0, img_button, img_button_hover, "Difficulty", menu_button_font)
diff_enemystr_increase = Button(0,0, img_button_small, img_button_hover_small, "+", menu_button_font)
diff_enemystr_decrease = Button(0,0, img_button_small, img_button_hover_small, "-", menu_button_font)
diff_lighting_increase = Button(0,0, img_button_small, img_button_hover_small, "+", menu_button_font)
diff_lighting_decrease = Button(0,0, img_button_small, img_button_hover_small, "-", menu_button_font)
diff_enemyspwn_increase = Button(0,0, img_button_small, img_button_hover_small, "+", menu_button_font)
diff_enemyspwn_decrease = Button(0,0, img_button_small, img_button_hover_small, "-", menu_button_font)
difficulty_buttons = [diff_enemyspwn_decrease,diff_enemyspwn_increase,diff_lighting_decrease,diff_lighting_increase,diff_enemystr_decrease,diff_enemystr_increase,back_button]

diff_lighting_text = menu_button_font.render("Lighting", True, WHITE)
diff_enemyspwn_text = menu_button_font.render("Enemy Count", True, WHITE)
diff_enemystr_text = menu_button_font.render("Enemy Strength", True, WHITE)

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

# Player select menu buttons
player_1_button_x = 20
player_2_button_x = 280
player_3_button_x= 540
player_button_y = 100
player_1_button = Button(player_1_button_x, player_button_y, cowboy_button_image, cowboy_button_image_hover, "", menu_button_font)
player_2_button = Button(player_2_button_x, player_button_y, ninja_button_image, ninja_button_image_hover, "", menu_button_font)
player_3_button = Button(player_3_button_x, player_button_y, roadrunner_button_image, roadrunner_button_image_hover, "", menu_button_font)

playermenu_buttons = [player_1_button, player_2_button, player_3_button, back_button]

buttons = [play_button, options_button, quit_button, scoreboard_button, difficulty]


def play(player_type:int):
    SETTINGS.RECALC()
    SETTINGS.IN_GAME = True

    gameover_ticks = 0
    gameover_delay = 200
    dying = False
    
    # Set up the player
    player_projectile_list:list[Projectile.Projectile] = []
    if (player_type == 0):
        player = Player.Cowboy(player_projectile_list)
    elif(player_type == 1):
        player = Player.Ninja(player_projectile_list)
    elif(player_type == 2):
        player = Player.Roadrunner(player_projectile_list)
    else:
        print("Error - invalid player index value")
        quit()

    # Create UI
    ui = UI(player)

    # Set up the camera
    camera = Camera(player, SETTINGS.WR_WIDTH, SETTINGS.WR_HEIGHT)

    player.set_camera(camera)

    MusicManager.play_song(maingame, True)

    render_group = Rendergroup()

    # Pass in reference to player object, as well as the vertical render distance 
    # Render distance should be set to (screen height / 2) normally
    map = Map(camera, render_group, 4, 60)
    map.setStartPosOf(player)

    player.map = map

    Lightning.setMap(map)

    lightning_bolt_list:list[Lightning.Lightning] = []
    enemy_list:list[Enemies.Enemy] = []
    enemy_projectile_list:list[Projectile.Projectile] = []

    # current_frame = 0
    lighting_spawn_frame = SETTINGS.LIGHTNING_SPAWN_RATE
    enemy_spawn_frame = SETTINGS.ENEMY_SPAWN_RATE

    pre_screen = pygame.Surface((SETTINGS.WR_WIDTH, SETTINGS.WR_HEIGHT))

    # Game loop1
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    quit()
            MusicManager.master_volume_game_change(event)
            if (SETTINGS.USE_DEBUG):
                if event.type == pygame.KEYDOWN:
                    # Music
                    if event.key == pygame.K_p:
                        MusicManager.play_soundfx(testsound)
                    if event.key == pygame.K_o:
                        MusicManager.play_song(menu, True)
                    if event.key == pygame.K_i:
                        MusicManager.play_song(maingame, True)
                    # Enemies
                    if event.key == pygame.K_KP7:
                        newe = Enemies.MeleeEnemy("assets/sprites/entities/enemies/zombie/", map, (10,10), (player.xi + 10, player.top-.25*SETTINGS.WR_HEIGHT))
                        enemy_list.append(newe)
                    if event.key == pygame.K_KP_8:
                        newe = Enemies.RangedEnemy("assets/sprites/entities/enemies/skeleton/", map, (16,16), (player.xi, player.top-.25*SETTINGS.WR_HEIGHT),enemy_projectile_list)
                        enemy_list.append(newe)
                    if event.key == pygame.K_KP9:
                        newe = Enemies.SummonerEnemy("assets/sprites/entities/enemies/leg_thing/", map, (32,32), (player.xi + 10, player.top-.25*SETTINGS.WR_HEIGHT), lightning_bolt_list)
                        enemy_list.append(newe)
                    if event.key == pygame.K_KP4:
                        newl = Lightning.Lightning("assets/sprites/entities/enemies/lightning/", (player.x, player.top-SETTINGS.WR_HEIGHT))
                        lightning_bolt_list.append(newl)
                    if event.key == pygame.K_KP0:
                        lightning_bolt_list.clear()
                        enemy_list.clear()
                        
                    # Other
                    if event.key == pygame.K_KP5:
                        newp = Projectile.Projectile("assets/sprites/entities/projectiles/bullet.png", (16,16), (player.xi + 10, player.top-.25*SETTINGS.WR_HEIGHT), 1, 1, 20, random.randint(0,359))
                        enemy_projectile_list.append(newp)

        # Check for game over
        if player.health <= 0 and not dying:
            MusicManager.play_soundfx(sound_fadeaway)
            global temp_master_volume
            temp_master_volume = MusicManager.master_volume
            MusicManager.set_mastervol(0)
            dying = True

        if dying:
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

            if (SETTINGS.USE_DEBUG): player.button_functions()

            # Spawn new lightning bolts
            if (lighting_spawn_frame <= 0):
                Lightning.Lightning.updateStats(player)
                lighting_spawn_frame = SETTINGS.LIGHTNING_SPAWN_RATE
                # Random chance to spawn
                newr = random.randrange(0,150,1)
                if (newr < math.sqrt(player.points)/2+15):
                    # Get random x position
                    l_x = random.randrange(0,SETTINGS.WR_WIDTH, 1)
                    # Get random y positon
                    offset = random.randrange(SETTINGS.WR_HEIGHT, SETTINGS.WR_HEIGHT + 30, 1)
                    if (player.direction_y == "up"):
                        l_y = player.yi - offset
                    else:
                        l_y = player.yi +offset
                    # Spawn lighting bolt
                    newl = Lightning.Lightning("assets/sprites/entities/enemies/lightning/",
                                    (l_x, l_y))
                    lightning_bolt_list.append(newl)

            
            # Spawn new enemies
            if (enemy_spawn_frame <= 0):	
                enemy_spawn_frame = SETTINGS.ENEMY_SPAWN_RATE
                newr = random.randrange(0, 180, 1)
                if (newr < map.getRoomCount()*math.sqrt(SETTINGS.CFG_ENEMY_RATE)):
                    enemy_type = random.randrange(1,100,1)
                    newe:Enemies.Enemy
                    position_good:bool = False
                    while (position_good == False):
                        e_x = random.randrange(5,SETTINGS.WR_WIDTH-5, 1)
                        #if (player.direction_y == "up"):
                        e_y = player.yi - random.randrange(SETTINGS.WR_HEIGHT, SETTINGS.WR_HEIGHT + 30, 1)
                        #else:
                        #    e_y = player.yi + random.randrange(SETTINGS.WR_HEIGHT, SETTINGS.WR_HEIGHT + 30, 1)
                        if (enemy_type <= SETTINGS.ENEMY_MELEE_PCT_SPAWN):
                            newe = Enemies.MeleeEnemy("assets/sprites/entities/enemies/zombie/", map, (10,10), (e_x, e_y))
                        elif (enemy_type <= SETTINGS.ENEMY_RANGED_PCT_SPAWN+SETTINGS.ENEMY_MELEE_PCT_SPAWN):
                            newe = Enemies.RangedEnemy("assets/sprites/entities/enemies/skeleton/", map, (16,16), (e_x, e_y), enemy_projectile_list)
                        else:
                            newe = Enemies.SummonerEnemy("assets/sprites/entities/enemies/leg_thing/", map, (32,32), (e_x, e_y), lightning_bolt_list)
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
            map.collide_loot(player)
            map.tick() # Update map	
            

            # Update lighting bolts and add them to the render group
            for l in lightning_bolt_list:
                l.update(player)
                if (l.should_render):
                    render_group.appendSky(l)
                else:
                    lightning_bolt_list.remove(l)
                    # Update lighting bolts and add them to the render group

            for e in enemy_list:
                e.update(player)
                if (e.should_render):
                    if isinstance(e, Enemies.SummonerEnemy):
                        render_group.appendSky(e)
                    else:
                        render_group.appendEntity(e)
                else:
                    enemy_list.remove(e)

            for ep in enemy_projectile_list:
                if (ep.alive) and camera.render_area.colliderect(ep.get_rect()):
                    render_group.appendSky(ep)
                    ep.damage_check(player)
                else:
                    enemy_projectile_list.remove(ep)
                ep.update()

            for p in player_projectile_list:
                for e in enemy_list:
                    p.damage_check(e)
                if (p.alive) and camera.render_area.colliderect(p.get_rect()):
                    render_group.appendSky(p)
                else:
                    player_projectile_list.remove(p)
                p.update()
                
            # Rendering prep
            pre_screen.fill(BG_COLOR)
            map.playerCheck(player)
            camera.update()

            # Rendering
            map.fillRendergroup(render_group)
            render_group.appendTo(player, 3)
            render_group.render(pre_screen, camera) # Render everything within the render group

            pygame.transform.scale(pre_screen, (screen_width, screen_height), screen)

            # Drawing the UI last
            ui.draw(screen, ui_font, WHITE)

            # Refresh the display
            pygame.display.flip()

            # Rendering cleanup
            render_group.clearAll()

                
            lighting_spawn_frame -= 1
            enemy_spawn_frame -= 1
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
                quit()
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

def player_select():
    # Insert our main branch options configurations once ready
    # Rendering
    #enter_score(15, datetime.now())
    back_button.setPos(280, 600)

    cowboy_button_centerx = (player_1_button.rect.left + player_1_button.rect.right) / 2
    ninja_button_centerx = (player_2_button.rect.left + player_2_button.rect.right) / 2
    roadrunner_button_centerx = (player_3_button.rect.left + player_3_button.rect.right) / 2

    # Text surface init
    title_text = menu_button_font.render("Click to select a player character!", True, WHITE)
    cowboy_text_1 = menu_button_font.render("Cowboy", True, WHITE)
    cowboy_text_2 = menu_button_font.render("Average health", True, WHITE)
    cowboy_text_3 = menu_button_font.render("Average damage", True, WHITE)
    cowboy_text_4 = menu_button_font.render("Average speed", True, WHITE)
    cowboy_text_5 = menu_button_font.render("Piercing bullets", True, WHITE)
    ninja_text_1 = menu_button_font.render("Ninja", True, WHITE)
    ninja_text_2 = menu_button_font.render("+ Health", True, WHITE)
    ninja_text_3 = menu_button_font.render("- Damage", True, WHITE)
    ninja_text_4 = menu_button_font.render("+ Speed", True, WHITE)
    ninja_text_5 = menu_button_font.render("Fast firing", True, WHITE)
    roadrunner_text_1 = menu_button_font.render("Roadrunner", True, WHITE)
    roadrunner_text_2 = menu_button_font.render("- Health", True, WHITE)
    roadrunner_text_3 = menu_button_font.render("+ Damage", True, WHITE)
    roadrunner_text_4 = menu_button_font.render("Super Speed", True, WHITE)
    roadrunner_text_5 = menu_button_font.render("- Fire Rate", True, WHITE)

    cowboy_text_x = (cowboy_button_centerx - cowboy_text_1.get_rect().width/2)
    ninja_text_x = (ninja_button_centerx - ninja_text_1.get_rect().width/2)
    roadrunner_text_x = (roadrunner_button_centerx - roadrunner_text_1.get_rect().width/2)

    while True:

        # Getting mouse data
        mouse_pos = pygame.mouse.get_pos()

        screen.fill(BLACK)

        # Drawing text for each set of buttons
        
        screen.blit(title_text, (ninja_button_centerx - title_text.get_rect().width/2, 30))
        screen.blit(cowboy_text_1, (cowboy_button_centerx - cowboy_text_1.get_rect().width/2, 350))
        screen.blit(cowboy_text_2, (cowboy_button_centerx - cowboy_text_2.get_rect().width/2, 400))
        screen.blit(cowboy_text_3, (cowboy_button_centerx - cowboy_text_3.get_rect().width/2, 450))
        screen.blit(cowboy_text_4, (cowboy_button_centerx - cowboy_text_4.get_rect().width/2, 500))
        screen.blit(cowboy_text_5, (cowboy_button_centerx - cowboy_text_5.get_rect().width/2, 550))

        screen.blit(ninja_text_1, (ninja_button_centerx - ninja_text_1.get_rect().width/2, 350))
        screen.blit(ninja_text_2, (ninja_button_centerx - ninja_text_2.get_rect().width/2, 400))
        screen.blit(ninja_text_3, (ninja_button_centerx - ninja_text_3.get_rect().width/2, 450))
        screen.blit(ninja_text_4, (ninja_button_centerx - ninja_text_4.get_rect().width/2, 500))
        screen.blit(ninja_text_5, (ninja_button_centerx - ninja_text_5.get_rect().width/2, 550))

        screen.blit(roadrunner_text_1, (roadrunner_button_centerx - roadrunner_text_1.get_rect().width/2, 350))
        screen.blit(roadrunner_text_2, (roadrunner_button_centerx - roadrunner_text_2.get_rect().width/2, 400))
        screen.blit(roadrunner_text_3, (roadrunner_button_centerx - roadrunner_text_3.get_rect().width/2, 450))
        screen.blit(roadrunner_text_4, (roadrunner_button_centerx - roadrunner_text_4.get_rect().width/2, 500))
        screen.blit(roadrunner_text_5, (roadrunner_button_centerx - roadrunner_text_5.get_rect().width/2, 550))

        # Check for hover
        for button in playermenu_buttons:
            button.draw(screen, mouse_pos)
        pygame.display.flip()
        # Check for clicking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Cycle through the buttons that can be clicked -> perform their action
                if back_button.is_clicked(mouse_pos):
                    main_menu()
                elif player_1_button.is_clicked(mouse_pos):
                    play(0)
                elif player_2_button.is_clicked(mouse_pos):
                    play(1)
                elif player_3_button.is_clicked(mouse_pos):
                    play(2)


        clock.tick(60)

def quit():
    Scoreboard.export()
    pygame.quit()
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
    
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
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

    # Position buttons
    button_size = play_button.rect.size
    x_center = (screen.get_width()-button_size[0]) // 2
    play_button.setPos(x_center, 300)

    y_space = screen.get_height() - button_size[1] - play_button.rect.top - 25
    y_spacing = 130
    x_offset = button_size[0] // 2 + 30

    difficulty.setPos(x_center-x_offset, y_space+y_spacing)
    scoreboard_button.setPos(x_center+x_offset, y_space+y_spacing)
    options_button.setPos(x_center-x_offset, y_space+2*y_spacing)
    quit_button.setPos(x_center+x_offset, y_space+2*y_spacing)

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
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Cycle through the buttons that can be clicked -> perform their action
                if play_button.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    player_select()
                if options_button.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    options()
                if quit_button.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    quit()
                if scoreboard_button.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    scoreboard()
                if difficulty.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    change_difficulty()

                

        pygame.display.flip()
        clock.tick(FRAME_RATE)

def game_over(score:int, date:datetime):
    SETTINGS.IN_GAME = False
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
                quit()
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

def change_difficulty():
    y_top = 160
    y_spacing = 120
    x_offset = 240
    x_center = screen.get_width() // 2
    bhw = diff_lighting_decrease.rect.width // 2
    bh = diff_lighting_decrease.rect.height

    diff_lighting_decrease.setPos(x_center-x_offset-bhw, y_top)
    diff_lighting_increase.setPos(x_center+x_offset-bhw, y_top)
    diff_enemyspwn_decrease.setPos(x_center-x_offset-bhw, y_top+y_spacing)
    diff_enemyspwn_increase.setPos(x_center+x_offset-bhw, y_top+y_spacing)
    diff_enemystr_decrease.setPos(x_center-x_offset-bhw, y_top+2*y_spacing)
    diff_enemystr_increase.setPos(x_center+x_offset-bhw, y_top+2*y_spacing)

    text_y_offset = (bh-diff_lighting_text.get_height()) // 2
    lighting_text_x = x_center - (diff_lighting_text.get_width() // 2)
    enemyspwn_text_x = x_center - (diff_enemyspwn_text.get_width() // 2)
    enemystr_text_x = x_center - (diff_enemystr_text.get_width() // 2)

    indicator_gap = 3
    indicator_size = (
        (2*x_offset - 11*indicator_gap - 2*bhw) // 10,
        6
    )
    indicator_off = [x_center-x_offset+bhw, bh-indicator_size[1]]

    indicator_full = pygame.Surface(indicator_size)
    indicator_empty = indicator_full.copy()
    indicator_full.fill(WHITE)
    indicator_empty.fill((20,20,20))

    back_button.setPos(280, 520)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                need_recalc = True
                if diff_lighting_decrease.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    SETTINGS.CFG_LIGHTING_DIFFICULTY = min(10, max(1, SETTINGS.CFG_LIGHTING_DIFFICULTY-1))
                elif diff_lighting_increase.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    SETTINGS.CFG_LIGHTING_DIFFICULTY = min(10, max(1, SETTINGS.CFG_LIGHTING_DIFFICULTY+1))
                elif diff_enemyspwn_decrease.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    SETTINGS.CFG_ENEMY_RATE = min(10, max(1, SETTINGS.CFG_ENEMY_RATE-1))
                elif diff_enemyspwn_increase.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    SETTINGS.CFG_ENEMY_RATE = min(10, max(1, SETTINGS.CFG_ENEMY_RATE+1))
                elif diff_enemystr_decrease.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    SETTINGS.CFG_ENEMY_STRENGTH = min(10, max(1, SETTINGS.CFG_ENEMY_STRENGTH-1))
                elif diff_enemystr_increase.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    SETTINGS.CFG_ENEMY_STRENGTH = min(10, max(1, SETTINGS.CFG_ENEMY_STRENGTH+1))
                elif back_button.is_clicked(mouse_pos):
                    MusicManager.play_soundfx(menuclick)
                    main_menu()
                else:
                    need_recalc = False
                if need_recalc: SETTINGS.RECALC()
        
        screen.fill(BLACK)
        for button in difficulty_buttons:
            button.draw(screen, mouse_pos)

        for i in range(0, 10):
            pos = (
                i*(indicator_gap+indicator_size[0]) + indicator_gap + indicator_off[0],
                y_top+indicator_off[1]
            )
            if (SETTINGS.CFG_LIGHTING_DIFFICULTY > i):
                screen.blit(indicator_full, pos)
            else:
                screen.blit(indicator_empty, pos)

        for i in range(0, 10):
            pos = (
                i*(indicator_gap+indicator_size[0]) + indicator_gap + indicator_off[0],
                y_top+indicator_off[1]+y_spacing
            )
            if (SETTINGS.CFG_ENEMY_RATE > i):
                screen.blit(indicator_full, pos)
            else:
                screen.blit(indicator_empty, pos)

        for i in range(0, 10):
            pos = (
                i*(indicator_gap+indicator_size[0]) + indicator_gap + indicator_off[0],
                y_top+indicator_off[1]+2*y_spacing
            )
            if (SETTINGS.CFG_ENEMY_STRENGTH > i):
                screen.blit(indicator_full, pos)
            else:
                screen.blit(indicator_empty, pos)

        screen.blit(diff_lighting_text, (lighting_text_x, y_top+text_y_offset))
        screen.blit(diff_enemyspwn_text, (enemyspwn_text_x, y_top+text_y_offset+y_spacing))
        screen.blit(diff_enemystr_text, (enemystr_text_x, y_top+text_y_offset+2*y_spacing))

        diff_score_scale = menu_button_font.render("Score Multiplier: " + str(SETTINGS.SCORE_MULTIPLIER), True, WHITE)
        screen.blit(diff_score_scale, (
            x_center - diff_score_scale.get_width() // 2,
            60
        ))

        pygame.display.flip()
        clock.tick(SETTINGS.FRAMERATE)


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
                quit()
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
