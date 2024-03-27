import pygame
import SETTINGS
import Renderable
import math
import Collision
from Collision import StaticCollidable

class Entity(Renderable.Renderable):
    def __init__(self, texture, size, pos, health, speed):
        super().__init__(   texture,      size,  pos)
        #                   ^ img file                  ^ size      ^start pos
        self.speed = speed
        self.health:int = health
        self.max_health = health
        self.alive = True
        self._x:float = pos[0]
        self._y:float = pos[1]

    def lower_health(self, value:int):
        self.health -= value
        self.health = max(0,self.health)
        if (self.health == 0):
            self.alive = False

    def increase_health(self, value:int):
        self.health += value
        self.health = min(self.health, self.max_health)

    def lower_max_health(self, decrease:int):
        self.max_health -= decrease
        self.max_health = max(1, self.max_health)
        if (self.max_health < self.health):
            self.lower_health(self.health-self.max_health)

    def increase_max_health(self, increase:int):
        old_max_health = self.max_health
        self.max_health += increase
        if (old_max_health != 0):
            self.health = int(self.health * (self.max_health / old_max_health))
    def kill(self):
        self.health = 0
        self.alive = False




# For entities that walk around on the ground. 
# They can face is the 4 cardinal direcitons, and need to check collisions with the map. 
class GroundEntity(Entity):
    def __init__(self, texture_folder, map, size, pos, health, speed):
        super().__init__(texture_folder+"down.png", size, pos, health, speed)
        self.map:StaticCollidable = map
        self.texture_folder = texture_folder
        self.direction_y = "down"
    
    # Checks collisions, moves, and sets animations
    def move(self, move_dir):
        if not (move_dir[0] or move_dir[1]): return

        move = [self.speed * move_dir[0], self.speed * move_dir[1]]
        ini_rect = self.get_rect()
        ini_pos = (self.x, self.y)

        # Move without checks
        super().move(move)

        # Check movement and snap positon back as needed
        Collision.collision_oob_snap(self, (SETTINGS.WR_WIDTH, SETTINGS.WR_WIDTH))
        self.map.collide_stop(self, ini_rect)


        checked_move = (self.x-ini_pos[0], self.y-ini_pos[1])
        if (checked_move[0] and checked_move[1]):
            # If distances are similar, just shorten the distance equally
            if abs(abs(checked_move[0]) - abs(checked_move[1])) < 0.25:
                checked_dist = math.sqrt(checked_move[0]*checked_move[0]
                                     + checked_move[1]*checked_move[1])
                scalar_undo:float = min(self.speed / checked_dist, 1) - 1
                super().move((
                    checked_move[0] * scalar_undo,
                    checked_move[1] * scalar_undo
                ))
            # If X-movement is greater, adjust X-movement only
            elif abs(checked_move[1]) < abs(checked_move[0]):
                self.y += get_undo_move(checked_move[0], checked_move[1], self.speed)
            # If Y-movement is greater, adjust Y-movement only
            else:
                self.x += get_undo_move(checked_move[1], checked_move[0], self.speed)
            


        # if (move[0] != 0) and (move[1] != 0):
        #     adjusted_speed = math.sqrt((self.speed*self.speed)/2) - 1
        #     move[0] = adjusted_speed * move_dir[0]
        #     move[1] = adjusted_speed * move_dir[1]
        #     adjusted_speed = math.sqrt((self.speed*self.speed)/2)
        #     move[0] = adjusted_speed * move_dir[0]
        #     move[1] = adjusted_speed * move_dir[1]
        #   ^^ "normalizes" the movement "vector" ^^
        
        
        match(move_dir[0]):
            case(-1):
                self.surface = pygame.image.load(self.texture_folder + "left.png")
            case(1):
                self.surface = pygame.image.load(self.texture_folder + "right.png")
        match(move_dir[1]):
            case(-1):
                self.surface = pygame.image.load(self.texture_folder + "up.png")
                self.direction_y = "up"
            case(1):
                self.surface = pygame.image.load(self.texture_folder + "down.png")
                self.direction_y = "down"

        
def get_undo_move(low:float, high:float, max_dist:float) -> float:
    dist = abs(math.pow(max_dist, 2) - math.pow(low, 2))
    new_move = min(math.sqrt(dist),
                high*math.copysign(1,high)) * math.copysign(1,high)
    return new_move - high
    