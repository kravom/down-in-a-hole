from player import Player
from mapa import Mapa
from settings import *

pygame.init()

# Configuração principal
tela = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Down In A Hole')
relogio = pygame.time.Clock()
# Estado do jogo
death = False
executando = True
# Recursos
riven = Player()
riven_dead = pygame.image.load('images/player_dead.png').convert_alpha()
riven_dead = pygame.transform.scale(riven_dead, (200, 215))

mapa_fundo = Mapa('images/background.png')
tela_morte = Mapa('images/screen_death.png')

# Funções auxiliares
def reset_player():
    #Reseta o estado do jogador após a morte.
    riven.pos_x = 10
    riven.pos_y = 535
    riven.rect.topleft = (riven.pos_x, riven.pos_y)
    riven.vel_x = 0
    riven.vel_y = 0
    riven.no_chao = False
    riven.pulo_ativo = False
    riven.tempo_pulo_atual = 0

def handle_death_screen(teclas):
    #Exibe a tela de morte e verifica reinício
    global death
    tela_morte.paint(tela)
    tela.blit(riven_dead, ((WINDOW_WIDTH // 2 + 40), (WINDOW_HEIGHT // 2 + 100)))

    font = pygame.font.Font('font/WOODCUT.TTF', 100)
    text_game_over = font.render("GAME-OVER", True, (139, 0, 0))
    text_restart = font.render("Pressione R para continuar", True, (139, 0, 0))

    tela.blit(text_game_over, ((WINDOW_WIDTH // 2 - 410), (WINDOW_HEIGHT // 2 - 200)))
    tela.blit(text_restart, ((WINDOW_WIDTH // 2 - 580), (WINDOW_HEIGHT // 2 - 30)))

    if teclas[pygame.K_r]:
        death = False
        reset_player()

def draw_world():
    #Desenha o fundo, plataformas e retorna lista de colisão.
    mapa_fundo.paint(tela)
    cor_chao = (139, 69, 19)

    # Plataformas sólidas simples
    teto1 = pygame.draw.rect(tela, cor_chao, (700, 390, 100, 90))
    plat1 = pygame.draw.rect(tela, cor_chao, (0, 600, 100, 250))

    # Plataforma com textura
    plat2 = pygame.Rect(200, 600, 1000, 170)
    textura_plat2 = pygame.image.load('images/chão_3-pixilart.png').convert_alpha()
    textura_plat2 = pygame.transform.scale(textura_plat2, (plat2.width, plat2.height))
    tela.blit(textura_plat2, plat2.topleft)

    return [plat1, plat2, teto1]


# Loop principal

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    teclas = pygame.key.get_pressed()

    if death:
        handle_death_screen(teclas)
        relogio.tick(10)
        pygame.display.flip()
        continue

    tela.fill((0, 0, 0))
    objetos_colisao = draw_world()

    riven.mover(teclas, objetos_colisao)
    riven.desenhar(tela)

    # Desenha hitbox
    pygame.draw.rect(tela, (255, 0, 0), riven.rect, 2)

    # Morte por queda
    if riven.pos_y >= 3000:
        death = True

    # Debug
    print(f"Y = {riven.pos_y}")
    print(f"X = {riven.pos_x}")

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
