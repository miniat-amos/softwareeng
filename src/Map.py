import pygame
import SETTINGS
from pygame import Rect
from Building import Building

from Renderable import Renderable
from Rendergroup import Rendergroup

from Collision import StaticCollidable
from Camera import Camera
import random
from Player import Player

#	Lower indecies for a tile or room list will always mean "earlier" components.
# I.e. if the player is moving forward, they will enter room[0], then room[1], etc.
# Consequently, higher indices mean lower (more negative) y-values. 

# 	This program uses standard pyton conventions, where a double-underscore indicates a private
# attribute / method, and single-underscore indicates protected. 
# 	This may change if it makes things less readable. 

# Major Functions
# 	- playerCheck(player):
#		Performs any checks based on the players location
#		Currently hides roofs, may pick up loot and damage player if they're somewhere dangerous
#	- fillRenderGroup(render_group):
#		Adds all renderable map objects to the given render group.
#		A.fillRenferGroup() will add A to the group, then call the function on its sub-components
#	- collide_stop(moving_obj, move):
#		Checks collisions using Collision.collision_stop()
#		Works identically to the aformentioned function, but checks collisions with all sub-components too

TILE_HEIGHT = SETTINGS.WR_TILE_HEIGHT
TILES_PER_ROOM = SETTINGS.WR_TILE_COUNT
ROOM_HEIGHT = TILE_HEIGHT * TILES_PER_ROOM
WIDTH = SETTINGS.WR_WIDTH



