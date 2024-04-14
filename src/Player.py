import pygame
import Entity
import Inventory
import SETTINGS
import math

class Player(Entity.GroundEntity):# pygame.sprite.Sprite):
    def __init__(self, texture_folder:str, map = 0):
        super().__init__(   texture_folder, map,    (10,10),  (400,400),  100,    SETTINGS.PLAYER_SPEED)
        
        self.points = 0 #probably best to store points/money directly, rather than in inventory
        self.inventory = Inventory.Inventory()
        self.build = 0
        self.tex_offset = (-3,-6)
    
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
            self.move()

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


def undoAxis(undo_axis:float, other_axis:float, max_dist:float) -> float:
    dist = abs(math.pow(max_dist, 2) - math.pow(other_axis, 2))
    new_move = min(math.sqrt(dist),
                undo_axis*math.copysign(1,undo_axis)) * math.copysign(1,undo_axis)
    return new_move - undo_axis