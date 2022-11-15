import pygame
import random

pygame.init()

x = 1280
y = 720

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption('Início da Jornada')

paisagem = pygame.image.load('images/paisagem.jpg').convert_alpha()
paisagem = pygame.transform.scale(paisagem, (x,y))

alien = pygame.image.load('images/alien.png').convert_alpha()
alien = pygame.transform.scale(alien, (50,50))

playerImg = pygame.image.load('images/airship.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (50,50)) #conversão de tamanho da nave
playerImg = pygame.transform.rotate(playerImg, -90)

missil = pygame.image.load('images/shot.png').convert_alpha()
missil = pygame.transform.scale(playerImg, (50, 50))
missil = pygame.transform.rotate(missil, -45)

pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

vel_x_missil = 0
pos_x_missil = 200
pos_y_missil = 300

#looping para o movimento e dinâmica

triggered = False

#definindo os sólidos

player_rect = playerImg.get_rect()
#alien_rect = alien.get.rect()
missil_rect = missil.get_rect()


rodando = True

#funções 
def respawn():
    x = 1350
    y = random.randint(1, 640)
    return[x,y]

def respawn_missil():
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y
    vel_x_missil = 0
    return[respawn_missil_x, respawn_missil_y,triggered,vel_x_missil]

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    tela.blit(paisagem, (0,0))

    rel_x = x % paisagem.get_rect().width
    tela.blit(paisagem, (rel_x - paisagem.get_rect().width,0)) #cria um background
    if rel_x < 1280:
        tela.blit(paisagem, (rel_x, 0))

    #comandos e teclas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_w] and pos_player_y > 1:
        pos_player_y -=1

        if not triggered:
            pos_y_missil -= 1

    if tecla[pygame.K_s] and pos_player_y < 665:
        pos_player_y += 1

        if not triggered:
            pos_y_missil += 1

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_x_missil = 1

    # respawn
    if pos_alien_x == 50:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]

    if pos_x_missil == 1300:
        pos_x_missil, pos_y_missil, triggered, vel_x_missil = respawn_missil()
    
    #posição rect

    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    missil_rect.x = pos_x_missil
    missil_rect.y = pos_y_missil




    #movimento
    x-=2
    pos_alien_x -= 1

    pos_x_missil += vel_x_missil

    pygame.draw.rect(tela, (255, 0, 0), player_rect, 4)
    pygame.draw.rect(tela, (255, 0, 0), missil_rect, 4)
    #pygame.draw.rect(tela, (255, 0,  0), alien_rect, 4)

    #criar imagem
    tela.blit(alien, (pos_alien_x, pos_alien_y))
    tela.blit(missil, (pos_x_missil,pos_y_missil))
    tela.blit(playerImg, (pos_player_x, pos_player_y))


    pygame.display.update()