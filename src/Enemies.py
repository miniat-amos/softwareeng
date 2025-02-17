import Entity
import math
import pygame
import Player
import SETTINGS
#import StaticMusicManager
import Projectile
import math
import Lightning
import random
from MusicManager import MusicManager

class Enemy(Entity.GroundEntity):
    def __init__(self, folder:str, map, size, pos, health:int, attack_damage:int, speed:float, attack_cooldown:int):
        super().__init__(folder, map, size, pos, health, speed)
        self.folder = folder
        self.attack_damage:int = attack_damage
        self.attack_cooldown_max:int = attack_cooldown
        self.attack_cooldown:int = 0
        self.tex_offset = [-3,-6]
        self.enemy_projectile_list:list[Projectile.Projectile] = []
        self.lightning_bolt_list:list[Lightning.Lightning]
        self.iframes_max = SETTINGS.ENEMY_IFRAMES

    def melee_attack(self, player:Player.Player):
        self.attack_cooldown = max(self.attack_cooldown-1, 0)
        if (self.attack_cooldown == 0):
            if (self.get_rect().colliderect(player.get_rect())) and player.alive:
                player.damage(self.attack_damage)
                MusicManager.play_soundfx(SETTINGS.MELEE_ENEMY_ATTACK_SOUND, 1.5)
                self.attack_cooldown = self.attack_cooldown_max

    def ranged_attack(self, player:Player.Player):
        self.attack_cooldown = max(self.attack_cooldown-1, 0)
        if (self.attack_cooldown == 0):
            if player.alive:
                xdiff = player.x - self.x
                ydiff = player.y - self.y
                if (xdiff == 0):
                    if (ydiff < 0):
                        angle = 270
                    else:
                        angle = 90
                else:
                    angle = math.degrees(math.atan((player.y-self.y) / (xdiff)))
                if (xdiff < 0): angle += 180
                newp = Projectile.Projectile("assets/sprites/entities/projectiles/bullet.png", (16,16), self.pos, 1, 1.5, self.attack_damage,
                                             angle)
                newp.tex_offset = (0,0)
                self.enemy_projectile_list.append(newp)
                MusicManager.play_soundfx("assets/sounds/entities/enemies/ranger/fire.wav")
                self.attack_cooldown = self.attack_cooldown_max

    def summoner_attack(self, player:Player.Player):
        self.attack_cooldown = max(self.attack_cooldown-1, 0)
        if (self.attack_cooldown == 0):
            if player.alive:
                newl = Lightning.Lightning("assets/sprites/entities/enemies/lightning/",
                                (self.xi, self.yi))
                self.lightning_bolt_list.append(newl)
                self.attack_cooldown = self.attack_cooldown_max


    def update(self):
        super().update()

class MeleeEnemy(Enemy):
    def __init__(self, folder:str, map, size, pos):
        super().__init__(folder, map, size, pos, SETTINGS.ENEMY_MELEE_HEALTH, SETTINGS.ENEMY_MELEE_ATTACK_DAMAGE, 
                        SETTINGS.ENEMY_DEFAULT_SPEED, SETTINGS.ENEMY_MELEE_COOLDOWN)
        self.last_move:tuple[float,float] = [0,0]
        self.damage_sound = "assets/sounds/entities/enemies/melee/damage.wav"
        self.death_sound = "assets/sounds/entities/enemies/melee/death.mp3"

    def update(self, player:Player.Player):
        if (self.alive):
            self.melee_attack(player)
            self.move(player.pos)
        super().update()
        
    def move(self, player_pos:tuple[int,int]):  #CENTER of player rect
        dx = player_pos[0] - self.get_rect().centerx
        dy = player_pos[1] - self.get_rect().centery
        distance = math.sqrt(dx * dx + dy * dy)
        if distance < 0.01: return # Prevent division by zero errors
        inertia:float = random.uniform(SETTINGS.INERTIA_RANGE_MIN, SETTINGS.INERTIA_RANGE_MAX)
        x_move = dx/distance * self.speed
        x_move = (x_move * inertia + self.last_move[0]*(1-inertia))#/2
        y_move = dy/distance * self.speed
        y_move = (y_move * inertia + self.last_move[1]*(1-inertia))#/2
        checked_move = super().move((
            x_move, y_move
        ))
        self.last_move = checked_move
        self.normalizeMove(checked_move)

class RangedEnemy(Enemy):
    def __init__(self, folder:str, map, size, pos, enemy_projectile_list):
        super().__init__(folder, map, size, pos, SETTINGS.ENEMY_RANGED_HEALTH, SETTINGS.ENEMY_RANGED_ATTACK_DAMAGE, 
                        SETTINGS.ENEMY_DEFAULT_SPEED, SETTINGS.ENEMY_RANGED_COOLDOWN)
        self.enemy_projectile_list = enemy_projectile_list
        self.damage_sound = "assets/sounds/entities/enemies/ranger/damage.mp3"
        self.death_sound = "assets/sounds/entities/enemies/ranger/death.mp3"

    def update(self, player:Player.Player):
        if (self.alive and (abs(player.yi-self.yi) < SETTINGS.WR_HEIGHT)):
            self.ranged_attack(player)
            self.turn(player)
        super().update()

    def turn(self, player:Player.Player):
        xch = player.xi - self.xi
        ych = player.yi - self.yi
        if abs(xch) > abs(ych):
            if (xch > 0):
                self.surface = pygame.image.load(self.folder + "right.png")
            else:
                self.surface = pygame.image.load(self.folder + "left.png")
        else:
            if (ych > 0):
                self.surface = pygame.image.load(self.folder + "down.png")
            else:
                self.surface = pygame.image.load(self.folder + "up.png")


class SummonerEnemy(Enemy):
    def __init__(self, folder:str, map, size, pos, lightning_bolt_list):
        super().__init__(folder, map, size, pos, SETTINGS.ENEMY_SUMMONER_HEALTH, 0, 
                        SETTINGS.ENEMY_DEFAULT_SPEED, SETTINGS.ENEMY_SUMMONER_COOLDOWN)
        self.lightning_bolt_list = lightning_bolt_list
        MusicManager.play_soundfx("assets/sounds/entities/enemies/summoner/spawn.wav", 0.75)
        self.angle:float = math.radians(random.randrange(0,359, 1))
        self.starting_pos = pos
        self.damage_sound = "assets/sounds/entities/enemies/summoner/damage.mp3"
        self.death_sound = "assets/sounds/entities/enemies/summoner/death.mp3"
        self.attack_cooldown = self.attack_cooldown_max

    def update(self, player:Player.Player):
        if (self.alive):
            self.angle += SETTINGS.ENEMY_SUMMONER_ANGLE_CHANGE
            if (abs(player.yi-self.yi) < (SETTINGS.WR_HEIGHT)):
                self.summoner_attack(player)
            self.move()
        super().update()

    def move(self):
        self.x = (SETTINGS.ENEMY_SUMMONER_CIRCLE_RADIUS*math.cos(self.angle) + self.starting_pos[0])
        self.y = (SETTINGS.ENEMY_SUMMONER_CIRCLE_RADIUS*math.sin(self.angle) + self.starting_pos[1])