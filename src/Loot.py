import pygame
import Renderable
import Collision
import Player
#import StaticMusicManager
from MusicManager import MusicManager

import SETTINGS

class Loot(Renderable.Renderable):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2

    def __init__(self, pos:tuple[int, int], val:int):
        self.value:int = 0
        self.folder:str = SETTINGS.LOOT_TEXTURE_FOLDER
        self.filepath:str = self.folder
        match(val):
            case(Loot.LARGE):
                self.filepath += "Block_of_Gold.png"
                size = SETTINGS.LOOT_SIZE_LARGE
                self.value = SETTINGS.LOOT_VALUE_LARGE
            case(Loot.MEDIUM):
                self.filepath += "Gold_Ingot.png"
                size = SETTINGS.LOOT_SIZE_MEDIUM
                self.value = SETTINGS.LOOT_VALUE_MEDIUM
            case _: # Default to small
                self.filepath += "Gold_Nugget.png"
                size = SETTINGS.LOOT_SIZE_SMALL
                self.value = SETTINGS.LOOT_VALUE_SMALL
        super().__init__(self.filepath, size, pos)


    # vv NOT USED -- CHECKED IN collide_loot in Map vv
    def update(self, player:Player.Player) -> bool:
        if (self.get_rect().colliderect(player.get_rect())):
            player.add_points(self.value)
            MusicManager.play_soundfx("assets/sounds/loot/item_pickup.wav")
            return True
        else: return False
