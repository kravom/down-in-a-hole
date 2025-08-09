import pygame

pygame.init()

tela = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()

x = 400
y = 581  # posição inicial no chão
vel_x = 0
aceleracao = 0.5       # quão rápido acelera no eixo X
desaceleracao = 0.4    # quão rápido desacelera
velocidade_max = 6

vel_y = 0
gravidade = 0.5
pulo_forca = -12       # força inicial do pulo
pulo_forca_extra = -0.4  # força adicional enquanto segura o botão
pulo_max_frames = 15   # tempo máximo segurando pulo para aumentar altura
pulo_contador = 0

pygame.display.set_caption("Teste de gravidade estilo Mario")

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    teclas = pygame.key.get_pressed()

    # Movimento horizontal com inércia
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        vel_x -= aceleracao
    elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        vel_x += aceleracao
    else:
        # aplica desaceleração quando não há input
        if vel_x > 0:
            vel_x -= desaceleracao
            if vel_x < 0:
                vel_x = 0
        elif vel_x < 0:
            vel_x += desaceleracao
            if vel_x > 0:
                vel_x = 0

    # limita velocidade máxima
    if vel_x > velocidade_max:
        vel_x = velocidade_max
    if vel_x < -velocidade_max:
        vel_x = -velocidade_max

    x += vel_x

    # Verifica se está no chão
    no_chao = y >= 581

    # Pulo inicial
    if no_chao and (teclas[pygame.K_w] or teclas[pygame.K_SPACE]):
        vel_y = pulo_forca
        pulo_contador = 0

    # Pulo variável: enquanto segura, aplica força extra por alguns frames
    if (teclas[pygame.K_w] or teclas[pygame.K_SPACE]) and pulo_contador < pulo_max_frames and vel_y < 0:
        vel_y += pulo_forca_extra
        pulo_contador += 1

    # Aplica gravidade
    vel_y += gravidade
    y += vel_y

    # Impede que passe do chão
    if y > 581:
        y = 581
        vel_y = 0

    # Renderização
    tela.fill((30, 30, 30))
    pygame.draw.circle(tela, (255, 0, 0), (int(x), int(y)), 20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
