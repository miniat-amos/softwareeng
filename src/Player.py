import pygame
import Entity
import Inventory
import SETTINGS
import Camera
import math
import Projectile
from MusicManager import MusicManager

class Player(Entity.GroundEntity):# pygame.sprite.Sprite):
    def __init__(self, texture_folder:str, player_projectile_list, map, attack_cooldown, speed):
        super().__init__(   texture_folder, map,    (10,10),  (400,400),  100,    speed)
        
        self.points = 0 #probably best to store points/money directly, rather than in inventory
        self.inventory = Inventory.Inventory()
        self.build = 0
        self.tex_offset = [-3,-6]
        self.camera:Camera.Camera
        self.projectile_list = player_projectile_list
        self.attack_cooldown:int = attack_cooldown
        self.attack_cooldown_max:int = attack_cooldown
        self.projectile_image:str
        self.projectile_piercing:bool
        self.projectile_sound:str
        self.projectile_speed:float
        self.projectile_damage:int
        self.iframes_max = SETTINGS.PLAYER_IFRAMES

    def set_camera(self, camera:Camera.Camera):
        self.camera = camera
    
    def add_points(self, amount:int):
        if (amount < 0):
            raise Exception("Tried to add a negative amount of points")
        else:
            self.points += amount

    def remove_points(self, amount:int):
        if (amount < 0):
            raise Exception("Tried to remove a negative amount of points. Input a positive number of points to be removed.")
        else:
            self.points -= amount

    def set_points(self, points:int):
        self.points = points

    def set_points_increase_only(self, points:int):
        if (points > self.points):
            self.points = math.floor(points)
    
    def update(self):
        if (self.alive):
            self.attack_cooldown = max(0, self.attack_cooldown-1)
            self.move()
            self.ranged_attack()
            super().update()

    def move(self):
        horizontal_direction = 0    #   These keep track of horizontal and vertical direction. Left and down are -1,
        vertical_direction = 0      #   right and up are +1. These are used for changing direction image and for normalizing movement
        if (pygame.key.get_pressed()[pygame.K_a]):
            horizontal_direction -= 1
        if (pygame.key.get_pressed()[pygame.K_d]):
            horizontal_direction += 1
        if (pygame.key.get_pressed()[pygame.K_w]):
            vertical_direction -= 1
        if (pygame.key.get_pressed()[pygame.K_s]):
            vertical_direction += 1
        
        move_dir = (horizontal_direction, vertical_direction)
        
        if not (move_dir[0] or move_dir[1]): return

        move = [self.speed * move_dir[0], self.speed * move_dir[1]]

        # Move with collision checks, return actual movement vector
        checked_move = super().move(move)

        # If the entity is moving
        if (checked_move[0] and checked_move[1]):
            # If distances are similar, just shorten the distance equally
            if abs(abs(checked_move[0]) - abs(checked_move[1])) < 0.125:
                self.normalizeMove(checked_move)
            # If X-movement is greater, adjust X-movement only
            elif abs(checked_move[1]) < abs(checked_move[0]):
                self.y += undoAxis(checked_move[1], checked_move[0], self.speed)
            # If Y-movement is greater, adjust Y-movement only
            else:
                self.x += undoAxis(checked_move[0], checked_move[1], self.speed)

    def ranged_attack(self):
        if (pygame.mouse.get_pressed()[0] and self.attack_cooldown == 0):
            print(pygame.mouse.get_pos()[0] + self.camera.render_area.left, 
                  SETTINGS.SCALE*self.camera.render_area.bottom - (SETTINGS.HEIGHT-pygame.mouse.get_pos()[1]) , 
                  self.pos)
            cy = SETTINGS.SCALE*self.camera.render_area.bottom - (SETTINGS.HEIGHT-pygame.mouse.get_pos()[1])
            cx = pygame.mouse.get_pos()[0] + self.camera.render_area.left
            xdiff = cx - SETTINGS.SCALE * self.x
            ydiff = cy - SETTINGS.SCALE * self.y
            if (xdiff == 0):
                if (ydiff < 0):
                    angle = 270
                else:
                    angle = 90
            else:
                angle = math.degrees(math.atan((ydiff) / (xdiff)))
            if (xdiff < 0): angle += 180
            newp = Projectile.Projectile(self.projectile_image, (10,10), 
                                         (self.pos[0] + 3, self.pos[1] + 3),
                                         1, self.projectile_speed, 20, angle, self.projectile_piercing)
            self.projectile_list.append(newp)
            MusicManager.play_soundfx(self.projectile_sound, 0.5)
            self.attack_cooldown = self.attack_cooldown_max

    def button_functions(self):
        if (pygame.key.get_pressed()[pygame.K_z]):
            self.add_points(10)
            print(self.points)
        if (pygame.key.get_pressed()[pygame.K_x]):
            self.remove_points(10)
            print(self.points)
        if (pygame.key.get_pressed()[pygame.K_c]):
            self.inventory.add_item("Chocolate")
            print(self.inventory.items["Chocolate"])
        if (pygame.key.get_pressed()[pygame.K_v]):
            self.inventory.remove_item("Chocolate")

        if (pygame.key.get_pressed()[pygame.K_y]):
            self.inventory.remove_item("Item that does not exist")

        if (pygame.key.get_pressed()[pygame.K_g]):
            self.increase_health(5)
            print(self.health)
        if (pygame.key.get_pressed()[pygame.K_h]):
            self.lower_health(1)
            print(self.health)

        if (pygame.key.get_pressed()[pygame.K_b]):
            self.increase_max_health(5)
            print(self.max_health)
        if (pygame.key.get_pressed()[pygame.K_n]):
            self.lower_max_health(5)
            print(self.max_health)

        if (pygame.key.get_pressed()[pygame.K_TAB]):
            print("Points:      " , self.points)
            print("Health:      " , self.health)
            print("Max health:  " , self.max_health)
            print("Player is:   " , ["dead     (player cannot be resurrected)", "alive"][self.alive])
        if (pygame.key.get_pressed()[pygame.K_SPACE]):
            print("Items:")
            for item in self.inventory.items:
                print(item , ": " , str(self.inventory.items[item]))


