import pygame

class Player:
    def __init__(self, image):
        self.imagem = pygame.image.load(image)
        self.imagem = pygame.transform.scale(self.imagem, (50, 65))
        self.pos_x = 10
        self.pos_y = 535
        
        self.vel_max = 10
        self.vel_x = 0
        self.atrito = 0.5
        
        self.vel_y = 0
        self.gravidade = 0.5
        self.pulo_forca = -9
        
        # Variáveis para pulo variável
        self.pulo_ativo = False       # Está em fase de pulo controlado
        self.tempo_pulo_max = 10      # Frames máximos que pode continuar pulando
        self.tempo_pulo_atual = 0     # Contador de tempo do pulo atual
        
        self.no_chao = False
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 50, 65)

    def mover(self, teclas, objetos_colisao):
        # Horizontal (com deslize)
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.vel_x = -self.vel_max
        elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.vel_x = self.vel_max
        else:
            if self.vel_x > 0:
                self.vel_x -= self.atrito
                if self.vel_x < 0:
                    self.vel_x = 0
            elif self.vel_x < 0:
                self.vel_x += self.atrito
                if self.vel_x > 0:
                    self.vel_x = 0
        self.pos_x += self.vel_x
        self.rect.topleft = (self.pos_x, self.pos_y)
        for obj in objetos_colisao:
            if self.rect.colliderect(obj):
                if self.vel_x > 0:
                    self.pos_x = obj.left - self.rect.width
                elif self.vel_x < 0:
                    self.pos_x = obj.right
                self.vel_x = 0
                self.rect.topleft = (self.pos_x, self.pos_y)

        # Pulo variável - só inicia se estiver no chão
        if (teclas[pygame.K_w] or teclas[pygame.K_SPACE] or teclas[pygame.K_UP]) and self.no_chao:
            self.vel_y = self.pulo_forca
            self.no_chao = False
            self.pulo_ativo = True
            self.tempo_pulo_atual = 0
        elif self.pulo_ativo and self.tempo_pulo_atual < self.tempo_pulo_max and (teclas[pygame.K_w] or teclas[pygame.K_SPACE] or teclas[pygame.K_UP]):
            self.vel_y += -0.7  # impulso extra
            self.tempo_pulo_atual += 1
        else:
            self.pulo_ativo = False

        # Aplica gravidade normalmente
        self.vel_y += self.gravidade

        # Queda rápida quando tecla pra baixo é pressionada no ar
        if not self.no_chao and (teclas[pygame.K_s] or teclas[pygame.K_DOWN]):
            self.vel_y += 0.5  # acelera a descida

        self.pos_y += self.vel_y
        self.rect.topleft = (self.pos_x, self.pos_y)

        # Colisão vertical
        colidiu_no_chao = False
        for obj in objetos_colisao:
            if self.rect.colliderect(obj):
                if self.vel_y > 0:
                    self.pos_y = obj.top - self.rect.height
                    self.vel_y = 0
                    colidiu_no_chao = True
                    self.pulo_ativo = False  # reset pulo variável ao tocar o chão
                elif self.vel_y < 0:
                    self.pos_y = obj.bottom
                    self.vel_y = 0
                self.rect.topleft = (self.pos_x, self.pos_y)

        self.no_chao = colidiu_no_chao  # só está no chão se colidiu com algo por baixo

        if self.pos_x < 0:
            self.pos_x = 0
            self.rect.topleft = (self.pos_x, self.pos_y)
        
    def desenhar(self, tela):
        tela.blit(self.imagem, (self.pos_x, self.pos_y))
