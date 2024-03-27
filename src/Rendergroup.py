import pygame
from Renderable import Renderable
from Camera import Camera

class Rendergroup():
	def __init__(self):
		self.layers:list[list[Renderable]] = []
		for i in range(0,6): self.layers.append([])
	
	def appendTo(self, item:Renderable, index:int):
		while index >= len(self.layers):
			self.layers.append([])
		self.layers[index].append(item)

	def appendGround(self, item): self.appendTo(item, 0)
	def appendOnGround(self, item): self.appendTo(item, 1)
	def appendObject(self, item): self.appendTo(item, 2)	
	def appendEntity(self, item): self.appendTo(item, 3)
	def appendRoof(self, item): self.appendTo(item, 4)
	def appendSky(self, item): self.appendTo(item, 5)
	
	def render(self, surface:pygame.Surface, camera:Camera):
		for layer in self.layers:
			for item in layer:
				surface.blit(item.surface, camera.applyTL(item))

	def clearAll(self):
		for layer in self.layers:
			layer.clear()
	
	def clearLayer(self, index:int): 
		self.layers[index].clear()
	def clearGround(self): self.layers[0].clear()
	def clearOnGround(self): self.layers[1].clear()
	def clearObjects(self): self.layers[2].clear()
	def clearEntities(self): self.layers[3].clear()
	def clearRoofs(self): self.layers[4].clear()
	def clearSky(self): self.layers[5].clear()
	def clearMapObjects(self):
		self.layers[0].clear()
		self.layers[1].clear()
		self.layers[4].clear()