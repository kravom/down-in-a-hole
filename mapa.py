from settings import *
class Mapa:
    def __init__(self, background_path):
        self.background = pygame.image.load(background_path).convert()

        wall_wid = 400
        wall_hei = 200
        self.frames_wall = [
            pygame.transform.scale(pygame.image.load(f'images/wall_ani/wall_{i}.png'), (wall_wid, wall_hei))
            for i in [1,1,2,2,3,4,5,4,3,2,2]]
        self.frame_index = 0
        self.velocidade_anim = 0.15
        self.tempo_anim = 0 
       
    def paint(self, surface):
        surface.blit(self.background, (0, 0))  # desenha no canto superior esquerdo
