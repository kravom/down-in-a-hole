from settings import *

class Music:
    def __init__(self, music_file):
        # Carregar música de fundo
        pygame.mixer.init()
        self.music_file = music_file
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.set_volume(0.5)  # Ajustar volume
        pygame.mixer.music.play(-1)  # Reproduzir em loop
    def stop_music(self):
        pygame.mixer.music.stop()