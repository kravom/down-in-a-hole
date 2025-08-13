from player import Player
from mapa import Mapa
from settings import *
from music import Music

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
Love_Hate_Love = Music('music/Love_Hate_Love.mp3')
mapa = Mapa('images/background.png')


# Funções auxiliares
camera_x = 0  # deslocamento do mundo

def camera_update(riven):
    global camera_x

    limite_camera = 742
    limite_camera2 = 500

    if riven.pos_x > limite_camera:
         #trava no limite e câmera acompanha
        camera_x += riven.vel_x  # soma velocidade para mover para esquerda
        riven.pos_x = limite_camera
        riven.rect.topleft = (riven.pos_x, riven.pos_y)
    if riven.pos_x < limite_camera2:
        camera_x += riven.vel_x  # soma velocidade para mover para direita
        riven.pos_x = limite_camera2
        riven.rect.topleft = (riven.pos_x, riven.pos_y)
        

    
def reset_player():
    #Reseta o jogador 
    global camera_x
    riven.pos_x = 10
    riven.pos_y = 535
    riven.rect.topleft = (riven.pos_x, riven.pos_y)
    riven.vel_x = 0
    riven.vel_y = 0
    riven.no_chao = False
    riven.pulo_ativo = False
    riven.tempo_pulo_atual = 0
    camera_x = 0

def handle_death_screen(teclas):
    #Mostra a tela de morte
    global death
    tela.blit(riven_dead, ((WINDOW_WIDTH // 2 + 40), (WINDOW_HEIGHT // 2 + 100)))

    font = pygame.font.Font('font/Gameplay.ttf', 120)
    font1 = pygame.font.Font('font/Gameplay.ttf', 40)
    text_game_over = font.render("GAME-OVER", True, (139, 0, 0))
    text_restart = font1.render("Pressione R para continuar", True, (139, 0, 0))

    tela.blit(text_game_over, ((WINDOW_WIDTH // 2 - 300), (WINDOW_HEIGHT // 2 - 200)))
    tela.blit(text_restart, ((WINDOW_WIDTH // 2 - 230), (WINDOW_HEIGHT // 2 - 30)))

    if teclas[pygame.K_r]:
        death = False
        reset_player()
  
def draw_world(camera_x):
    mapa.paint(tela)

    ba = pygame.Rect(-510 - camera_x, 250, 500, 400)
    textura_ba = pygame.image.load('images/barreira/olho_barreira.png').convert_alpha()
    textura_ba = pygame.transform.scale(textura_ba, (ba.width, ba.height))
    tela.blit(textura_ba, ba.topleft)
   
    teto1 = pygame.Rect(700 - camera_x, 500, 100, 90)
    textura_teto1 = pygame.image.load('images/plat_papelao.png').convert_alpha()
    textura_teto1 = pygame.transform.scale(textura_teto1, (teto1.width, teto1.height))
    tela.blit(textura_teto1, teto1.topleft)

    teto2 = pygame.Rect(600 - camera_x, 500, 100, 90)
    textura_teto2 = pygame.image.load('images\plat_caixa.png').convert_alpha()
    textura_teto2 = pygame.transform.scale(textura_teto2, (teto2.width, teto2.height))
    tela.blit(textura_teto2, teto2.topleft)

    plat1 = pygame.Rect(0 - camera_x, 700, 1500, 200)
    textura_plat1 = pygame.image.load('images/chão.png').convert_alpha()
    textura_plat1 = pygame.transform.scale(textura_plat1, (plat1.width, plat1.height))
    tela.blit(textura_plat1, plat1.topleft)

    plat2 = pygame.Rect(-510 - camera_x, 700, 500, 200)
    textura_plat2 = pygame.transform.scale(textura_plat1, (plat1.width, plat1.height))
    tela.blit(textura_plat2, plat2.topleft)

    plat3 = pygame.Rect(2100 - camera_x, 700, 1500, 200)
    textura_plat3 = pygame.transform.scale(textura_plat1, (plat1.width, plat1.height))
    tela.blit(textura_plat3, plat3.topleft)

    return [plat1, teto1, ba, plat3, teto2]

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
    
    camera_update(riven)  # atualiza posição e câmera

    objetos_colisao = draw_world(camera_x)  # desenha mundo com offset

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