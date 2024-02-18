import pygame
from pygame import Rect

#	Lower indecies for a tile or room list will always mean "earlier" components.
# I.e. if the player is moving forward, they will enter room[0], then room[1], etc.
# Consequently, higher indices mean lower (more negative) y-values. 


# 	This program uses standard pyton conventions, where a double-underscore indicates a private
# attribute / method, and single-underscore indicates protected. 
# 	This may change if it makes things less readable. 

TILE_HEIGHT = 20 # Will depend on height of building assets later
TILES_PER_ROOM = 5
ROOM_HEIGHT = TILE_HEIGHT * TILES_PER_ROOM



# TEMPORARY player class
class Player():
	def __init__(self):
		self.rect = Rect(0,0,20,20)
		
# TEMPORARY generic object class, just for testing/debugging
class Obj():
	def __init__(self, name, pos:tuple[int,int] = 0):
		self.name = name
		self.rect = Rect(0,0,5,5)
		if pos:
			self.rect.center = pos

	def __str__(self) -> str:
		return "*"



class Map():
	# Takes parameters: map width, player, active area, inactive (but loaded) area
	def __init__(self, width:int, player_to_follow: Player, max_active_rooms:int = 4, max_inactive_rooms:int = 12) -> None:
		self.__WIDTH = width
		
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
		self.player = player_to_follow
		player_start_y = 0 #(TILES_PER_ROOM * TILE_HEIGHT) // 2
		self.player.rect.centery = player_start_y

		# Generate all initial rooms
		for i in range(0, max_active_rooms):
			self.__addARoom()


	# Adds a room to self.__room_list, removes a room if the limit is reached
	def __addARoom(self) -> None:
		# Generate room
		self.__room_gen_count += 1
		self.__room_list.append(Room(self.__WIDTH, -ROOM_HEIGHT*self.__room_gen_count, self.__room_gen_count-1))
		# Delete room if list is too long (to save on memory ig)
		if (len(self.__room_list) > self.__MAX_ROOM_COUNT):
			self.__room_list.pop(0)
			self.__active_start_index -= 1


	# Tick functions are run every frame and have no parameters
	def tick(self) -> None:
		self.updateActiveRange()

		for i in range(self.__active_start_index, self.__active_start_index + self.__ACTIVE_ROOM_COUNT):
			room = self.__room_list[i]
			room.tick()
	
	# Updates self.__active_start_index, which determines the range of rooms considered active
	def updateActiveRange(self) -> None:
		p_room_index = self.getPlayerRoomIndex()
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
	def getPlayerRoomIndex(self) -> int:
		first_room_start_y = self.__room_list[0].rect.bottom
		return (first_room_start_y-self.player.rect.centery) // ROOM_HEIGHT

	# Returns a rect that contains the entire active area of the map
	def getActiveArea(self) -> Rect:
		lowest_room = self.__room_list[0]
		highest_room = self.__room_list[self.__active_start_index + self.__ACTIVE_ROOM_COUNT + 1]
		
		left = 0
		top = highest_room.rect.top
		width = self.__WIDTH
		height = top - lowest_room.rect.bottom
		
		return Rect(left, top, width, height)

	# Returns the rect of the room the player is approaching
	def getApproachingArea(self) -> Rect:
		approaching_room = self.__room_list[self.__active_start_index + self.__ACTIVE_ROOM_COUNT + 1]
		return approaching_room.rect

	# String conversion used for debugging when rendering can't be done
	def __str__(self) -> str:
		string:str = "\nActive Rooms:\n"
		for i in range(self.__active_start_index, self.__active_start_index + self.__ACTIVE_ROOM_COUNT):
			room = self.__room_list[i]
			string += room.__str__() + "\n"
		string += "Player in %d (%d, %d)" % (self.getPlayerRoomIndex(), self.player.rect.centerx,  self.player.rect.centery)
		return string

	# Spawns the object at the player's current position
	def spawnObjAtPlayer(self, obj:Obj):
		obj.rect.center = self.player.rect.center
		room = self.__room_list[self.getPlayerRoomIndex()]
		room.addObj(obj)


class Room():
	# Parameters: room width, position (top y-value), tile count, tile height
	def __init__(self, width:int, top_y:int, id:int, tile_count:int = TILES_PER_ROOM, tile_height:int = TILE_HEIGHT) -> None:
		self.__WIDTH = width
		self.ID = id # Mostly used for debugging
		
		# Define position and size of room
		self.rect = Rect(0, top_y, width, tile_height * tile_count)

		self.tile_list:list[Tile] = []

		tile_y = self.rect.bottom
		for i in range(0, tile_count):
			tile_y -= TILE_HEIGHT
			tile = Tile(self.__WIDTH, tile_y)
			self.tile_list.append(tile)
			pass
	
	# Tick functions are run every frame and have no parameters
	def tick(self):
		pass

	def __str__(self) -> str:
		string = "ID: %d (y : %d ~ %d)" % (self.ID, self.rect.bottom, self.rect.top)
		for tile in self.tile_list:
			string += "\n\t" + tile.__str__()
		return string

	# Returns the tile that collides with the center of the given rectangle
	def getTileIndexAtLoc(self, rect:Rect):
		return (self.rect.bottom-rect.centery) // TILE_HEIGHT
	

	# Adds the given object to the tile that matches its position
	def addObj(self, obj:Obj):
		tile = self.tile_list[self.getTileIndexAtLoc(obj.rect)]
		tile.addObj(obj)


class Tile():
	def __init__(self, width:int, top_y:int):
		self.rect = Rect(0, top_y, width, TILE_HEIGHT)
		self.obj_list:list[Obj] = []
	
	def addObj(self, obj:Obj):
		self.obj_list.append(obj)
	
	def __str__(self) -> str:
		string = "(y : %d ~ %d) [" % (self.rect.bottom, self.rect.top)
		for obj in self.obj_list:
			string += obj.__str__()
		string += "]"
		return string