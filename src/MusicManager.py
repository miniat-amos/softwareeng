import pygame
import SETTINGS
import time

class MusicManager:

    def __init__(self):
        self.music_end = None
        self.repeat = False
        self.current_song = None
        self.standard_volume = 1

    # Play song
    def play_song(self, song, repeat, volume=1):
        if self.current_song != song:
            self.current_song = song
            self.repeat = repeat
            self.set_volume(volume)
            self.standard_volume = volume
            pygame.mixer.music.stop()
            pygame.mixer.music.load(song)

            if repeat:
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.play()

    # Play sound effect
    def play_soundfx(self, effect, volume=1):
        sound = pygame.mixer.Sound(effect)
        sound.set_volume(volume * SETTINGS.VOL_SFX)
        sound.play()

    # Set volume
    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume * SETTINGS.VOL_MUSIC)

    # Volume check
    def volume_check(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.standard_volume += .1
            elif event.key == pygame.K_DOWN:
                self.standard_volume -= .1
        self.set_volume(self.standard_volume)
