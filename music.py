import pygame

class MusicManager:
    def __init__(self, music_file):
        self.music_file = music_file
        pygame.mixer.init()  # Initialize the mixer

    def play_music(self):
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play(-1)  # Loop forever

    def stop_music(self):
        pygame.mixer.music.stop()
