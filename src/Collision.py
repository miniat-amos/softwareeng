import pygame
from Renderable import Renderable

#Standard (ugly) collision function using masks
def collision_stop(mask1:pygame.mask.Mask, mask2:pygame.mask.Mask,
                   mask1_coords:tuple[int,int], mask2_coords:tuple[int,int],
                   movement:tuple[int,int]):
    x_diff = mask2_coords[0] - mask1_coords[0]
    y_diff = mask2_coords[1] - mask1_coords[1]
    if (mask1.overlap(mask2, (x_diff + movement[0], y_diff))):
        movement[0] = 0
    if (mask1.overlap(mask2, (x_diff, y_diff + movement[1]))):
        movement[1] = 0
    if (mask1.overlap(mask2, (x_diff + movement[0], y_diff + movement[1]))):
        movement = (0,0)
    return movement

    # vv refined version for Renderables, you only have to send in the objects and the movement of object2
def collision_stop(obj1:Renderable, obj2:Renderable,
                   movement:tuple[int,int]):
    x_diff = obj2.left - obj1.left
    y_diff = obj2.top - obj1.top
    if (obj1.mask.overlap(obj2.mask, (x_diff + movement[0], y_diff))):
        movement[0] = 0
    if (obj1.mask.overlap(obj2.mask, (x_diff, y_diff + movement[1]))):
        movement[1] = 0
    if (obj1.mask.overlap(obj2.mask, (x_diff + movement[0], y_diff + movement[1]))):
        movement = (0,0)
    return movement

#Block going out of bounds, send in player, screen size, and player's desired movement
def collision_oob(obj1:Renderable, screen_size:tuple[int,int],
                   movement:tuple[int,int]):
    if (obj1.left + movement[0] < 0):
        movement[0] = 0 #-obj1.left
    elif (obj1.right + movement[0] >= screen_size[0]):
        movement[0] = 0 #screen_size[0] - obj1.right
    if (obj1.bottom + movement[1] > 0):
        movement[1] = 0
    #if (obj1.rect.bottom + movement[1] >= screen_size[1]):
    #    movement[1] = 0
    return movement

def collision_oob_snap(moving:Renderable, screen_size:tuple[int,int]):
    if (moving.left < 0):
        moving.left = 0
    if (moving.right >= screen_size[0]):
        moving.right = screen_size[0]
    if (moving.bottom > 0):
        moving.bottom = 0

#Rect version of collision
def collision_stop(rect1:pygame.rect.Rect, rect2:pygame.rect.Rect,
                   movement:tuple[int,int]):
    if (rect1.colliderect(rect2.move(movement[0],0))):
        movement[0] = 0
    if (rect1.colliderect(rect2.move(0,movement[1]))):
        movement[1] = 0
    #if (mask1.overlap(mask2, (x_diff, y_diff + movement[1]))):
    #    movement[1] = 0
    #if (mask1.overlap(mask2, (x_diff + movement[0], y_diff + movement[1]))):
    #    movement = (0,0)
    return movement


def collision_snap(static:Renderable, moving:Renderable, initial:pygame.Rect):
    new_pos = moving.get_rect().center
    move = (new_pos[0] - initial.centerx, new_pos[1] - initial.centery)

    # If the objects' Y bounds overlap
    if static.top < initial.top < static.bottom \
        or static.top < initial.bottom < static.bottom:
        
        if move[0]:
            # Moving left
            if move[0] < 0:
                # If started on the right side and now are overlapping
                if (initial.left >= static.right and \
                    moving.get_rect().left <= static.right):
                    moving.left = static.right
            # Moving right
            else:
                # If started on the left side and now are overlapping
                if (initial.right <= static.left and \
                    moving.get_rect().right >= static.left):
                    moving.right = static.left
    
    # If the objects' X bound overlap
    if static.left < moving.left < static.right \
        or static.left < moving.right < static.right:
        # If moving
        if move[1]:
            # Moving up
            if move[1] < 0:
                # If started underneath and now overlapping
                if (initial.top >= static.bottom and \
                    moving.get_rect().top <= static.bottom):
                    moving.top = static.bottom
            # Moving right
            else:
                # If started above and now overlapping
                if (initial.bottom <= static.top and \
                    moving.get_rect().bottom >= static.top):
                    moving.bottom = static.top


# Class for non-moving objects that are collidable
# Needed to prevent circular imports between Player and Map
class StaticCollidable(Renderable):
    def collide_stop(self, object:Renderable, move:tuple[int,int]) -> tuple[int,int]:
        pass