import pygame
from classes import *

def Final(window):
    #Criando tela
    WIDTH = 383*2
    HEIGHT = 286*2

    #Criando o fundo e os personagens
    jogador_WIDTH2 = 100
    jogador_HEIGHT2 = 100
    font = pygame.font.SysFont(None, 48)
    background = pygame.image.load('imagens/mapa teste.png').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    jogador_img = pygame.image.load('imagens/Among_Us_Ciano.png').convert_alpha()
    jogador_img = pygame.transform.scale(jogador_img, (jogador_WIDTH2, jogador_HEIGHT2))
    verde_img = pygame.image.load('imagens/Among_Us_Green.png').convert_alpha()
    verde_img = pygame.transform.scale(verde_img, (jogador_WIDTH2, jogador_HEIGHT2))
    


    # ----- Inicia estruturas de dados
    game = True

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    FPS = 30

    #Definindo all sprites
    all_sprites = pygame.sprite.Group()
    ob_verde = pygame.sprite.Group()
 

    # Criando o jogador
    player = Jogador(jogador_img)
    all_sprites.add(player)

    #Criando o personagem verde
    personagem_verde = Verde(verde_img)
    all_sprites.add(personagem_verde)
    ob_verde.add(personagem_verde)

    

    # ===== Loop principal =====
    while game:
        clock.tick(FPS)
        window.fill((0, 0, 0))  # Preenche com a cor preta

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False

            #Verifica se apertou alguma tecla
            if event.type == pygame.KEYDOWN:
                #Dependendo da tecla, altera a velocidade
                if event.key == pygame.K_LEFT:
                    player.speedx -= 8
                if event.key == pygame.K_RIGHT:
                    player.speedx += 8
                if event.key == pygame.K_UP:
                    player.speedy += 8
                if event.key == pygame.K_DOWN:
                    player.speedy -= 8
                    print('oi\n')
                
            #Verifica se soltou alguma tecla
            if event.type == pygame.KEYUP:
                #Dependendo da tecla, altera a velocidade
                if event.key == pygame.K_LEFT:
                    player.speedx += 8
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 8
                if event.key == pygame.K_UP:
                    player.speedy -= 8
                if event.key == pygame.K_DOWN:
                    player.speedy += 8

        # ----- Gera saídas
        
        all_sprites.update()
        
        all_sprites.draw(window)
        
        pygame.display.update()  # Mostra o novo frame para o jogador
    
    pygame.quit()