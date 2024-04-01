import pygame
import math
import Entity
import Collision
import Player

class Projectile(Entity.Entity):
    def __init__(self, texture, size, pos, health, speed, damage:int, angle:float):
                                                                        #ANGLE IS IN DEGREES
        self.damage:float = damage
        super().__init__(texture, size, pos, health, speed)
        self.angle:float = angle
        self.piercing = True
        self.currently_damaging = False
        self.starting_image:pygame.Surface = self.surface
        self.tex_offset = [-3,-6]

    def update(self, player:Player.Player):
        if player.get_rect().colliderect(self.get_rect()):
            if (self.currently_damaging == False):
                player.lower_health(self.damage)
                self.currently_damaging = True
                if (self.piercing == False):
                    self.kill()
        else:
            self.currently_damaging = False
        if (self.alive):
            self.move()

    def move(self):
        self.surface = pygame.transform.rotate(self.starting_image, -self.angle)
        dx = self.speed * math.cos(math.radians(self.angle))
        dy = self.speed * math.sin(math.radians(self.angle))
        super().raw_move((dx,dy))