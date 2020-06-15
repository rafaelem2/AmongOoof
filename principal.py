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
    jogador_HEIGHT = 70
    font = pygame.font.SysFont(None, 38)
    font2 = pygame.font.SysFont(None, 50)

    quadro_img = pygame.image.load('imagens/o_quadro.png').convert_alpha()
    quadro_img = pygame.transform.scale(quadro_img, (40, 30))

    background = pygame.image.load('imagens/cidadinha_fogo.png').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    verde_img = pygame.image.load('imagens/verde_bombeiro_esq.png').convert_alpha()
    verde_img = pygame.transform.scale(verde_img, (jogador_WIDTH, jogador_HEIGHT))

    vermelho_img = pygame.image.load('imagens/vermelho_trabalhador_dir.png').convert_alpha()
    vermelho_img = pygame.transform.scale(vermelho_img, (jogador_WIDTH, jogador_HEIGHT))

    amarelo_img = pygame.image.load('imagens/amarelo_capitaomostarda_dir.png').convert_alpha()
    amarelo_img = pygame.transform.scale(amarelo_img, (jogador_WIDTH, jogador_HEIGHT))

    preto_img = pygame.image.load('imagens/morto.png').convert_alpha()
    preto_img = pygame.transform.scale(preto_img, (jogador_WIDTH, jogador_WIDTH))

    rosa_img = pygame.image.load('imagens/rosa_policial_esq.png').convert_alpha()
    rosa_img = pygame.transform.scale(rosa_img, (jogador_WIDTH, jogador_HEIGHT))

    branco_img = pygame.image.load('imagens/branco_medico_dir.png').convert_alpha()
    branco_img = pygame.transform.scale(branco_img, (jogador_WIDTH, jogador_HEIGHT))

    roxo_img = pygame.image.load('imagens/roxo_piloto_dir.png').convert_alpha()
    roxo_img = pygame.transform.scale(roxo_img, (jogador_WIDTH, jogador_HEIGHT))

    laranja_img = pygame.image.load('imagens/laranja_astronauta_dir.png').convert_alpha()
    laranja_img = pygame.transform.scale(laranja_img, (jogador_WIDTH, jogador_HEIGHT))

    azul_img = pygame.image.load('imagens/azul_frio_dir.png').convert_alpha()
    azul_img = pygame.transform.scale(azul_img, (jogador_WIDTH, jogador_HEIGHT - 10))



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
    text_verde2 = ''
    text_verde3 = ''

    #Criando o personagem vermelho
    personagem_vermelho = Vermelho(vermelho_img)
    all_sprites.add(personagem_vermelho)
    ob_vermelho.add(personagem_vermelho)
    text_vermelho = ''
    text_vermelho2 = ''

    #Criando o personagem amarelo
    personagem_amarelo = Amarelo(amarelo_img)
    all_sprites.add(personagem_amarelo)
    ob_amarelo.add(personagem_amarelo)
    text_aramelo = ''
    text_aramelo2 = ''

    #Criando o personagem preto
    personagem_preto = Preto(preto_img)
    all_sprites.add(personagem_preto)
    ob_preto.add(personagem_preto)
    text_preto = ''

    #Criando o quadro
    o_quadro = Quadro(quadro_img)
    all_sprites.add(o_quadro)

    #Criando o personagem rosa
    personagem_rosa = Rosa(rosa_img)
    all_sprites.add(personagem_rosa)
    ob_rosa.add(personagem_rosa)
    text_rosa = ''
    text_rosa2 = ''

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
    text_roxo2 = ''

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
    text_azul2 = ''

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
        contando = 90 - (tempo_principal-10000)/1000
        conta = int(contando)
        superficie_cont = font2.render(str(conta), True, blood)  

        # ----- Atualiza estado do jogo
        all_sprites.update()

        #Verificando se houve colisão entre o jogador e o personagem verde
        hit_verde = pygame.sprite.spritecollide(player, ob_verde, False)
        if len(hit_verde) == 1:
            #fala_verde()
            text_verde = 'tentamos apagar o fogo mas ainda não conseguimos.'
            text_verde2 = 'estava escuro ontem, será que confundiram ele '
            text_verde3 = 'com um ladrão?'
            tempo_verde = pygame.time.get_ticks()
            
        #Verificando se houve colisão entre o jogador e o personagem vermelho
        hit_vermelho = pygame.sprite.spritecollide(player, ob_vermelho, False)
        if len(hit_vermelho) == 1:
            text_vermelho = 'é irônico que ele se salvou do incêndio '
            text_vermelho2 = 'e morreu logo depois...'
            tempo_vermelho = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem amarelo
        hit_amarelo = pygame.sprite.spritecollide(player, ob_amarelo, False)
        if len(hit_amarelo) == 1:
            text_aramelo = 'Coronel Mostarda à sua disposição!'
            text_aramelo2 = 'a missão do astronauta não era ontem à noite?'
            tempo_amarelo = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem preto
        hit_preto = pygame.sprite.spritecollide(player, ob_preto, False)
        if len(hit_preto) == 1:
            text_preto = 'estou morto ;-;'
            window.blit(superficie_preto, (0,0))
            tempo_preto = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem rosa
        hit_rosa = pygame.sprite.spritecollide(player, ob_rosa, False)
        if len(hit_rosa) == 1:
            text_rosa = 'quando passei aqui essa manhã não tinha mais ninguém,'
            text_rosa2 = 'mas pelo menos um quadro foi salvo'
            tempo_rosa = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem branco
        hit_branco = pygame.sprite.spritecollide(player, ob_branco, False)
        if len(hit_branco) == 1:
            text_branco = 'tentei salvar o dono do museu, mas não consegui'
            tempo_branco = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem roxo
        hit_roxo = pygame.sprite.spritecollide(player, ob_roxo, False)
        if len(hit_roxo) == 1:
            text_roxo = 'quando sobrevoei a cidade ontem à noite '
            text_roxo2 = 'o museu já estava em chamas '
            tempo_roxo = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem laranja
        hit_laranja = pygame.sprite.spritecollide(player, ob_laranja, False)
        if len(hit_laranja) == 1:
            text_laranja = 'não sei como vim parar aqui... era para eu estar em marte'
            tempo_laranja = pygame.time.get_ticks()

        #Verificando se houve colisão entre o jogador e o personagem azul
        hit_azul = pygame.sprite.spritecollide(player, ob_azul, False)
        if len(hit_azul) == 1:
            text_azul = 'ele levou um tiro nas costas, que covardia!'
            text_azul2 = 'aliás está muito frio!'
            tempo_azul = pygame.time.get_ticks()

        # ----- Gera saídas
        window.blit(background, (0, 0))

        #Criando padrões para formato do texto
        superficie_preto = font.render(text_preto, True, black2, white)
        superficie_aramelo = font.render(text_aramelo, True, yellow, black)
        superficie_aramelo2 = font.render(text_aramelo2, True, yellow, black)
        superficie_azul = font.render(text_azul, True, blue, black)
        superficie_azul2 = font.render(text_azul2, True, blue, black)
        superficie_branco = font.render(text_branco, True, white2, black)
        superficie_verde = font.render(text_verde, True, green, black)
        superficie_verde2 = font.render(text_verde2, True, green, black)
        superficie_verde3 = font.render(text_verde3, True, green, black)
        superficie_laranja = font.render(text_laranja, True, orange, black)
        superficie_rosa = font.render(text_rosa, True, pink, black)
        superficie_rosa2 = font.render(text_rosa2, True, pink, black)
        superficie_roxo = font.render(text_roxo, True, purple, black)
        superficie_roxo2 = font.render(text_roxo2, True, purple, black)
        superficie_vermelho = font.render(text_vermelho, True, red, black)
        superficie_vermelho2 = font.render(text_vermelho2, True, red, black)

        #Para o verde
        if tempo_principal - tempo_verde < 2:
            window.blit(superficie_verde, (0,0))
            window.blit(superficie_verde2, (0,27))
            window.blit(superficie_verde3, (0,54))

        #Para o vermelho
        if tempo_principal - tempo_vermelho < 2:
            window.blit(superficie_vermelho, (0,0))
            window.blit(superficie_vermelho2, (0,27))

        #Para o amarelo
        if tempo_principal - tempo_amarelo < 2:
            window.blit(superficie_aramelo, (0,0))
            window.blit(superficie_aramelo2, (0,27))
        
        #Para o preto
        if tempo_principal - tempo_preto < 2:
            window.blit(superficie_preto, (0,0))
        
        #Para o rosa
        if tempo_principal - tempo_rosa < 2:
            window.blit(superficie_rosa, (0,0))
            window.blit(superficie_rosa2, (0,28.5))

        #Para o branco
        if tempo_principal - tempo_branco < 2:
            window.blit(superficie_branco, (0,0))
        
        #Para o roxo
        if tempo_principal - tempo_roxo < 2:
            window.blit(superficie_roxo, (0,0))
            window.blit(superficie_roxo2, (0,27))
        
        #Para o laranja
        if tempo_principal - tempo_laranja < 2:
            window.blit(superficie_laranja, (0,0))
        
        #Para o azul
        if tempo_principal - tempo_azul < 2:
            window.blit(superficie_azul, (0,0))
            window.blit(superficie_azul2, (0,27.5))

        #Para o tempo
        if tempo_principal <= 100000:
            window.blit(superficie_cont,(WIDTH - 40, 00))

        #Para o final
        if tempo_principal > 100000:
            Final(window)


        all_sprites.draw(window)
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

