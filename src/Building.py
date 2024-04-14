import pygame
import SETTINGS
from Renderable import Renderable
from Rendergroup import Rendergroup
from pygame import Rect
from pygame import Surface
import random
import Collision
from Player import Player

TILE_HEIGHT = SETTINGS.WR_TILE_HEIGHT

#	Current risk: Buildings and porches require multiple surfaces, which may make rendering a 
# bit more complicated. Shouldn't affect hitbox-related things like collisions. Will likely need a 
# proper "Render Group" and rendering functionality. 

# Create building assets in {BUILDINGS_DIRECTORY + [Buiding Name]} folder
# Building assets needed for a building: 
# 	- main_base.png - Should be the size of the building's footprint
# 	- main_roof.png	- The area above the main building's footprint
#	- porch_base.png - The porch that the player can stand on
#	- porch_roof.png - The roof of the porch
#	- porch_roof_charred.png - Slighting damaged varient of porch_roof.png
#	- porch_roof_burnt.png - Broken variant of porch_roof.png

BUILDINGS_DIRECTORY = "assets/sprites/buildings/"
BUILDING_VARIENTS = [
	"Generic_1/",
	"Pawn_Shop/"
]
BUILD_VAR_CNT = len(BUILDING_VARIENTS)

ROOF_ALPHA = 128 # Alpha of roofs when the player is underneath them (0~255)


# Loads all building image files into surfaces. Buildings assets and draw facing right. 
def initializeSurfacesFR(file_list:list[str], list_fright:list[list[Surface]]):
	list_fright.clear()

	for subdir in BUILDING_VARIENTS:
		fulldir = BUILDINGS_DIRECTORY + subdir
		fright_entry = []

		for file in file_list:
			surface_fright = pygame.image.load(fulldir + file)
			# surface_fright = pygame.transform.scale_by(surface_fright, 5) # TEMPORARY
			surface_fright = surface_fright.convert_alpha()
			fright_entry.append(surface_fright)

		list_fright.append(fright_entry)

# Create transparent copies of some surfaces (meant for roofs)
def appendTransparentDuplicates(surface_list:list[list[Surface]], start_index:int, alpha:int = 50):
	for entry in surface_list:
		for i in range(start_index, len(entry)):
			new_surface = entry[i].copy()
			new_surface.set_alpha(alpha)
			entry.append(new_surface)

# Create flipped copies of building surfaces and put them into the "facing_left" list
def copyFlipped(list_fright:list[list[Surface]], list_fleft:list[list[Surface]]):
	list_fleft.clear()
	for entry_fright in list_fright:
		entry_fleft = []
		for surf_fright in entry_fright:
			entry_fleft.append(pygame.transform.flip(surf_fright, True, False))
		list_fleft.append(entry_fleft)



class Building(Collision.StaticCollidable):
	# Lists for building surfaces facing left & right: [(main_base, main_roof), (...)...]
	surfaces_face_right:list[list[Surface]] = []
	surfaces_face_left:list[list[Surface]] = []
	blank_surface = Surface((0,0), pygame.SRCALPHA)
	TILE_HEIGHT = TILE_HEIGHT
	isInitialized = False
	TYPE_COUNT = -1


	def __init__(self, tile_rect:Rect, type:int, facing_right:bool) -> None:
		super().__init__()
		
		if not Building.isInitialized:
			Building.initialize()

		self.isEmpty = (type < 0)
		if type >= BUILD_VAR_CNT: 
			raise IndexError("Type %d exceeds building-type range [0~%d]" % (type, BUILD_VAR_CNT-1))
		
		# Assign surface and create rect
		if (self.isEmpty):
			self.surface = Building.blank_surface
			self.set_rect(Rect(0,0,50,TILE_HEIGHT))
		else:
			self.roof:Renderable = Renderable()
			if facing_right:
				self.surface = Building.surfaces_face_right[type][0]
				self.roof.surface = Building.surfaces_face_right[type][1]
			else:
				self.surface = Building.surfaces_face_left[type][0]
				self.roof.surface = Building.surfaces_face_left[type][1]
			self.set_rect(self.surface.get_rect())
			self.roof.set_rect(self.roof.surface.get_rect())

		# Align rects
		if facing_right:
			self.bottomleft = tile_rect.bottomleft
			if not self.isEmpty:
				self.roof.bottomleft = self.topleft
		else:
			self.bottomright = tile_rect.bottomright
			if not self.isEmpty:
				self.roof.bottomright = self.topright

		self.porch = Porch(self.get_rect(), type, facing_right)

	# Checks player-related things like roof visibility
	def playerCheck(self, player:Player):
		if not self.isEmpty:
			if self.porch.get_rect().colliderect(player.get_rect()):
				self.porch.hideRoof()
			else:
				self.porch.showRoof()

	# Fills the given render group with all building objects
	def fillRenderGroup(self, render_group:Rendergroup):
		if (not self.isEmpty):
			render_group.appendOnGround(self)
			render_group.appendRoof(self.roof)
			self.porch.fillRenderGroup(render_group)

	# Checks colision between self and another object
	def collide_stop(self, object:Renderable, inital_pos:Rect):
		if self.isEmpty: return

		Collision.collision_snap(self, object, inital_pos)

	def collision_boolean(self, object:Renderable) -> bool:
		if self.isEmpty: return False

		col = (self.get_rect().colliderect(object.get_rect()))
		#if self.porch.burn_state > 1:
			#move = Collision.collision_stop(self.porch.rect, object.rect, move)
		return col

	# Initializes building and roof surfaces
	def initialize():
		initializeSurfacesFR(["main_base.png", "main_roof.png"], 
					Building.surfaces_face_right)
		copyFlipped(Building.surfaces_face_right, Building.surfaces_face_left)
		
		Porch.initialize()
		Building.isInitialized = True
		if len(Building.surfaces_face_right) < BUILD_VAR_CNT: 
			raise IndexError("Only %d of %d building types loaded" % (len(Building.surfaces_face_left), BUILD_VAR_CNT-1))

