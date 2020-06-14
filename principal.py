#------Inicialização-----
#Importando bibliotecas
import pygame
import math
import time
from final import *
from classes import *
from pygame import mixer

#Criando função principal
def Principal(window):
    #Criando tela
    WIDTH = 383*2
    HEIGHT = 286*2
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Among OOOF')

    #Criando o fundo e os personagens
    jogador_WIDTH = 50
    jogador_HEIGHT = 50
    font = pygame.font.SysFont(None, 48)

    background = pygame.image.load('imagens/Cidadinha.jpg').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    verde_img = pygame.image.load('imagens/Among_Us_Verde.png').convert_alpha()
    verde_img = pygame.transform.scale(verde_img, (jogador_WIDTH, jogador_HEIGHT))

    vermelho_img = pygame.image.load('imagens/Among_Us_Vermelho.png').convert_alpha()
    vermelho_img = pygame.transform.scale(vermelho_img, (jogador_WIDTH, jogador_HEIGHT))

    amarelo_img = pygame.image.load('imagens/Among_Us_Amarelo.png').convert_alpha()
    amarelo_img = pygame.transform.scale(amarelo_img, (jogador_WIDTH, jogador_HEIGHT))

    preto_img = pygame.image.load('imagens/morto.png').convert_alpha()
    preto_img = pygame.transform.scale(preto_img, (jogador_WIDTH, jogador_HEIGHT))

    rosa_img = pygame.image.load('imagens/Among_Us_Rosa.png').convert_alpha()
    rosa_img = pygame.transform.scale(rosa_img, (jogador_WIDTH, jogador_HEIGHT))

    branco_img = pygame.image.load('imagens/Among_Us_Branco.png').convert_alpha()
    branco_img = pygame.transform.scale(branco_img, (jogador_WIDTH, jogador_HEIGHT))

    roxo_img = pygame.image.load('imagens/Among_Us_Roxo.png').convert_alpha()
    roxo_img = pygame.transform.scale(roxo_img, (jogador_WIDTH, jogador_HEIGHT))

    laranja_img = pygame.image.load('imagens/Among_Us_Laranja.png').convert_alpha()
    laranja_img = pygame.transform.scale(laranja_img, (jogador_WIDTH, jogador_HEIGHT))

    azul_img = pygame.image.load('imagens/Among_Us_Azul.png').convert_alpha()
    azul_img = pygame.transform.scale(azul_img, (jogador_WIDTH, jogador_HEIGHT))



    # ----- Inicia estruturas de dados
    # Definindo os novos tipos

    #Colocando a música de fundo
    mixer.music.load('sons/principal_musica.mp3')
    mixer.music.play(-1)

    # ----- Inicia estruturas de dados
    game = True

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    FPS = 30

    #Definindo all sprites
    all_sprites = pygame.sprite.Group()

    #Definindo grupos de objetos para cada personagem
    ob_verde = pygame.sprite.Group()
    ob_vermelho = pygame.sprite.Group()
    ob_amarelo = pygame.sprite.Group()
    ob_preto = pygame.sprite.Group()
    ob_rosa = pygame.sprite.Group()
    ob_branco = pygame.sprite.Group()
    ob_roxo = pygame.sprite.Group()
    ob_laranja = pygame.sprite.Group()
    ob_azul = pygame.sprite.Group()


    # Criando o jogador
    player = Jogador()
    all_sprites.add(player)

    #Criando o personagem verde
    personagem_verde = Verde(verde_img)
    all_sprites.add(personagem_verde)
    ob_verde.add(personagem_verde)
    text_verde = ''

    #Criando o personagem vermelho
    personagem_vermelho = Vermelho(vermelho_img)
    all_sprites.add(personagem_vermelho)
    ob_vermelho.add(personagem_vermelho)
    text_vermelho = ''

    #Criando o personagem amarelo
    personagem_amarelo = Amarelo(amarelo_img)
    all_sprites.add(personagem_amarelo)
    ob_amarelo.add(personagem_amarelo)
    text_aramelo = ''

    #Criando o personagem preto
    personagem_preto = Preto(preto_img)
    all_sprites.add(personagem_preto)
    ob_preto.add(personagem_preto)
    text_preto = ''

    #Criando o personagem rosa
    personagem_rosa = Rosa(rosa_img)
    all_sprites.add(personagem_rosa)
    ob_rosa.add(personagem_rosa)
    text_rosa = ''

    #Criando o personagem branco
    personagem_branco = Branco(branco_img)
    all_sprites.add(personagem_branco)
    ob_branco.add(personagem_branco)
    text_branco = ''

    #Criando o personagem roxo
    personagem_roxo = Roxo(roxo_img)
    all_sprites.add(personagem_roxo)
    ob_roxo.add(personagem_roxo)
    text_roxo = ''

    #Criando o personagem laranja
    personagem_laranja = Laranja(laranja_img)
    all_sprites.add(personagem_laranja)
    ob_laranja.add(personagem_laranja)
    text_laranja = ''

    #Criando o personagem azul
    personagem_azul = Azul(azul_img)
    all_sprites.add(personagem_azul)
    ob_azul.add(personagem_azul)
    text_azul = ''

    #Definindo o valor RGB para branco, verde e azul (cores das fontes)
    white = (255, 255, 255) 
    white2 = (232, 232, 241)
    black = (0, 0, 0)
    black2 = (42, 42, 47)
    red = (246, 5, 5)    
    blood = (208, 35, 44)
    green = (27, 141, 79) 
    blue = (7, 24, 226) 
    orange = (251, 127, 7)
    purple = (110, 20, 213)
    pink = (247, 62, 201)
    yellow = (255, 248, 64)

    #Criando variáveisde tempo
    #tempo_principal = pygame.time.get_ticks()
    tempo_verde = pygame.time.get_ticks()
    tempo_vermelho = pygame.time.get_ticks()
    tempo_amarelo = pygame.time.get_ticks()
    tempo_preto = pygame.time.get_ticks()
    tempo_rosa = pygame.time.get_ticks()
    tempo_branco = pygame.time.get_ticks()
    tempo_roxo = pygame.time.get_ticks()
    tempo_laranja = pygame.time.get_ticks()
    tempo_azul = pygame.time.get_ticks()

    # ===== Loop principal =====
    while game:
        clock.tick(FPS)

        tempo_principal = pygame.time.get_ticks()

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
                    player.image = player.jogador_img_esq
                if event.key == pygame.K_RIGHT:
                    player.speedx += 8
                    player.image = player.jogador_img_dir
                if event.key == pygame.K_UP:
                    player.speedy += 8
                if event.key == pygame.K_DOWN:
                    player.speedy -= 8
                
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


        #Imprimindo tempo
        contando = 30 - (tempo_principal-10000)/1000
        conta = int(contando)
        superficie_cont = font.render(str(conta), True, blood)  

        # ----- Atualiza estado do jogo
        all_sprites.update()

        #Verificando se houve colisão entre o jogador e o personagem verde
        hit_verde = pygame.sprite.spritecollide(player, ob_verde, False)
        if len(hit_verde) == 1:
            #fala_verde()
            text_verde = 'bom dia'
            tempo_verde = pygame.time.get_ticks()
            
        #Verificando se houve colisão entre o jogador e o personagem vermelho
        hit_vermelho = pygame.sprite.spritecollide(player, ob_vermelho, False)
        if len(hit_vermelho) == 1:
            text_vermelho = 'eae'
            tempo_vermelho = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem amarelo
        hit_amarelo = pygame.sprite.spritecollide(player, ob_amarelo, False)
        if len(hit_amarelo) == 1:
            text_aramelo = 'eae'
            tempo_amarelo = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem preto
        hit_preto = pygame.sprite.spritecollide(player, ob_preto, False)
        if len(hit_preto) == 1:
            text_preto = 'estou morto ;-;'
            tempo_preto = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem rosa
        hit_rosa = pygame.sprite.spritecollide(player, ob_rosa, False)
        if len(hit_rosa) == 1:
            text_rosa = 'eae'
            tempo_rosa = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem branco
        hit_branco = pygame.sprite.spritecollide(player, ob_branco, False)
        if len(hit_branco) == 1:
            text_branco = 'eae'
            tempo_branco = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem roxo
        hit_roxo = pygame.sprite.spritecollide(player, ob_roxo, False)
        if len(hit_roxo) == 1:
            text_roxo = 'eae'
            tempo_roxo = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem laranja
        hit_laranja = pygame.sprite.spritecollide(player, ob_laranja, False)
        if len(hit_laranja) == 1:
            text_laranja = 'eae'
            tempo_laranja = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem azul
        hit_azul = pygame.sprite.spritecollide(player, ob_azul, False)
        if len(hit_azul) == 1:
            text_azul = 'eae'
            tempo_azul = pygame.time.get_ticks()

        # ----- Gera saídas
        window.blit(background, (0, 0))

        #Criando padrões para formato do texto
        #superficie = font.render(text, True, blue)
        #tempo = pygame.time.get_ticks()
        superficie_preto = font.render(text_preto, True, black2)
        superficie_aramelo = font.render(text_aramelo, True, yellow)
        superficie_azul = font.render(text_azul, True, blue)
        superficie_branco = font.render(text_branco, True, white2)
        superficie_verde = font.render(text_verde, True, green, black)
        superficie_laranja = font.render(text_laranja, True, orange)
        superficie_rosa = font.render(text_rosa, True, pink)
        superficie_roxo = font.render(text_roxo, True, purple)
        superficie_vermelho = font.render(text_vermelho, True, red)

        #Para o verde
        if tempo_principal - tempo_verde < 500:
            window.blit(superficie_verde, (0,0))
        #window.blit(jogador, (meteor_x, meteor_y))

        #Para o vermelho
        if tempo_principal - tempo_vermelho < 200:
            window.blit(superficie_vermelho, (0,0))

        #Para o amarelo
        if tempo_principal - tempo_amarelo < 200:
            window.blit(superficie_aramelo, (0,0))

        #Para o preto
        if tempo_principal - tempo_preto < 200:
            window.blit(superficie_preto, (0,0))

        #Para o rosa
        if tempo_principal - tempo_rosa < 200:
            window.blit(superficie_rosa, (0,0))

        #Para o branco
        if tempo_principal - tempo_branco < 200:
            window.blit(superficie_branco, (0,0))
        
        #Para o roxo
        if tempo_principal - tempo_roxo < 200:
            window.blit(superficie_roxo, (0,0))
        
        #Para o laranja
        if tempo_principal - tempo_laranja < 200:
            window.blit(superficie_laranja, (0,0))
        
        #Para o azul
        if tempo_principal - tempo_azul < 200:
            window.blit(superficie_azul, (0,0))

        #Para o tempo
        if tempo_principal <= 40000:
            window.blit(superficie_cont,(WIDTH - 50, 20))

        #Para o final
        if tempo_principal > 400:
            Final(window)


        all_sprites.draw(window)
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

