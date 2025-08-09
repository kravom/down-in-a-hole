import pygame
from player import Player
from mapa import Mapa

pygame.init()

# configuração de tela
tela = pygame.display.set_mode((1000, 700), pygame.RESIZABLE)
pygame.display.set_caption('Down In A Hole')
relogio = pygame.time.Clock()
# Cria o jogador
riven = Player()
# define o png fundo
mapa = Mapa('images/background.png')

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    teclas = pygame.key.get_pressed()

    mapa.paint(tela) 

    # Cor: marrom escuro
    cor_chao = (139, 69, 19)
    # Desenha o chão
    plat1 = pygame.draw.rect(tela, cor_chao, (0, 600, 100, 250))  # chão com altura de 100px
    
    plat2 = pygame.draw.rect(tela, cor_chao, (200, 300, 100, 250))  # chão com altura de 100px
    
    # Lista de objetos para colisão
    objetos_colisao = [ plat1, plat2 ]

    # Move o personagem considerando colisão
    riven.mover(teclas, objetos_colisao)
   
    # Desenha o personagem
    riven.desenhar(tela)

    # Desenha hitbox do personagem
    pygame.draw.rect(tela, (255, 0, 0), riven.rect, 2)

    print(f"Y = {riven.pos_y}")
    print(f"X = {riven.pos_x}")

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
