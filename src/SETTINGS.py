import math

### NOTE: Some values are set to 0 by default because they will be properly calculated in RECALC()

USE_DEBUG = False

# User settings (Each range 1~10)
CFG_LIGHTING_DIFFICULTY = 4
CFG_ENEMY_RATE = 4
CFG_ENEMY_STRENGTH = 4

SCORE_MULTIPLIER = 0 # Calculated from above config options


# Main settings
WIDTH = 800
HEIGHT = 720
FRAMERATE = 60


# Might not get used in the final version, I just wanted to be able to hear my music when testing lmao
VOL_SFX = 0.1
VOL_MUSIC = 0.1


# World gen settings
WR_WIDTH = 200
SCALE = WIDTH/WR_WIDTH
WR_HEIGHT = round(WR_WIDTH * (HEIGHT / WIDTH))

WR_TILE_COUNT = 8
WR_TILE_HEIGHT = 60

BUILDINGS_PER_ROOM = 0

MIN_LOOT_PER_ROOM = 5
MAX_LOOT_PER_ROOM = 5


#Player settings
COWBOY_SPEED = 1
NINJA_SPEED = 1.25
ROADRUNNER_SPEED = 1.5

COWBOY_FOLDER = "assets/sprites/entities/players/cowboy/"
NINJA_FOLDER = "assets/sprites/entities/players/ninja/"
ROADRUNNER_FOLDER = "assets/sprites/entities/players/roadrunner/"

COWBOY_PROJECTILE_SOUND = "assets/sounds/entities/players/cowboy/fire.wav"
NINJA_PROJECTILE_SOUND = "assets/sounds/entities/players/ninja/throw.mp3"
ROADRUNNER_PROJECTILE_SOUND = "assets/sounds/entities/players/roadrunner/launch.ogg"

COWBOY_HEALTH = 100
NINJA_HEALTH = 125
ROADRUNNER_HEALTH = 75

COWBOY_PROJECTILE_DAMAGE = 25
NINJA_PROJECTILE_DAMAGE = 15
ROADRUNNER_PROJECTILE_DAMAGE = 45

COWBOY_PROJECTILE_SPEED = COWBOY_SPEED + 1.0
NINJA_PROJECTILE_SPEED = NINJA_SPEED + 2.0
ROADRUNNER_PROJECTILE_SPEED = ROADRUNNER_SPEED + 1.0

COWBOY_ATTACK_COOLDOWN = 30
NINJA_ATTACK_COOLDOWN = 15
ROADRUNNER_ATTACK_COOLDOWN = 30

PLAYER_IFRAMES = int(FRAMERATE / 2)
ENEMY_IFRAMES = int(FRAMERATE / 4)


# Loot settings
LOOT_SIZE_SMALL = (8,8)
LOOT_SIZE_MEDIUM = (16,16)
LOOT_SIZE_LARGE = (16,16)

LOOT_VALUE_SMALL = 0
LOOT_VALUE_MEDIUM = 0
LOOT_VALUE_LARGE = 0

LOOT_TEXTURE_FOLDER = "assets/sprites/loot/"
COIN_PICKUP_SOUND = "assets/sounds/loot/item_pickup.wav"


#Enemy settings
ENEMY_DEFAULT_SPEED = 1
MELEE_ENEMY_ATTACK_SOUND = "assets/sounds/entities/enemies/melee/melee_attack_hit.ogg"
INERTIA_RANGE_MIN = 0.01
INERTIA_RANGE_MAX = 0.05

ENEMY_MELEE_HEALTH = 50
ENEMY_RANGED_HEALTH = 30
ENEMY_SUMMONER_HEALTH = 125

ENEMY_MELEE_ATTACK_DAMAGE = 20
ENEMY_RANGED_ATTACK_DAMAGE = 20

ENEMY_MELEE_COOLDOWN = 60
ENEMY_RANGED_COOLDOWN = 100
ENEMY_SUMMONER_COOLDOWN = 50

ENEMY_MELEE_PCT_SPAWN = 0
ENEMY_RANGED_PCT_SPAWN = 0
ENEMY_SUMMONER_PCT_SPAWN = 0
ENEMY_SPAWN_RATE = 0

SILENCE_SOUND = "assets/sounds/entities/enemies/default/silence_1sec.wav"

LIGHTNING_DEFAULT_SPEED = 0
LIGHTNING_MAX_SPEED = ROADRUNNER_SPEED + 0.4
LIGHTNING_DAMAGE = 0
LIGHTNING_SPAWN_RATE = 0
LIGHTNING_INERTIA_RANGE_MIN = 0.06
LIGHTNING_INERTIA_RANGE_MAX = 0.1

