from settings import *
import pygame

class Hostile:
    def __init__(self, tela, x, y, largura, altura, imag='images/padrao.png'):
        self.enemy = pygame.Rect(x, y, largura, altura)
        self.textura_enemy = pygame.image.load(imag).convert_alpha()
        self.textura_enemy = pygame.transform.scale(self.textura_enemy, (self.enemy.width, self.enemy.height))

    def draw(self, tela, camera_x, riven):
        # Cria um retângulo temporário considerando o deslocamento da câmera
        enemy_pos = pygame.Rect(self.enemy.x - camera_x, self.enemy.y, self.enemy.width, self.enemy.height)

        # Desenha o inimigo
        tela.blit(self.textura_enemy, (enemy_pos.x, enemy_pos.y))

        # Debug da hitbox
        pygame.draw.rect(tela, (250, 0, 0), enemy_pos, 2)

        # Checa colisão
        if riven.rect.colliderect(enemy_pos):
            print('colidiu!')
            return True  # retorna True se houve colisão

        return False