class Map(StaticCollidable):
	# Takes parameters: player, active area, inactive (but loaded) area
	def __init__(self, camera:Camera, render_group:Rendergroup, max_active_rooms:int = 4, max_inactive_rooms:int = 12) -> None:
		self.render_group = render_group
		self.camera = camera
		self.render_area:Rect = Rect(0, 0, camera.rect.width, camera.rect.height + 2*TILE_HEIGHT)
		
		# Total number of rooms that have been generated
		self.__room_gen_count:int = 0

		self.__room_list:list[Room] = []
		self.__MAX_ROOM_COUNT = max_active_rooms + max_inactive_rooms

		# Active rooms are rooms that will be updated regularly and checked for interactions later on
		self.__ACTIVE_ROOM_COUNT = max(max_active_rooms, 4)
		self.__active_start_index = 0 # Indicies from (this) to (this + __ACTIVE_ROOM_COUNT) will be active
		
		# Not the exact center, but used to decide when to change the active range of rooms
		self.__ACTIVE_CENTER_OFFSET = self.__ACTIVE_ROOM_COUNT // 2
		
		# Player positioning
		start_y = -ROOM_HEIGHT // 2#(TILES_PER_ROOM * TILE_HEIGHT) // 2
		start_x = WIDTH // 2
		self.start_pos = (start_x, start_y)

		# Generate all initial rooms
		for i in range(0, max_active_rooms):
			self.__addARoom()

	# Sets the position of the object to the map's start pos
	def setStartPosOf(self, object:Renderable): object.pos = self.start_pos

	# Adds a room to self.__room_list, removes a room if the limit is reached
	def __addARoom(self) -> None:
		# Generate room
		self.__room_gen_count += 1
		self.__room_list.append(Room(-ROOM_HEIGHT*self.__room_gen_count, self.__room_gen_count-1))
		# Delete room if list is too long (to save on memory ig)
		if (len(self.__room_list) > self.__MAX_ROOM_COUNT):
			self.__room_list.pop(0)
			self.__active_start_index -= 1

	def getRoom(self, index:int):
		return self.__room_list[index]


	# Tick functions are run every frame and have no parameters
	def tick(self) -> None:
		self.updateActiveRange()
		for i in range(self.__active_start_index, self.__active_start_index + self.__ACTIVE_ROOM_COUNT):
			room = self.__room_list[i]
			room.tick()
	
	# Updates self.__active_start_index, which determines the range of rooms considered active
	def updateActiveRange(self) -> None:
		p_room_index = self.getCameraRoomIndex()
		active_center = self.__active_start_index + self.__ACTIVE_CENTER_OFFSET

		# If player is below the active center, shift active range down
		if (p_room_index < active_center-1):
			if self.__active_start_index > 0:
				self.__active_start_index -= 1
		
		# If player is above the active center, shift active range up
		elif (p_room_index > active_center):
			self.__active_start_index += 1
			last_active_index = self.__active_start_index + self.__ACTIVE_ROOM_COUNT
			# If the active range extends past the number of rooms
			if last_active_index > len(self.__room_list):
				self.__addARoom()
	
	# Returns the index of the room that the player is in
	def getCameraRoomIndex(self) -> int:
		first_room_start_y = self.__room_list[0].bottom
		index = (first_room_start_y-self.camera.target.y) // ROOM_HEIGHT
		if (index < 0): return 0
		if (index > len(self.__room_list)): return len(self.__room_list) - 1
		return index
	
		# Returns the index of the room that the player is in
	def getRectRoomIndex(self, rect:pygame.Rect) -> int:
		first_room_start_y = self.__room_list[0].bottom
		index = (first_room_start_y-rect.centery) // ROOM_HEIGHT
		if (index < 0): return 0
		if (index > len(self.__room_list)): return len(self.__room_list) - 1
		return index

	# Returns a rect that contains the entire active area of the map
	def getActiveArea(self) -> Rect:
		lowest_room = self.__room_list[0]
		highest_room = self.__room_list[self.__active_start_index + self.__ACTIVE_ROOM_COUNT + 1]
		
		left = 0
		top = highest_room.top
		width = WIDTH
		height = top - lowest_room.bottom
		return Rect(left, top, width, height)

	# Returns the rect of the room the player is approaching
	def getApproachingArea(self) -> Rect:
		approaching_room = self.__room_list[self.__active_start_index + self.__ACTIVE_ROOM_COUNT + 1]
		return approaching_room.get_rect()

	# Fills the given render group with all map objects
	def fillRendergroup(self, render_group:Rendergroup = 0):
		if render_group == 0: render_group = self.render_group
		
		render_group.clearMapObjects()

		self.render_area.centery = self.camera.target.y + TILE_HEIGHT
		if (self.render_area.bottom > 0):
			self.render_area.bottom = 0

		for i in range(self.__active_start_index+self.__ACTIVE_ROOM_COUNT-1, self.__active_start_index-1, -1):
			room = self.__room_list[i]
			if room.get_rect().colliderect(self.render_area):
				room.fillRenderGroup(render_group, self.render_area)
	
	# Checks collision with all relevant map objects and returns new movement vector
	def collide_stop(self, moving_object:Renderable, initial_pos:Rect) -> tuple[int,int]:
		for i in range(self.__active_start_index, self.__active_start_index + self.__ACTIVE_ROOM_COUNT):
			room = self.__room_list[i]
			room.collide_stop(moving_object, initial_pos)
	
	def getWidth(self):
		return WIDTH
	
	# Checks player-related things. For now, just hiding roofs if the player is under them
	def playerCheck(self, player:Player):
		for i in range(self.__active_start_index, self.__active_start_index + self.__ACTIVE_ROOM_COUNT):
			room = self.__room_list[i]
			room.playerCheck(player)

	# String conversion used for debugging when rendering can't be done
	def __str__(self) -> str:
		string:str = "\nActive Rooms:\n"
		for i in range(self.__active_start_index, self.__active_start_index + self.__ACTIVE_ROOM_COUNT):
			room = self.__room_list[i]
			string += room.__str__() + "\n"
		player_pos = self.camera.target.get_rect()
		string += "Player in %d (%d, %d)" % (self.getCameraRoomIndex(), player_pos.centerx, player_pos.centery)
		return string

	# Returns some stats about the map
	def getStats(self) -> str:
		string = ""
		player_room_number = self.__room_gen_count - (len(self.__room_list) - self.getCameraRoomIndex())
		topleft = self.__room_list[len(self.__room_list) - 1].topleft
		bottomright = self.__room_list[0].bottomright
		string += "Player room number = %d\n" % (player_room_number)
		string += "Total rooms generated = %d\n" % (self.__room_gen_count)
		player = self.camera.target
		string += "Player position (x,y) = (%d,%d)\n" % (player.get_rect().centerx, player.get_rect().centery)
		camera_pos = self.camera.rect
		string += "Camera position (x,y) = (%d,%d)\n" % (camera_pos.centerx, camera_pos.centery)
		string += "Map coordniate range (topleft) ~ (bottomright) = (%d,%d) ~ (%d,%d)"\
			% (topleft[0], topleft[1], bottomright[0], bottomright[1])
		return string


