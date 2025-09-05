from player import Player
from mapa import Mapa
from settings import *
from music import Music
from hostile import Hostile

pygame.init()

# Configuração principal
tela = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Two Beers for Alice')
relogio = pygame.time.Clock()
# Estado do jogo
death = False
executando = True
# Recursos
riven = Player()
riven_dead = pygame.image.load('images/player_dead.png').convert_alpha()
riven_dead = pygame.transform.scale(riven_dead, (200, 215))
#Love_Hate_Love = Music('music/Again.mp3')
cor = (250,0,0)
inimigos = []
inimigos = [
    Hostile(tela, 1680, 50, 250, 230, pasta='images/inimigos/sun', base_name='sun', frame_count=7),
    Hostile(tela, 1000, 590, 100, 110, pasta='images/inimigos/jar', base_name='jar', frame_count=10),
    Hostile(tela, 2300, 590, 100, 110, pasta='images/inimigos/jar', base_name='jar', frame_count=10),
    Hostile(tela, 2600, 550, 125, 150, pasta='images/inimigos/caixad', base_name='caixa', frame_count=2),
    Hostile(tela, 4000, 560, 155, 140, pasta='images/inimigos/caranguejo', base_name='caranguejo', frame_count=10),
    Hostile(tela, 5300, 560, 155, 140, pasta='images/inimigos/caranguejo', base_name='caranguejo', frame_count=10),
    ]
#sun 1
inimigos[0].vel_x = 5
inimigos[0].limite_esquerda = 1500
inimigos[0].limite_direita = 1750

inimigos[0].vel_y = 3
inimigos[0].limite_inferior += 540
#caixa 1
inimigos[3].vel_y = 5
inimigos[3].limite_superior -= 150
inimigos[3].limite_inferior += 1
#caranguejo 1
inimigos[4].vel_x = 5
inimigos[4].limite_esquerda = 4000
inimigos[4].limite_direita = 5300
#caranguejo 2
inimigos[5].vel_x = 5
inimigos[5].limite_esquerda = 4000
inimigos[5].limite_direita = 5301

mapa = Mapa()
camera_x = 0  # deslocamento do mundo

def camera_update(riven):
    global camera_x

    limite_camera = 742
    limite_camera2 = 500

    if riven.pos_x > limite_camera:
         #trava no limite e câmera acompanhad
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
    pygame.draw.rect(tela, (0, 0, 0), (300, 150, 1000, 255))  
    font = pygame.font.Font('font/Gameplay.ttf', 120)
    font1 = pygame.font.Font('font/Gameplay.ttf', 40)
    text_game_over = font.render("GAME-OVER", True,	(128,0,0))
    text_restart = font1.render("Pressione R para continuar", True, (128,0,0))

    tela.blit(text_game_over, ((WINDOW_WIDTH // 2 - 300), (WINDOW_HEIGHT // 2 - 200)))
    tela.blit(text_restart, ((WINDOW_WIDTH // 2 - 230), (WINDOW_HEIGHT // 2 - 30)))

    if teclas[pygame.K_r]:
        death = False
        reset_player()
  
def draw_world(camera_x):
    height = 200
    ba = pygame.Rect(0 - camera_x, 250, 500, 400)
    textura_ba = pygame.image.load('images/barreira/olho_barreira.png').convert_alpha()
    textura_ba = pygame.transform.scale(textura_ba, (ba.width, ba.height))
    tela.blit(textura_ba, ba.topleft)
   
    teto1 = pygame.Rect(830 - camera_x, 500, 100, 90)
    textura_teto1 = pygame.image.load('images/plat_papelao.png').convert_alpha()
    textura_teto1 = pygame.transform.scale(textura_teto1, (teto1.width, teto1.height))
    tela.blit(textura_teto1, teto1.topleft)

    teto2 = pygame.Rect(2600 - camera_x, 295, 120, 110)
    textura_teto2 = pygame.image.load('images\plat_caixa.png').convert_alpha()
    textura_teto2 = pygame.transform.scale(textura_teto2, (teto2.width, teto2.height))
    tela.blit(textura_teto2, teto2.topleft)

    teto3 = pygame.Rect(4800 - camera_x, 500, 100, 90)
    textura_teto3 = pygame.image.load('images/plat_papelao.png').convert_alpha()
    textura_teto3 = pygame.transform.scale(textura_teto3, (teto3.width, teto3.height))
    tela.blit(textura_teto3, teto3.topleft)

    plat1 = pygame.Rect(0 - camera_x, 700, 1500, 2000)
    textura_plat1 = pygame.image.load('images/chão.png').convert_alpha()
    textura_plat1 = pygame.transform.scale(textura_plat1, (plat1.width, height))
    tela.blit(textura_plat1, plat1.topleft)

    plat3 = pygame.Rect(2000 - camera_x, 700, 1500, 2000)
    textura_plat3 = pygame.transform.scale(textura_plat1, (plat1.width, height))
    tela.blit(textura_plat3, plat3.topleft)

    plat4 = pygame.Rect(4000 - camera_x, 700, 1500, 2000)
    textura_plat4 = pygame.transform.scale(textura_plat1, (plat1.width, height))
    tela.blit(textura_plat4, plat4.topleft)

    plat5 = pygame.Rect(5000 - camera_x, 700, 1500, 2000)
    textura_plat5 = pygame.transform.scale(textura_plat1, (plat1.width, height))
    tela.blit(textura_plat5, plat5.topleft)
   

   #coli da plataforma "viva"
    plat_in1 = pygame.Rect(2900 - camera_x, 500, 600, 600)
    return [plat1, teto1, ba, plat3, teto2, plat4, plat5, teto3, plat_in1]

# Loop principal
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    teclas = pygame.key.get_pressed()

    for enemy in inimigos:
        if enemy.vel_x != 0:  # apenas move quem tem velocidade definida
            enemy.enemy.x += enemy.vel_x * enemy.direcao_x
        if enemy.enemy.x <= enemy.limite_esquerda or enemy.enemy.x >= enemy.limite_direita:
            enemy.direcao_x *= -1

    for enemy in inimigos:
        if enemy.vel_y != 0:
            enemy.enemy.y += enemy.vel_y * enemy.direcao_y
        if enemy.enemy.y <= enemy.limite_superior or enemy.enemy.y >= enemy.limite_inferior:
                enemy.direcao_y *= -1
    if death:
        handle_death_screen(teclas)
        relogio.tick(10)
        pygame.display.flip()
        continue
    mapa.paint(tela,camera_x)

    camera_update(riven)  # atualiza posição e câmera

    objetos_colisao = draw_world(camera_x)  # desenha mundo com offset

    riven.mover(teclas, objetos_colisao)

    riven.desenhar(tela)

    tex = pygame.Rect(2840 - camera_x, 410, 700, 290)
    tex_in1 = pygame.image.load('images/plat_viva.png').convert_alpha()
    tex_in1 = pygame.transform.scale(tex_in1, (tex.width, tex.height))
    tela.blit(tex_in1, tex.topleft)
    
    # Desenha hitbox
    pygame.draw.rect(tela, (255, 0, 0), riven.rect, 2)

    for enemy in inimigos:
        if enemy.draw(tela, camera_x, riven):
            death = True
            break 
    # Morte por queda
    if riven.pos_y >= 2000:
        death = True

    # Debug
    """print(f"Y = {riven.pos_y}")
    print(f"X = {riven.pos_x}")"""

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()