ENEMY_SUMMONER_ANGLE_CHANGE = 0.01
ENEMY_SUMMONER_CIRCLE_RADIUS = 50


# Scoreboard settings
SB_BACKGROUND_COLOR = (0,0,0,127)
HD_BACKGROUND_COLOR = (255,64,0,48)
CT_BACKGROUND_COLOR = (0,192,255,40)

SB_BORDER_COLOR = (255,255,255,255)
HD_BORDER_COLOR = (255,128,0,255)
CT_BORDER_COLOR = (0,192,255,255)

SB_TEXT_COLOR = (255,255,255)
HD_TEXT_COLOR = SB_TEXT_COLOR
CT_TEXT_COLOR = SB_TEXT_COLOR

IN_GAME = False

# Recalculate any values that may change
def RECALC():
	global SCALE, WR_HEIGHT, BUILDINGS_PER_ROOM,\
		SCORE_MULTIPLIER, LOOT_VALUE_SMALL, LOOT_VALUE_MEDIUM, LOOT_VALUE_LARGE,\
		LIGHTNING_DEFAULT_SPEED, LIGHTNING_DAMAGE, LIGHTNING_SPAWN_RATE,\
		ENEMY_MELEE_PCT_SPAWN, ENEMY_RANGED_PCT_SPAWN, ENEMY_SUMMONER_PCT_SPAWN,\
		ENEMY_MELEE_HEALTH, ENEMY_RANGED_HEALTH, ENEMY_SUMMONER_HEALTH,\
		ENEMY_SPAWN_RATE,\
		COWBOY_HEALTH, NINJA_HEALTH, ROADRUNNER_HEALTH

	if IN_GAME: return
	
	# Score multipler (NOT ALWAYS AN INT, MAKE SURE TO ROUND)
	SCORE_MULTIPLIER = round(math.sqrt(CFG_ENEMY_RATE * CFG_ENEMY_STRENGTH * CFG_LIGHTING_DIFFICULTY) * 10) / 10
	
	LOOT_VALUE_SMALL = round(1 * SCORE_MULTIPLIER)
	LOOT_VALUE_MEDIUM = round(3 * SCORE_MULTIPLIER)
	LOOT_VALUE_LARGE = round(8 * SCORE_MULTIPLIER)

	# World scale
	SCALE = WIDTH/WR_WIDTH
	WR_HEIGHT = round(WR_WIDTH * (HEIGHT / WIDTH))
 
	# Score multiplier or loot values
 
	# Lighting default settings
	LIGHTNING_DEFAULT_SPEED = math.sqrt((CFG_LIGHTING_DIFFICULTY + 5)) / 4
	LIGHTNING_DAMAGE = int(10 + 10*math.sqrt(CFG_LIGHTING_DIFFICULTY / 5))
	LIGHTNING_SPAWN_RATE = 2*FRAMERATE / math.pow(CFG_LIGHTING_DIFFICULTY, 1/3)
 
	# Rate of building spanws
	buildings_per_tile = (20 - CFG_LIGHTING_DIFFICULTY) / 10
	BUILDINGS_PER_ROOM = int(WR_TILE_COUNT * buildings_per_tile)
 
	# Rate of enemy spawns
	ENEMY_MELEE_PCT_SPAWN = (32-CFG_ENEMY_RATE) * 3 - CFG_ENEMY_STRENGTH
	ENEMY_RANGED_PCT_SPAWN = 12 + CFG_ENEMY_STRENGTH
	ENEMY_SUMMONER_PCT_SPAWN = 100-ENEMY_MELEE_PCT_SPAWN-ENEMY_RANGED_PCT_SPAWN

	ENEMY_SPAWN_RATE = FRAMERATE / math.sqrt(2*CFG_ENEMY_RATE-1)
 
	# Health of enemies/player
	enemy_health_scale = (CFG_ENEMY_STRENGTH + 4) / 8
	player_health_div = math.sqrt((CFG_ENEMY_STRENGTH + 10) / 15)

	ENEMY_MELEE_HEALTH = int(50 * enemy_health_scale)
	ENEMY_RANGED_HEALTH = int(30 * enemy_health_scale)
	ENEMY_SUMMONER_HEALTH = int(125 * enemy_health_scale)

	COWBOY_HEALTH = int(110 / player_health_div / 5) * 5
	NINJA_HEALTH = int(140 / player_health_div / 5) * 5
	ROADRUNNER_HEALTH = int(85 / player_health_div / 5) * 5

RECALC()