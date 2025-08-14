from settings import *

class Mapa:
    def __init__(self, background_path):
        self.background = pygame.image.load(background_path).convert()
    def paint(self, surface):
        surface.blit(self.background, (0, 0))  # desenha no canto superior esquerd
    