class Room(StaticCollidable):
	surface = pygame.Surface((WIDTH, 1))
	surface.fill((200,200,200))

	# Parameters: room width, position (top y-value), tile count, tile height
	def __init__(self, top_y:int, id:int, tile_count:int = TILES_PER_ROOM, tile_height:int = TILE_HEIGHT) -> None:
		super().__init__()
		self.ID = id # Mostly used for debugging
		
		# Define position and size of room
		self.set_rect(Rect(0, top_y, WIDTH, tile_height * tile_count))

		self.tile_list:list[Tile] = []

		tile_y = self.bottom
		for i in range(0, tile_count):
			tile_y -= TILE_HEIGHT
			tile = Tile(tile_y)
			self.tile_list.append(tile)
			pass
	
	# Tick functions are run every frame and have no parameters
	def tick(self):
		pass

	# Returns the tile that collides with the center of the given rectangle
	def getTileIndexAtLoc(self, rect:Rect):
		index = (self.bottom-rect.centery) // TILE_HEIGHT
		if (index < 0): return 0
		if (index > len(self.tile_list)): return len(self.tile_list)-1
		return index
	
	# Fills the given render group with all objects in the room
	def fillRenderGroup(self, render_group:Rendergroup, render_area:Rect):
		for i in range(len(self.tile_list)-1, -1, -1):
			tile = self.tile_list[i]
			if render_area.colliderect(tile.get_rect()):
				tile.fillRenderGroup(render_group)
		render_group.appendGround(self)
	
	# Checks player-related things like roof visibility
	def playerCheck(self, player:Player):
		for tile in self.tile_list:
			# REMEBER: rect.top < rect.bottom because higher ==> more negative
			if tile.bottom + TILE_HEIGHT > player.bottom \
				or tile.top - TILE_HEIGHT < player.bottom:
				tile.playerCheck(player)

	# Checks collision with all relevant map objects and returns new movement vector
	def collide_stop(self, moving_object:Renderable, initial_pos:Rect) -> tuple[int,int]:
		for tile in self.tile_list:
			# REMEBER: rect.top < rect.bottom because higher ==> more negative
			if tile.bottom + TILE_HEIGHT > moving_object.bottom \
				or tile.top - TILE_HEIGHT < moving_object.bottom:
				tile.collide_stop(moving_object, initial_pos)

	# Returns string with info about the room
	def __str__(self) -> str:
		string = "ID: %d (y : %d ~ %d)" % (self.ID, self.bottom, self.top)
		for tile in self.tile_list:
			string += "\n\t" + tile.__str__()
		return string


class Tile(StaticCollidable):
	surface = pygame.Surface((WIDTH, TILE_HEIGHT))
	surface.fill((100, 50, 10))
	pygame.draw.line(surface, (0,0,0), surface.get_rect().topleft, surface.get_rect().topright)

	def __init__(self, top_y:int):
		super().__init__()
		self.set_rect(Rect(0, top_y, WIDTH, TILE_HEIGHT))

		self.building_left = Building(self.get_rect(), random.randint(-1, Building.TYPE_COUNT-1), True)
		self.building_right = Building(self.get_rect(), random.randint(-1, Building.TYPE_COUNT-1), False)

	# Fills render group with all tile objects
	def fillRenderGroup(self, render_group:Rendergroup):
		render_group.appendGround(self)
		self.building_left.fillRenderGroup(render_group)
		self.building_right.fillRenderGroup(render_group)

	# Checks palyer-related things like roof visibility
	def playerCheck(self, player:Player):
		self.building_left.playerCheck(player)
		self.building_right.playerCheck(player)

	# Checks collisions between player and tile objects
	def collide_stop(self, moving_object:Renderable, initial_pos:Rect) -> tuple[int,int]:
		self.building_left.collide_stop(moving_object, initial_pos)
		self.building_right.collide_stop(moving_object, initial_pos)

	# Returns string with information about the tile
	def __str__(self) -> str:
		string = "(y : %d ~ %d) [" % (self.bottom, self.top)
		string += "]"
		return string