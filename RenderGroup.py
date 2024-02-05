import pygame
import Camera

class Renderable():
	pass

class RenderGroup():
	def __init__(self, initialize_count):
		self.super_list: list[list[Renderable]] = []
		for i in range(0, initialize_count):
			self.super_list.append([])
		
	def addTo(self, obj: Renderable, super_index):
		if super_index in range(0, len(self.super_list)):
			self.super_list[super_index].append(obj)
	
	def render(self, screen: pygame.Surface, camera: Camera):
		for l in self.super_list:
			for rendable in l:
				screen.blit(rendable.image, camera.apply(rendable.rect))

	def clear(self, list_index = -1):
		if (list_index == -1):
			for l in self.super_list:
				l.clear()
		else:
			self.super_list[list_index].clear()


# Dummy simple class to declare something "renderable"
class Renderable():
	image = 0
	image = pygame.Surface((50, 50), pygame.SRCALPHA)
	image.fill((255, 50, 50, 127))
	
	def __init__(self):
		self.rect = pygame.Rect(0,0,0,0)

	def appendToRenderGroup(self, render_group: RenderGroup, player_rect: pygame.Rect):
		render_group.addTo(self, 0)
		pass