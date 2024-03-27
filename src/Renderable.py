import pygame

class Renderable():
	surface = pygame.Surface((50,50))
	surface.fill((255,100,100))
	
	def __init__(self, texture = 0, size = 0, pos = 0):
		if texture != 0:
			self.surface = pygame.image.load(texture)
			self.__rect = self.surface.get_rect()
			# vv Note that the rectangle's TOP LEFT is set at the given coords. It's possible this
			# vv												   could need to be changed later.
			if pos: self.__x, self.__y = pos[0], pos[1]
			else: self.__x, self.__y = 0, 0
			
			if size: self.size = size
				
			#   We could end up not needing the mask, or the mask might be better off created in the subclasses
			self.mask = pygame.mask.from_surface(self.surface)
		else:
			self.__x, self.__y = 0, 0
			self.__rect = pygame.Rect(0,0,0,0)
		
		# Equal to: (Topleft of where the texture should be drawn) - (Topleft of rect/hitbox)
		self.tex_offset = (0,0)


	# Moves without any checks of any kind. Increments x/y, recomputes rect.center
	def move(self, move:tuple[int,int]):
		self.__x += move[0]
		self.__y += move[1]
		self.__rect.center = (round(self.__x), round(self.__y))

	# If you need the get the entire rect, use *.get_rect(), but you won't be able to modify this rect
	def get_rect(self): return self.__rect.copy()
	def set_rect(self, new:pygame.Rect):
		self.__rect = new
		self.__x, self.__y  =  new.centerx, new.centery 


	# Properties and setters allow you to direction modify attributes and have it recompute related ones
	# E.g. "obj.x += 5.3" will increment obj.__x and recompute the location of obj.__rect
	#	Get/set center positon:	(*.pos, *.x, *.y) - i varients for integers
	#	Get/set edge:			(*.left, *.right, *.top, *.bottom)
	#	Get/set corner: 		(*.topleft, *.topright, *.bottomleft, *.topleft)
	#	Get/set size: 			(*.size) - Keeps the rect centered on player's x/y
			
	@property
	def pos(self): return (self.__x, self.__y)
	@pos.setter
	def pos(self, set:tuple[float,float]):
		self.__x, self.__y = set[0], set[1]
		self.__rect.center = (round(set[0]), round(set[1]))
	
	@property
	def x(self): return self.__x
	@x.setter
	def x(self, set):
		self.__x = set
		self.__rect.centerx = round(set)
	
	@property
	def y(self): return self.__y
	@y.setter
	def y(self, set):
		self.__y = set
		self.__rect.centery = round(set)
			
	@property
	def posi(self): return self.__rect.center
	@posi.setter
	def posi(self, set:tuple[int,int]): self.pos(set)
			
	@property
	def xi(self): return self.__rect.centerx
	@xi.setter
	def xi(self, set:tuple[int,int]): self.pos(set)
			
	@property
	def yi(self): return self.__rect.centery
	@yi.setter
	def yi(self, set:tuple[int,int]): self.pos(set)
	
	@property
	def size(self): return self.__rect.size
	@size.setter
	def size(self, set:tuple[int,int]):
		self.__rect.size = set
		self.__rect.center = (round(self.__x), round(self.__y))

	@property
	def left(self): return self.__rect.left
	@left.setter
	def left(self, set:int):
		self.__rect.left = set
		self.__x = self.__rect.centerx
	
	@property
	def right(self): return self.__rect.right
	@right.setter
	def right(self, set):
		self.__rect.right = set
		self.__x = self.__rect.centerx
	
	@property
	def top(self): return self.__rect.top
	@top.setter
	def top(self, set):
		self.__rect.top = set
		self.__y = self.__rect.centery
	
	@property
	def bottom(self): return self.__rect.bottom
	@bottom.setter
	def bottom(self, set):
		self.__rect.bottom = set
		self.__y = self.__rect.centery
	
	@property
	def topleft(self): return self.__rect.topleft
	@topleft.setter
	def topleft(self, set:tuple[int,int]):
		self.__rect.topleft = set
		self.__x, self.__y = self.__rect.centerx, self.__rect.centery
	
	@property
	def topright(self): return self.__rect.topright
	@topright.setter
	def topright(self, set:tuple[int,int]):
		self.__rect.topright = set
		self.__x, self.__y = self.__rect.centerx, self.__rect.centery
	
	@property
	def bottomleft(self): return self.__rect.bottomleft
	@bottomleft.setter
	def bottomleft(self, set:tuple[int,int]):
		self.__rect.bottomleft = set
		self.__x, self.__y = self.__rect.centerx, self.__rect.centery
	
	@property
	def bottomright(self): return self.__rect.bottomright
	@bottomright.setter
	def bottomright(self, set:tuple[int,int]):
		self.__rect.bottomright = set
		self.__x, self.__y = self.__rect.centerx, self.__rect.centery