from settings import *

class Mapa:
    def __init__(self):
        self.bg_images = []
        for i in range(1, 5):
            img = pygame.image.load(f"images/back_{i}.png").convert_alpha()
            self.bg_images.append(img)
        self.bg_width = self.bg_images[0].get_width()
    def paint(self, tela, camera_x):
        for x in range(4):
            speed = 1
            for i in self.bg_images:
                tela.blit(i ,((x * self.bg_width) - camera_x * speed, 0))
                speed += 0.09