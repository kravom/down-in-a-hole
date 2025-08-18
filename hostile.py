from settings import *
class Hostile:
    def __init__(self, tela, x, y, x1, y1, imag='images/padrao.png', ):
        self.enemy = pygame.Rect(x, y, x1, y1)
        self.textura_enemy = pygame.image.load(imag).convert_alpha()
        self.textura_enemy = pygame.transform.scale(self.textura_enemy, (self.enemy.width, self.enemy.height))
        tela.blit(self.textura_enemy, self.enemy.topleft)

    def draw(self, tela, camera_x, riven, death):
        tela.blit(self.textura_enemy, (self.enemy.x - camera_x, self.enemy.y))
        # Desenha debug
        pygame.draw.rect(
            tela,
            (250, 0, 0),
            (self.enemy.x - camera_x, self.enemy.y, self.enemy.width, self.enemy.height),
            2)
        if riven.rect.colliderect(self.enemy):
            death = True
            return death