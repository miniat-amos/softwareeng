import Entity
import math
import pygame
import Player
import SETTINGS
import StaticMusicManager
import Projectile
import math
import Lightning

class Enemy(Entity.GroundEntity):
    def __init__(self, folder:str, map, size, pos, health:int, attack_damage:int, speed:float = SETTINGS.ENEMY_DEFAULT_SPEED):
        super().__init__(folder, map, size, pos, health, speed)
        self.folder = folder
        self.attack_damage:int = attack_damage
        self.attack_cooldown_max:int = SETTINGS.ENEMY_MELEE_COOLDOWN
        self.attack_cooldown:int = 0
        self.tex_offset = [-3,-6]
        self.enemy_projectile_list:list[Projectile.Projectile] = []
        self.lightning_bolt_list:list[Lightning.Lightning]

    def melee_attack(self, player:Player.Player):
        self.attack_cooldown = max(self.attack_cooldown-1, 0)
        if (self.attack_cooldown == 0):
            if (self.get_rect().colliderect(player.get_rect())) and player.alive:
                player.lower_health(self.attack_damage)
                StaticMusicManager.play_soundfx(SETTINGS.MELEE_ENEMY_ATTACK_SOUND)
                self.attack_cooldown = self.attack_cooldown_max

    def ranged_attack(self, player:Player.Player):
        self.attack_cooldown = max(self.attack_cooldown-1, 0)
        if (self.attack_cooldown == 0):
            if player.alive:
                angle = math.degrees(math.atan((player.y-self.y) / (player.x-self.x)))
                if (player.xi < self.xi): angle += 180
                newp = Projectile.Projectile("assets/sprites/entities/projectiles/bullet.png", (16,16), self.pos, 1, 1, 20,
                                             angle)
                self.enemy_projectile_list.append(newp)
                StaticMusicManager.play_soundfx("assets/sounds/entities/enemies/ranger/fire.mp3")
                self.attack_cooldown = self.attack_cooldown_max

    def summoner_attack(self, player:Player.Player):
        self.attack_cooldown = max(self.attack_cooldown-1, 0)
        if (self.attack_cooldown == 0):
            if player.alive:
                newl = Lightning.Lightning("assets/sprites/entities/enemies/lightning/",
                                (self.xi, self.yi), SETTINGS.FRAMERATE * 5)
                self.lightning_bolt_list.append(newl)
                self.attack_cooldown = self.attack_cooldown_max


    def update(self, player:Player.Player):
        if (self.alive):
            self.move(player.get_rect().center)

    def move(self, player_pos:tuple[int,int]):  #CENTER of player rect
        dx = player_pos[0] - self.get_rect().centerx
        dy = player_pos[1] - self.get_rect().centery
        distance = math.sqrt(dx * dx + dy * dy)
        if distance < 0.25: return
        checked_move = super().move((
            dx/distance * self.speed, 
            dy/distance * self.speed
        ))
        self.normalizeMove(checked_move)

class MeleeEnemy(Enemy):
    def __init__(self, folder:str, map, size, pos, health:int, attack_damage:int, speed:float = SETTINGS.ENEMY_DEFAULT_SPEED):
        super().__init__(folder, map, size, pos, health, attack_damage, speed)

    def update(self, player:Player.Player):
        if (self.alive):
            self.melee_attack(player)
            self.move(player.get_rect().center)

class RangedEnemy(Enemy):
    def __init__(self, folder:str, map, size, pos, health:int, attack_damage:int, enemy_projectile_list, speed:float = SETTINGS.ENEMY_DEFAULT_SPEED):
        super().__init__(folder, map, size, pos, health, attack_damage, speed)
        self.enemy_projectile_list = enemy_projectile_list

    def update(self, player:Player.Player):
        if (self.alive):
            self.ranged_attack(player)

class SummonerEnemy(Enemy):
    def __init__(self, folder:str, map, size, pos, health:int, attack_damage:int, lightning_bolt_list, speed:float = SETTINGS.ENEMY_DEFAULT_SPEED):
        super().__init__(folder, map, size, pos, health, attack_damage, speed)
        self.lightning_bolt_list = lightning_bolt_list
        StaticMusicManager.play_soundfx("assets/sounds/entities/enemies/summoner/spawn.mp3")

    def update(self, player:Player.Player):
        if (self.alive):
            self.summoner_attack(player)