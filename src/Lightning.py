import pygame
import SETTINGS
import Entity
import math
import Collision
import Building
import Map
import SETTINGS
#import StaticMusicManager
import Player
import random
from MusicManager import MusicManager

MAP = None

def setMap(the_map:Map.Map):
    global MAP
    MAP = the_map

class Lightning(Entity.Entity):
    speed = SETTINGS.LIGHTNING_DEFAULT_SPEED
    start_time = SETTINGS.FRAMERATE * 5
    #MAP = None

    def __init__(self, folder:str, pos:tuple[int,int]):
        super().__init__(   folder+"target.png",    (12, 12),  pos,        100,    Lightning.speed)
        #                   ^ img file              ^ size      ^start pos  ^health ^speed
        #self.surface.set_alpha(196)
        self.folder = folder
        self.time = Lightning.start_time
        self.last_move:tuple[float,float] = [0,0]
        self.tex_offset = (2,2)

    def update(self, player):    #player pos refers to CENTER of player rect here and in move()
        self.time -= 1
        if (self.time > 0):
            self.move(player.posi)
        if (self.time == 0):
            self.strike(player)
            self.kill()
        super().update()



    def strike(self, player:Player.Player) -> None:
        temproom = MAP.getRoom(MAP.getRectRoomIndex(self.get_rect()))
        temptile = temproom.tile_list[temproom.getTileIndexAtLoc(self.get_rect())]
        porch_right = temptile.building_right.porch
        porch_left = temptile.building_left.porch
        
		# Check if lighting collides with a roof. If it does, don't damage the player
        do_player_damage = not (porch_right.lightingStrike(self.get_rect()) 
                            or porch_left.lightingStrike(self.get_rect()))

        if (do_player_damage):
            if (self.get_rect().colliderect(player.get_rect())):
                player.damage(SETTINGS.LIGHTNING_DAMAGE)
        
        self.surface = pygame.image.load(self.folder + "bolt.png")
        MusicManager.play_soundfx("assets/sounds/entities/enemies/lightning/static_zap.wav")
        self.size = (124,128)
        self.bottom = self.y
        # print("Base from Player: (%d, %d)" % (self.x-player.x, self.bottom-player.y))
        # print("From Player: (%d, %d)" % (self.x-player.x, self.y-player.y))

    # def old_move_not_using(self, player_pos:tuple[int,int]):  #CENTER of player rect
    #     move = [0,0]
    #     horizontal_direction = 0    #   These keep track of horizontal and vertical direction. Left and down are -1,
    #     vertical_direction = 0      #   right and up are +1. These are used for changing direction image and for normalizing movement
    #     if (player_pos[0] < self.x):
    #         move[0] -= self.speed
    #         horizontal_direction -= 1
    #     if (player_pos[0] > self.x):
    #         move[0] += self.speed
    #         horizontal_direction += 1
    #     if (player_pos[1] < self.y):
    #         move[1] -= self.speed
    #         vertical_direction -= 1
    #     if (player_pos[1] > self.y):
    #         move[1] += self.speed
    #         vertical_direction += 1

    #     if (move[0] != 0) and (move[1] != 0):
    #         adjusted_speed = math.sqrt((self.speed*self.speed)/2)
    #         move[0] = adjusted_speed * horizontal_direction
    #         move[1] = adjusted_speed * vertical_direction
        
    #     if (horizontal_direction == -1):
    #         self.x = max(player_pos[0], self.x + move[0])
    #     elif (horizontal_direction == 1):
    #         self.x = min(player_pos[0], self.x + move[0])

    #     if (vertical_direction == -1):
    #         self.y = max(player_pos[1], self.y + move[1])
    #     elif (vertical_direction == 1):
    #         self.y = min(player_pos[1], self.y + move[1])

    def move(self, player_pos:tuple[int,int]):  #CENTER of player rect
        dx = player_pos[0] - self.get_rect().centerx
        dy = player_pos[1] - self.get_rect().centery
        distance = math.sqrt(dx * dx + dy * dy)
        if distance < 0.01: return
        elif distance < 2:
            dx *= 2
            dy *= 2
        inertia:float = random.uniform(SETTINGS.LIGHTNING_INERTIA_RANGE_MIN, SETTINGS.LIGHTNING_INERTIA_RANGE_MAX)
        x_move = dx/distance * self.speed
        x_move = (x_move * inertia + self.last_move[0]*(1-inertia))#/2
        y_move = dy/distance * self.speed
        y_move = (y_move * inertia + self.last_move[1]*(1-inertia))#/2
        checked_move = super().lightning_move((
            x_move, y_move
        ))
        self.last_move = checked_move
        self.normalizeMove(checked_move)

    def updateStats(player:Player.Player):
        Lightning.start_time = max(
            int(SETTINGS.WR_HEIGHT / Lightning.speed + 2*SETTINGS.FRAMERATE), # Ensures it's long enough to reach the player
            int(1 + 200/(max(15,math.sqrt(player.points))))
        )

        Lightning.speed = min(
            SETTINGS.LIGHTNING_MAX_SPEED, # Sets a maximum on the speed
            SETTINGS.LIGHTNING_DEFAULT_SPEED + math.sqrt(player.points) / (16*(2+math.sqrt(SETTINGS.SCORE_MULTIPLIER)))
        )