import pygame
from Renderable import Renderable

class Camera:
    def __init__(self, target:Renderable, width, height):
        self.target = target
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, width, height)

    def apply(self, target_rect:pygame.Rect) -> pygame.Rect:
        return target_rect.move(self.rect.topleft)

    # Returns the positon of where the topleft of the texture should be drawn
    def applyTL(self, target:Renderable) -> tuple[int,int]:
        draw_x = target.left + target.tex_offset[0] + self.rect.left
        draw_y = target.top + target.tex_offset[1] + self.rect.top
        return (draw_x, draw_y)

    def update(self):
        x = 0
        y = max(-self.target.yi + self.height // 2, self.height)
        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.render_area = self.rect.copy()
        self.render_area.centery = -y + (self.rect.height/2)