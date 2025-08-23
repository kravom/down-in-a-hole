import random
from settings import *

class Music:
    def __init__(self, music_files):
        pygame.mixer.init()
        self.music_files = music_files
        self.play_random_music()

    def play_random_music(self):
        musica_escolhida = random.choice(self.music_files)
        pygame.mixer.music.load(musica_escolhida)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()
