import pygame
import Renderable
import Collision
import Player
import StaticMusicManager

import SETTINGS

class Loot(Renderable.Renderable):
    def __init__(self, pos:tuple[int, int], val:int):
        self.value:int = val
        self.folder:str = SETTINGS.LOOT_TEXTURE_FOLDER
        self.filepath:str = self.folder
        match(val):
            case(10):
                self.filepath += "Gold_Nugget.png"
                size = SETTINGS.LOOT_SIZE_SMALL
            case(100):
                self.filepath += "Gold_Ingot.png"
                size = SETTINGS.LOOT_SIZE_MEDIUM
            case(1000):
                self.filepath += "BlocK_Of_Gold.png"
                size = SETTINGS.LOOT_SIZE_LARGE
        super().__init__(self.filepath, size, pos)

    def update(self, player:Player.Player) -> bool:
        if (self.rect.colliderect(player.rect)):
            player.add_points(self.value)
            StaticMusicManager.play_soundfx("assets/sounds/loot/item_pickup.wav")
            return True
        else: return False