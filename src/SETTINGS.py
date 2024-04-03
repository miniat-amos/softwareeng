WIDTH = 800
HEIGHT = 720
FRAMERATE = 60
LOOT_TEXTURE_FOLDER = "assets/sprites/loot/"
MIN_LOOT_PER_ROOM = 5
MAX_LOOT_PER_ROOM = 5
COIN_PICKUP_SOUND = "assets/sounds/loot/item_pickup.wav"


# Might not get used in the final version, I just wanted to be able to hear my music when testing lmao
VOL_SFX = .1
VOL_MUSIC = .1


# World gen settings
WR_WIDTH = 200
WR_HEIGHT = round(WR_WIDTH * (HEIGHT / WIDTH))
WR_TILE_COUNT = 8
WR_TILE_HEIGHT = 100
ENEMY_MELEE_COOLDOWN = 30
ENEMY_RANGED_COOLDOWN = 100
ENEMY_SUMMONER_COOLDOWN = 50
ENEMY_SUMMONER_ANGLE_CHANGE = 0.01

#Player settings
PLAYER_SPEED = 1

#Enemy settings
ENEMY_DEFAULT_SPEED = 1
MELEE_ENEMY_ATTACK_SOUND = "assets/sounds/entities/enemies/melee/melee_attack_hit.ogg"
INERTIA_RANGE_MIN = 0.01
INERTIA_RANGE_MAX = 0.05

LIGHTNING_INERTIA_RANGE_MIN = 0.1
LIGHTNING_INERTIA_RANGE_MAX = 0.2

LOOT_SIZE_SMALL = (8,8)
LOOT_SIZE_MEDIUM = (16,16)
LOOT_SIZE_LARGE = (10,10)
