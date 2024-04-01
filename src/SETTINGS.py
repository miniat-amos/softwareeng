WIDTH = 800
HEIGHT = 720
FRAMERATE = 60


# Might not get used in the final version, I just wanted to be able to hear my music when testing lmao
VOL_SFX = .1
VOL_MUSIC = .1


# World gen settings
WR_WIDTH = 200
WR_HEIGHT = round(WR_WIDTH * (HEIGHT / WIDTH))
WR_TILE_COUNT = 8
WR_TILE_HEIGHT = 100
ENEMY_MELEE_COOLDOWN = 30
ENEMY_RANGED_COOLDOWN = 75
ENEMY_SUMMONER_COOLDOWN = 50
ENEMY_SUMMONER_ANGLE_CHANGE = 0.01

#Player settings
PLAYER_SPEED = 1

#Enemy settings
ENEMY_DEFAULT_SPEED = 1
MELEE_ENEMY_ATTACK_SOUND = "assets/sounds/entities/enemies/melee/melee_attack_hit.ogg"
INERTIA_RANGE_MIN = 0.01
INERTIA_RANGE_MAX = 0.05