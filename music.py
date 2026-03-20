import pygame

class MusicManager:
    current_music_file = None

    def __init__(self, music_file):
        self.music_file = music_file
        pygame.mixer.init()

    def play_music(self):
        if MusicManager.current_music_file != self.music_file:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play(-1)
            MusicManager.current_music_file = self.music_file

    def stop_music(self):
        if MusicManager.current_music_file == self.music_file:
            pygame.mixer.music.stop()
            MusicManager.current_music_file = None
