import pygame
import sys

pygame.init()

class Button:

    def __init__(self, x, y, img_button, img_button_hover, text, font):
        self.x = x
        self.y = y
        self.img_button = img_button
        self.img_button_hover = img_button_hover
        
        self.text = text
        self.font = font
        self.white = (255, 255, 255)
        self.yellow = (255, 236, 0)
        self.text_surface = font.render(text, True, self.white)

        # Button setup
        self.menu_button_font = pygame.font.Font(None, 48)
        #self.img_button_hover = pygame.image.load("assets/sprites/menu/Button_Hover.png")
        #self.img_button = pygame.image.load("assets/sprites/menu/Button.png")
        # Scaling button assets
        self.button_scale = .33
        self.img_button_hover = pygame.transform.scale(self.img_button_hover, (int(self.img_button_hover.get_width() * self.button_scale), int(self.img_button_hover.get_height() * self.button_scale)))
        self.img_button = pygame.transform.scale(self.img_button, (int(self.img_button.get_width() * self.button_scale), int(self.img_button.get_height() * self.button_scale)))

        self.rect = self.img_button.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen, mouse_pos):
        if self.is_clicked(mouse_pos):
            self.text_surface = self.font.render(self.text, True, self.yellow)
            self.image = self.img_button_hover
        elif not self.is_clicked(mouse_pos):
            self.text_surface = self.font.render(self.text, True, self.white)
            self.image = self.img_button
        screen.blit(self.image, self.rect)
        #screen.blit(self.text_surface, (self.x + ((240 - self.text_surface.get_width()) // 2), self.y + 27))
        screen.blit(self.text_surface, (self.x + ((self.img_button.get_rect().width - self.text_surface.get_width()) // 2), self.y + (self.img_button.get_rect().height - self.text_surface.get_height()) // 2))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