class Cowboy(Player):
    def __init__(self, player_projectile_list, attack_cooldown = SETTINGS.COWBOY_ATTACK_COOLDOWN):
        super().__init__(SETTINGS.COWBOY_FOLDER, player_projectile_list, map, attack_cooldown, SETTINGS.COWBOY_SPEED)
        self.projectile_image = SETTINGS.COWBOY_FOLDER + "projectile.png"
        self.projectile_piercing = True
        self.projectile_sound = SETTINGS.COWBOY_PROJECTILE_SOUND
        self.projectile_speed = SETTINGS.COWBOY_PROJECTILE_SPEED
        self.projectile_damage = SETTINGS.COWBOY_PROJECTILE_DAMAGE

    def update(self):
        super().update()

class Ninja(Player):
    def __init__(self, player_projectile_list, attack_cooldown = SETTINGS.NINJA_ATTACK_COOLDOWN):
        super().__init__(SETTINGS.NINJA_FOLDER, player_projectile_list, map, attack_cooldown, SETTINGS.NINJA_SPEED)
        self.projectile_image = SETTINGS.NINJA_FOLDER + "projectile.png"
        self.projectile_piercing = False
        self.projectile_sound = SETTINGS.NINJA_PROJECTILE_SOUND
        self.projectile_speed = SETTINGS.NINJA_PROJECTILE_SPEED
        self.projectile_damage = SETTINGS.NINJA_PROJECTILE_DAMAGE

    def update(self):
        super().update()

def undoAxis(undo_axis:float, other_axis:float, max_dist:float) -> float:
    dist = abs(math.pow(max_dist, 2) - math.pow(other_axis, 2))
    new_move = min(math.sqrt(dist),
                undo_axis*math.copysign(1,undo_axis)) * math.copysign(1,undo_axis)
    return new_move - undo_axis