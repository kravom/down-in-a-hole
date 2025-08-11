from player import Player
from mapa import Mapa
from settings import *

pygame.init()

    # configuração principal
    #tela
tela = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    #nome da janela
pygame.display.set_caption('Down In A Hole')
    #Para definir fps
relogio = pygame.time.Clock()
    #Morte
death = False

    # Cria o jogador
riven = Player()
    #png riven morto
riven_dead = pygame.image.load('images/player_dead.png').convert_alpha() #<-- faz a variavel em uma surface
riven_dead = pygame.transform.scale(riven_dead, (200, 215))
    # define o png fundo
map = Mapa('images/background.png')
    # fundo preto de morte
screen_death = Mapa('images/screen_death.png')


executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    teclas = pygame.key.get_pressed()
    # para funcionar a morte 
    if death:
        #mensagem de morte e o jogo "pausa"
        screen_death.paint(tela)
        #png riven
        tela.blit(riven_dead, ((WINDOW_WIDTH // 2+40), (WINDOW_HEIGHT // 2+100)))
        font = pygame.font.Font(None, 100)  # Cria a fonte
        text = font.render("GAME-OVER", True, (139, 0, 0))  # Renderiza o texto
        text2 = font.render("Pressione R para continuar", True, (139, 0, 0))
        tela.blit(text, ((WINDOW_WIDTH // 2-100), (WINDOW_HEIGHT // 2-100)))  # Desenha na tela
        tela.blit(text2, ((WINDOW_WIDTH // 2-300), (WINDOW_HEIGHT // 2-30)))
        relogio.tick(10)
        pygame.display.flip()
        #R retorna o jogo após a morte
        if teclas[pygame.K_r]:
            death = False
            riven.pos_x = 10
            riven.pos_y = 535
            riven.rect.topleft = (riven.pos_x, riven.pos_y)
            riven.vel_x = 0
            riven.vel_y = 0
            riven.no_chao = False
            riven.pulo_ativo = False
            riven.tempo_pulo_atual = 0
    else:
        tela.fill((0, 0, 0))
        map.paint(tela) 
        # Cor: marrom escuro
        cor_chao = (139, 69, 19)
        # Desenha o chão
        teto1 = pygame.draw.rect(tela, cor_chao, (200, 250, 600, 150))
        plat1 = pygame.draw.rect(tela, cor_chao, (0, 600, 100, 250))  # chão com altura de 100px
        plat2 = pygame.draw.rect(tela, cor_chao, (200, 600, 500, 250))  # chão com altura de 100px

        # Lista de objetos para colisão
        objetos_colisao = [ plat1, plat2, teto1]

        # Move o personagem considerando colisão
        riven.mover(teclas, objetos_colisao)
    
        # Desenha o personagem
        riven.desenhar(tela)
        

        # Desenha hitbox do personagem
        pygame.draw.rect(tela, (255, 0, 0), riven.rect, 2)
        #morte por queda(farei depois por npc)
        if riven.pos_y >= 3000:
            death = True
        #localização do boneco
        print(f"Y = {riven.pos_y}")
        print(f"X = {riven.pos_x}")

        pygame.display.flip()
        relogio.tick(60)

pygame.quit()