Building.TYPE_COUNT = len(BUILDING_VARIENTS)


class Porch(Renderable):
	# Lists for building surfaces facing left & right: [(porch_base, porch_roof, porch_roof_charred...), (...), ...]
	surfaces_face_right:list[list[Surface]] = []
	surfaces_face_left:list[list[Surface]] = []
	blank_surface = Surface((0,0), pygame.SRCALPHA)

	
	def __init__(self, building_rect:Rect, type:int, facing_right:bool) -> None:
		super().__init__()
		self.facing_right = facing_right
		self.isEmpty = (type < 0)
		self.type = type
		self.burn_state = 0 #random.randint(0,2)
		self.roof_state = 1+self.burn_state
		self.roof_state_trans = self.roof_state+3

		# Assign surface and create rect
		if (self.isEmpty):
			self.surface = Porch.blank_surface
			self.set_rect(Rect(0,0,50,TILE_HEIGHT)) # Defualt (empty) rect
		else:
			self.roof:Renderable = Renderable()
			if facing_right:
				self.surface = Porch.surfaces_face_right[type][0]
				self.roof.surface = Porch.surfaces_face_right[type][self.roof_state]
			else:
				self.surface = Porch.surfaces_face_left[type][0]
				self.roof.surface = Porch.surfaces_face_left[type][self.roof_state]
			self.set_rect(self.surface.get_rect())
			self.roof.set_rect(self.roof.surface.get_rect())
		
		# Allign rects
		if facing_right:
			self.bottomleft = building_rect.bottomright
			if not self.isEmpty:
				self.roof.bottomleft = self.bottomleft
		else:
			self.bottomright = building_rect.bottomleft
			if not self.isEmpty:
				self.roof.bottomright = self.bottomright

	# Fills the given render group with porch objects
	def fillRenderGroup(self, render_group:Rendergroup):
		if not self.isEmpty:
			render_group.appendOnGround(self)
			render_group.appendRoof(self.roof)

	# Damages roof due to lighting strike - Returns true if lighting damages
	def lightingStrike(self, strike_hb:Rect) -> bool:
		if self.burn_state < 2 and self.get_rect().colliderect(strike_hb):
			self.burn_state += 1
			self.roof_state = 1+self.burn_state
			self.roof_state_trans = self.roof_state+3 # Can probably just increment all 3 instead, but eh
			return True
		else:
			return False

	# Makes roof transparent
	def hideRoof(self):
		if not self.isEmpty:
			if self.facing_right:
				self.roof.surface = Porch.surfaces_face_right[self.type][self.roof_state_trans]
			else:
				self.roof.surface = Porch.surfaces_face_left[self.type][self.roof_state_trans]
	
	# Makes roof opaque
	def showRoof(self):
		if not self.isEmpty: 
			if self.facing_right:
				self.roof.surface = Porch.surfaces_face_right[self.type][self.roof_state]
			else:
				self.roof.surface = Porch.surfaces_face_left[self.type][self.roof_state]
	
	# Initialize all porch surfaces
	def initialize():
		initializeSurfacesFR(["porch_base.png", "porch_roof.png", "porch_roof_charred.png", "porch_roof_burnt.png"],
					   Porch.surfaces_face_right)
		appendTransparentDuplicates(Porch.surfaces_face_right, 1, ROOF_ALPHA)
		copyFlipped(Porch.surfaces_face_right, Porch.surfaces_face_left)
