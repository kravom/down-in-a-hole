from player import Player
from mapa import Mapa
from settings import *
from music import Music
from hostile import Hostile
from boss import Boss

pygame.init()

# Configuração principal
tela = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Two Beers for Alice')
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)
relogio = pygame.time.Clock()

# Estado do jogo
death = False
executando = True
#-----------------
no_menu = True 

# Recursos
riven = Player()
riven_dead = pygame.image.load('images/player_dead.png').convert_alpha()
riven_dead = pygame.transform.scale(riven_dead, (200, 215))
Love_Hate_Love = Music('music/Again.mp3')

# Cronômetro
tempo_inicial = pygame.time.get_ticks()

# ------- Carregamento único das imagens -----------------------------------------
texura_ba = pygame.image.load('images/barreira/olho_barreira.png').convert_alpha()
texura_ba = pygame.transform.scale(texura_ba, (500, 400))

textura_teto1 = pygame.image.load('images/plat_papelao.png').convert_alpha()
textura_teto1 = pygame.transform.scale(textura_teto1, (100, 90))

textura_teto2 = pygame.image.load('images/plat_caixa.png').convert_alpha()
textura_teto2 = pygame.transform.scale(textura_teto2, (120, 110))

textura_teto3 = pygame.transform.scale(textura_teto1, (100, 90))

textura_chao = pygame.image.load('images/chão.png').convert_alpha()
textura_chao = pygame.transform.scale(textura_chao, (1500, 200))

# novas cargas fora do loop
tex_in1_img = pygame.image.load('images/plat_viva.png').convert_alpha()
tex_in1_img = pygame.transform.scale(tex_in1_img, (700, 290))

ponte1_img = pygame.image.load('images/ponte_1.png').convert_alpha()
ponte1_img = pygame.transform.scale(ponte1_img, (1500, 400))

ladder_img = pygame.image.load('images/ladder.png').convert_alpha()
ladder_img = pygame.transform.scale(ladder_img, (700, 490))
# ------------------------------------------------------------------

# Inimigos
inimigos = [
    Hostile(tela, 1680, 50, 250, 230, pasta='images/inimigos/sun', base_name='sun', frame_count=7),
    Hostile(tela, 1000, 590, 100, 110, pasta='images/inimigos/jar', base_name='jar', frame_count=10),
    Hostile(tela, 2300, 590, 100, 110, pasta='images/inimigos/jar', base_name='jar', frame_count=10),
    Hostile(tela, 2600, 550, 125, 150, pasta='images/inimigos/caixad', base_name='caixa', frame_count=2),
    Hostile(tela, 4000, 560, 155, 140, pasta='images/inimigos/caranguejo', base_name='caranguejo', frame_count=10),
    Hostile(tela, 5300, 560, 155, 140, pasta='images/inimigos/caranguejo', base_name='caranguejo', frame_count=10),
    Hostile(tela, 5500, 50, 250, 230, pasta='images/inimigos/sun', base_name='sun', frame_count=7),
    Hostile(tela, 8000, 50, 250, 230, pasta='images/inimigos/sun', base_name='sun', frame_count=7),
    Hostile(tela, 5800, 550, 125, 150, pasta='images/inimigos/caixad', base_name='caixa', frame_count=2),
    Hostile(tela, 7000, 550, 125, 150, pasta='images/inimigos/caixad', base_name='caixa', frame_count=2),
    Hostile(tela, 5500, 560, 155, 140, pasta='images/inimigos/caranguejo', base_name='caranguejo', frame_count=10),
    Hostile(tela, 8000, 550, 125, 150, pasta='images/inimigos/caixad', base_name='caixa', frame_count=2),
    Hostile(tela, 7500, 590, 100, 110, pasta='images/inimigos/jar', base_name='jar', frame_count=10),
    Hostile(tela, 6500, 590, 100, 110, pasta='images/inimigos/jar', base_name='jar', frame_count=10),
]

# configurações de inimigos
inimigos[0].vel_x = 5
inimigos[0].limite_esquerda = 1500
inimigos[0].limite_direita = 1750
inimigos[0].vel_y = 5
inimigos[0].limite_inferior += 540
inimigos[6].vel_x = 7
inimigos[6].limite_esquerda = 5499
inimigos[6].limite_direita = 9200
inimigos[6].vel_y = 7
inimigos[6].limite_inferior += 420
inimigos[7].vel_x = 7
inimigos[7].limite_esquerda = 5499
inimigos[7].limite_direita = 9201
inimigos[7].vel_y = 7
inimigos[7].limite_inferior += 420
inimigos[3].vel_y = 5
inimigos[3].limite_superior -= 150
inimigos[3].limite_inferior += 1
inimigos[8].vel_y = 5
inimigos[8].limite_superior -= 150
inimigos[8].limite_inferior += 1
inimigos[9].vel_y = 5
inimigos[9].limite_superior -= 150
inimigos[9].limite_inferior += 1
inimigos[11].vel_y = 4
inimigos[11].limite_superior -= 150
inimigos[11].limite_inferior += 1
inimigos[4].vel_x = 8
inimigos[4].limite_esquerda = 4000
inimigos[4].limite_direita = 5300
inimigos[5].vel_x = 10
inimigos[5].limite_esquerda = 4000
inimigos[5].limite_direita = 5301
inimigos[10].vel_x = 8
inimigos[10].limite_esquerda = 5499
inimigos[10].limite_direita = 9200

mapa = Mapa()
camera_x = 0  # deslocamento do mundo

