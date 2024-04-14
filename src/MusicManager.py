import pygame
import SETTINGS
import time

class MusicManager:
    music_end = None
    repeat = False
    current_song = None
    master_volume = 0.5
    soundfx_volume = 0.5
    music_volume = 0.5

    # Play song
    def play_song(song, repeat):
        if MusicManager.current_song != song:
            MusicManager.current_song = song
            repeat = repeat
            pygame.mixer.music.set_volume(MusicManager.master_volume * MusicManager.music_volume)
            #self.standard_volume = volume
            pygame.mixer.music.stop()
            pygame.mixer.music.load(song)

            if repeat:
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.play()

    # Play sound effect
    def play_soundfx(effect, scale:float = 1):
        sound = pygame.mixer.Sound(effect)
        sound.set_volume(MusicManager.master_volume * MusicManager.soundfx_volume * scale)
        sound.play()

    # Changing the volume values
        
    def change_mastervol(change):
        MusicManager.master_volume += change
        MusicManager.master_volume = max(0, min(MusicManager.master_volume, 1))
        pygame.mixer.music.set_volume(MusicManager.master_volume * MusicManager.music_volume)
    
    def set_mastervol(change):
        MusicManager.master_volume = change
        MusicManager.master_volume = max(0, min(MusicManager.master_volume, 1))
        pygame.mixer.music.set_volume(MusicManager.master_volume * MusicManager.music_volume)

    def change_musicvol(change):
        MusicManager.music_volume += change
        MusicManager.music_volume = max(0, min(MusicManager.music_volume, 1))
        pygame.mixer.music.set_volume(MusicManager.master_volume * MusicManager.music_volume)

    def change_soundfxvol(change):
        MusicManager.soundfx_volume += change
        MusicManager.soundfx_volume = max(0, min(MusicManager.soundfx_volume, 1))
    

    # Master volume changer for mid game
    def master_volume_game_change(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                MusicManager.master_volume += .1
            elif event.key == pygame.K_DOWN:
                MusicManager.master_volume -= .1
        # Clamping the value
        MusicManager.master_volume = max(0, min(MusicManager.master_volume, 1))
        pygame.mixer.music.set_volume(MusicManager.master_volume * MusicManager.music_volume)
