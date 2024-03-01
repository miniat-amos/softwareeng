import pygame
import Entity
import math
import Collision
import Building
import Map

MAP = None

def setMap(the_map:Map.Map):
    global MAP
    MAP = the_map

class Lightning(Entity.Entity):
    #MAP = None

    def __init__(self, folder:str, pos:tuple[int,int], time):
        self.size = (100,100)
        super().__init__(   folder+"target.png",    (100,100),  pos,        100,    3)
        #                   ^ img file              ^ size      ^start pos  ^health ^speed
        self.folder = folder
        self.time = time

    def update(self, player):    #player pos refers to CENTER of player rect here and in move()
        self.time -= 1
        if (self.time == 0):
            self.strike(player)
        elif (self.time == -50):
            self.kill()
        if (self.time > 0):
            self.move(player.rect.center)



    def strike(self, player) -> None:
        do_player_damage = True
        temproom = MAP.getRoom(MAP.getRectRoomIndex(self.rect))
        temptile = temproom.tile_list[temproom.getTileIndexAtLoc(self.rect)]
		#for r in range (0, len(render_group.layers[4])):
        if (not (temptile.building_left.porch.isEmpty)):
            r = self.damage_roof(temptile.building_left.porch)
            if (r): do_player_damage = False
        if (not (temptile.building_right.porch.isEmpty)):
            t = self.damage_roof(temptile.building_right.porch)
            if (t): do_player_damage = False
        if (do_player_damage):
            if (self.rect.colliderect(player.rect)):
                player.lower_health(20)
        print(do_player_damage)
        x = self.rect.centerx
        self.surface = pygame.transform.scale(pygame.image.load(self.folder + "bolt.png"),(500,500))
        self.rect.size = (500,500)
        self.rect.bottom = self.rect.top + (self.size[0]/2)
        self.rect.centerx = x

    def damage_roof(self,porch:Building.Porch) -> int:
        if self.rect.colliderect(porch.roof.rect):
            if (porch.burn_state <= 1):
                print("lightning is colliding with roof")
                porch.burn_state += 1
                porch.updateBurnState()
                return True
        return False




    def move(self, player_pos:tuple[int,int]):  #CENTER of player rect
        move = [0,0]
        horizontal_direction = 0    #   These keep track of horizontal and vertical direction. Left and down are -1,
        vertical_direction = 0      #   right and up are +1. These are used for changing direction image and for normalizing movement
        if (player_pos[0] < self.rect.center[0]):
            move[0] -= self.speed
            horizontal_direction -= 1
        if (player_pos[0] > self.rect.center[0]):
            move[0] += self.speed
            horizontal_direction += 1
        if (player_pos[1] < self.rect.center[1]):
            move[1] -= self.speed
            vertical_direction -= 1
        if (player_pos[1] > self.rect.center[1]):
            move[1] += self.speed
            vertical_direction += 1

        if (move[0] != 0) and (move[1] != 0):
            adjusted_speed = math.sqrt((self.speed*self.speed)/2)
            move[0] = adjusted_speed * horizontal_direction
            move[1] = adjusted_speed * vertical_direction
        
        if (horizontal_direction == -1):
            self.rect.centerx = max(player_pos[0], self.rect.centerx + move[0])
        elif (horizontal_direction == 1):
            self.rect.centerx = min(player_pos[0], self.rect.centerx + move[0])

        if (vertical_direction == -1):
            self.rect.centery = max(player_pos[1], self.rect.centery + move[1])
        elif (vertical_direction == 1):
            self.rect.centery = min(player_pos[1], self.rect.centery + move[1])