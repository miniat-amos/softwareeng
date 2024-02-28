import pygame
from Renderable import Renderable
from pygame import Rect
from pygame import Surface
import random
import Collision

#	Current risk: Buildings and porches require multiple surfaces, which may make rendering a 
# bit more complicated. Shouldn't affect hitbox-related things like collisions. Will likely need a 
# proper "Render Group" and rendering functionality. 

TILE_HEIGHT = 200 # Will depend on height of building assets later

BUILDINGS_DIRECTORY = "assets/sprites/buildings/"
BUILDING_VARIENTS = [
	"Generic_1/",
	"Pawn_Shop/"
]




def initializeSurfaces(file_list:list[str], list_fright:list[list], list_fleft:list[list]):
	list_fright.clear()
	list_fleft.clear()

	for subdir in BUILDING_VARIENTS:
		fulldir = BUILDINGS_DIRECTORY + subdir
		fright_entry = []
		fleft_entry = []

		for file in file_list:
			surface_fright = pygame.image.load(fulldir + file)
			surface_fright = pygame.transform.scale_by(surface_fright, 5) # TEMPORARY
			surface_fright = surface_fright.convert_alpha()

			fright_entry.append(surface_fright)
			fleft_entry.append(pygame.transform.flip(surface_fright, True, False))
		
		list_fright.append(fright_entry)
		list_fleft.append(fleft_entry)


class Building(Renderable, Collision.StaticCollidable):
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
		
		# Assign surface and create rect
		if (self.isEmpty):
			self.surface = Building.blank_surface
			self.rect = Rect(0,0,50,TILE_HEIGHT)
		else:
			self.roof:Renderable = Renderable()
			if facing_right:
				self.surface = Building.surfaces_face_right[type][0]
				self.roof.surface = Building.surfaces_face_right[type][1]
			else:
				self.surface = Building.surfaces_face_left[type][0]
				self.roof.surface = Building.surfaces_face_left[type][1]
			self.rect = self.surface.get_rect()
			self.roof.rect = self.roof.surface.get_rect()

		# Align rects
		if facing_right:
			self.rect.bottomleft = tile_rect.bottomleft
			if not self.isEmpty:
				self.roof.rect.bottomleft = self.rect.topleft
		else:
			self.rect.bottomright = tile_rect.bottomright
			if not self.isEmpty:
				self.roof.rect.bottomright = self.rect.topright

		self.porch = Porch(self.rect, type, facing_right)


	def initialize():
		Porch.initialize()
		initializeSurfaces(["main_base.png", "main_roof.png"], 
					Building.surfaces_face_right, Building.surfaces_face_left)
		Building.isInitialized = True

	def playerCheck(self, player_rect:Rect):
		if not self.isEmpty:
			if self.porch.rect.colliderect(player_rect):
				self.porch.hideRoof()
			else:
				self.porch.showRoof()

	def addRenderObjects(self, render_lists:list[list[Renderable]]):
		if (not self.isEmpty):
			render_lists[2].append(self)
			render_lists[4].append(self.roof)
			self.porch.addRenderObjects(render_lists)
		pass

	def collide_stop(self, object:Renderable, move:tuple[int,int]) -> tuple[int,int]:
		if self.isEmpty: return move

		move = Collision.collision_stop(self.rect, object.rect, move)
		if self.porch.burn_state > 1:
			move = Collision.collision_stop(self.porch.rect, object.rect, move)
		return move

Building.TYPE_COUNT = len(BUILDING_VARIENTS)



class Porch(Renderable):
	# Lists for building surfaces facing left & right: [(porch_base, porch_roof), (...)...]
	surfaces_face_right:list[list[Surface]] = []
	surfaces_face_left:list[list[Surface]] = []
	blank_surface = Surface((0,0), pygame.SRCALPHA)

	
	def __init__(self, building_rect:Rect, type:int, facing_right:bool) -> None:
		super().__init__()
		self.facing_right = facing_right
		self.isEmpty = (type < 0)
		self.type = type
		self.burn_state = random.randint(0,2)

		# Assign surface and create rect
		if (self.isEmpty):
			self.surface = Porch.blank_surface
			self.rect = Rect(0,0,50,TILE_HEIGHT)
		else:
			self.roof:Renderable = Renderable()
			if facing_right:
				self.surface = Porch.surfaces_face_right[type][0]
				self.roof.surface = Porch.surfaces_face_right[type][1+self.burn_state]
			else:
				self.surface = Porch.surfaces_face_left[type][0]
				self.roof.surface = Porch.surfaces_face_left[type][1+self.burn_state]
			self.rect = self.surface.get_rect()
			self.roof.rect = self.roof.surface.get_rect()
		
		if facing_right:
			self.rect.bottomleft = building_rect.bottomright
			if not self.isEmpty:
				self.roof.rect.bottomleft = self.rect.bottomleft
		else:
			self.rect.bottomright = building_rect.bottomleft
			if not self.isEmpty:
				self.roof.rect.bottomright = self.rect.bottomright
	
	def initialize():
		initializeSurfaces(["porch_base.png", "porch_roof.png", "porch_roof_charred.png", "porch_roof_burnt.png"], 
					Porch.surfaces_face_right, Porch.surfaces_face_left)

	def addRenderObjects(self, render_lists:list[list[Renderable]]):
		if not self.isEmpty:
			render_lists[2].append(self)
			render_lists[4].append(self.roof)


	def hideRoof(self):
		if not self.isEmpty:
			self.roof.surface = Porch.blank_surface
	
	def showRoof(self):
		if not self.isEmpty: 
			if self.facing_right:
				self.roof.surface = Porch.surfaces_face_right[self.type][1+self.burn_state]
			else:
				self.roof.surface = Porch.surfaces_face_left[self.type][1+self.burn_state]