def camera_update(riven):
    global camera_x
    limite_camera = 742
    limite_camera2 = 500
    if riven.pos_x > limite_camera:
        camera_x += riven.vel_x
        riven.pos_x = limite_camera
        riven.rect.topleft = (riven.pos_x, riven.pos_y)
    if riven.pos_x < limite_camera2:
        camera_x += riven.vel_x
        riven.pos_x = limite_camera2
        riven.rect.topleft = (riven.pos_x, riven.pos_y)

def reset_player():
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
    global death, tempo_inicial
    tela.blit(riven_dead, ((WINDOW_WIDTH // 2 + 40), (WINDOW_HEIGHT // 2 + 100)))
    pygame.draw.rect(tela, (0, 0, 0), (300, 150, 1000, 255))
    font = pygame.font.Font('font/Gameplay.ttf', 120)
    font1 = pygame.font.Font('font/Gameplay.ttf', 40)
    text_game_over = font.render("GAME-OVER", True, (128,0,0))
    text_restart = font1.render("Pressione R para continuar", True, (128,0,0))
    tela.blit(text_game_over, ((WINDOW_WIDTH // 2 - 300), (WINDOW_HEIGHT // 2 - 200)))
    tela.blit(text_restart, ((WINDOW_WIDTH // 2 - 230), (WINDOW_HEIGHT // 2 - 30)))
    if teclas[pygame.K_r]:
        death = False
        reset_player()
        tempo_inicial = pygame.time.get_ticks()

def draw_world(camera_x):
    ba = pygame.Rect(0 - camera_x, 250, 500, 400)
    tela.blit(texura_ba, ba.topleft)
    teto1 = pygame.Rect(830 - camera_x, 500, 100, 90)
    tela.blit(textura_teto1, teto1.topleft)
    teto2 = pygame.Rect(2600 - camera_x, 295, 120, 110)
    tela.blit(textura_teto2, teto2.topleft)
    teto3 = pygame.Rect(4800 - camera_x, 500, 120, 105)
    tela.blit(textura_teto2, teto3.topleft)
    plat1 = pygame.Rect(0 - camera_x, 700, 1500, 2000)
    tela.blit(textura_chao, plat1.topleft)
    plat3 = pygame.Rect(2000 - camera_x, 700, 1500, 2000)
    tela.blit(textura_chao, plat3.topleft)
    plat4 = pygame.Rect(4000 - camera_x, 700, 1500, 2000)
    tela.blit(textura_chao, plat4.topleft)
    plat5 = pygame.Rect(7000 - camera_x, 700, 1500, 2000)
    tela.blit(textura_chao, plat5.topleft)
    plat6 = pygame.Rect(8000 - camera_x, 700, 1500, 2000)
    tela.blit(textura_chao, plat6.topleft)
    ladder1 = pygame.Rect(9500- camera_x, 602, 100, 90)
    ladder2 = pygame.Rect(9620- camera_x, 503, 100, 90)
    ladder3 = pygame.Rect(9735- camera_x, 405, 100, 90)
    ladder4 = pygame.Rect(9850- camera_x, 307, 100, 90)
    ladder5 = pygame.Rect(9967- camera_x, 208, 240, 90)
    plat_in1 = pygame.Rect(2900 - camera_x, 500, 600, 600)
    plat_in2 = pygame.Rect(5500 - camera_x, 700, 1500, 2000)
    return [plat1, teto1, ba, plat3, teto2, plat4, plat5, teto3, plat_in1, plat_in2, plat6, ladder1, ladder2, ladder3, ladder4, ladder5]

# MENU INICIAL ---
def menu_inicial():
    # desenha o fundo do menu
    fundo_menu = pygame.image.load('images/img_menu.png').convert()
    fundo_menu = pygame.transform.scale(fundo_menu, (1550, 800))
    tela.blit(fundo_menu, (0, 0))
    pygame.display.flip()

# Loop do menu inicial
while no_menu:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            no_menu = False
            executando = False
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RETURN]:
        no_menu = False
    if teclas[pygame.K_ESCAPE]:
        no_menu = False
        executando = False

    menu_inicial()
    relogio.tick(30)

# --- LOOP PRINCIPAL ---
while executando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    teclas = pygame.key.get_pressed()

    for enemy in inimigos:
        if enemy.vel_x != 0:
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
        pygame.display.flip()
        relogio.tick(10)
        continue

    mapa.paint(tela,camera_x)
    camera_update(riven)
    objetos_colisao = draw_world(camera_x)
    riven.mover(teclas, objetos_colisao)
    riven.desenhar(tela)

    tex = pygame.Rect(2840 - camera_x, 410, 700, 290)
    tela.blit(tex_in1_img, tex.topleft)

    ponte = pygame.Rect(5500 - camera_x, 476, 1500, 400)
    tela.blit(ponte1_img, ponte.topleft)

    tex_ladder = pygame.Rect(9500 - camera_x, 210, 700, 490)
    tela.blit(ladder_img, tex_ladder.topleft)

    for enemy in inimigos:
        if enemy.draw(tela, camera_x, riven):
            death = True
            break 
    if riven.pos_y >= 2000:
        death = True

    # Cronômetro MM:SS
    tempo_decorrido = (pygame.time.get_ticks() - tempo_inicial) // 1000
    minutos = tempo_decorrido // 60
    segundos = tempo_decorrido % 60
    font_cronometro = pygame.font.Font('font/Gameplay.ttf', 40)
    texto_cronometro = font_cronometro.render(f"{minutos:02}:{segundos:02}", True, (255, 255, 255))
    tela.blit(texto_cronometro, (1400, 20))

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
