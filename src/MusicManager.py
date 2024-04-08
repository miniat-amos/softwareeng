import pygame
import SETTINGS
import time

class MusicManager:

    def __init__(self):
        self.music_end = None
        self.repeat = False
        self.current_song = None
        self.master_volume = 0.5
        self.soundfx_volume = 0.5
        self.music_volume = 0.5

    # Play song
    def play_song(self, song, repeat):
        if self.current_song != song:
            self.current_song = song
            self.repeat = repeat
            pygame.mixer.music.set_volume(self.master_volume * self.music_volume)
            #self.standard_volume = volume
            pygame.mixer.music.stop()
            pygame.mixer.music.load(song)

            if repeat:
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.play()

    # Play sound effect
    def play_soundfx(self, effect):
        sound = pygame.mixer.Sound(effect)
        sound.set_volume(self.master_volume * self.soundfx_volume)
        sound.play()

    # Changing the volume values
        
    def change_mastervol(self, change):
        self.master_volume += change
        self.master_volume = max(0, min(self.master_volume, 1))
        pygame.mixer.music.set_volume(self.master_volume * self.music_volume)
    
    def set_mastervol(self, change):
        self.master_volume = change
        self.master_volume = max(0, min(self.master_volume, 1))
        pygame.mixer.music.set_volume(self.master_volume * self.music_volume)

    def change_musicvol(self, change):
        self.music_volume += change
        self.music_volume = max(0, min(self.music_volume, 1))
        pygame.mixer.music.set_volume(self.master_volume * self.music_volume)

    def change_soundfxvol(self, change):
        self.soundfx_volume += change
        self.soundfx_volume = max(0, min(self.soundfx_volume, 1))
    

    # Master volume changer for mid game
    def master_volume_game_change(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.master_volume += .1
            elif event.key == pygame.K_DOWN:
                self.master_volume -= .1
        # Clamping the value
        self.master_volume = max(0, min(self.master_volume, 1))
        pygame.mixer.music.set_volume(self.master_volume * self.music_volume)
