#Importando bibliotecas
import pygame
from classes_final import *
from pygame import mixer
from Explicacao import *

#Criando a função final
def Final(window):
    #Criando tela
    WIDTH = 383*2
    HEIGHT = 286*2

    #Criando a fonte para os textos
    font = pygame.font.SysFont(None, 48)

    #Criando variáveis
    text = ''
    text2 = ''
    text3 = ''
    mensagem = ''

    #Criando cores
    white = (255, 255, 255) 
    red = (255,0,0)    

    #Criando o fundo e os personagens
    jogador_WIDTH2 = 80
    jogador_HEIGHT2 = 96

    background = pygame.image.load('imagens/mapa teste.png').convert() 
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    jogador_img = pygame.image.load('imagens/Among_Us_detetive.png').convert_alpha()
    jogador_img = pygame.transform.scale(jogador_img, (jogador_WIDTH2, jogador_HEIGHT2))

    verde_img = pygame.image.load('imagens/verde_bombeiro_esq.png').convert_alpha()
    verde_img = pygame.transform.scale(verde_img, (jogador_WIDTH2, jogador_HEIGHT2))

    vermelho_img = pygame.image.load('imagens/vermelho_trabalhador_dir.png').convert_alpha()
    vermelho_img = pygame.transform.scale(vermelho_img, (jogador_WIDTH2, jogador_HEIGHT2))

    amarelo_img = pygame.image.load('imagens/amarelo_capitaomostarda_esq.png').convert_alpha()
    amarelo_img = pygame.transform.scale(amarelo_img, (jogador_WIDTH2, jogador_HEIGHT2))

    preto_img = pygame.image.load('imagens/morto.png').convert_alpha()
    preto_img = pygame.transform.scale(preto_img, (jogador_WIDTH2, jogador_WIDTH2))

    rosa_img = pygame.image.load('imagens/rosa_policial_esq.png').convert_alpha()
    rosa_img = pygame.transform.scale(rosa_img, (jogador_WIDTH2, jogador_HEIGHT2))

    branco_img = pygame.image.load('imagens/branco_medico_dir.png').convert_alpha()
    branco_img = pygame.transform.scale(branco_img, (jogador_WIDTH2 - 10, jogador_HEIGHT2))

    roxo_img = pygame.image.load('imagens/roxo_piloto_dir.png').convert_alpha()
    roxo_img = pygame.transform.scale(roxo_img, (jogador_WIDTH2, jogador_HEIGHT2))

    laranja_img = pygame.image.load('imagens/laranja_astronauta_dir.png').convert_alpha()
    laranja_img = pygame.transform.scale(laranja_img, (jogador_WIDTH2, jogador_HEIGHT2))

    azul_img = pygame.image.load('imagens/azul_frio_esq.png').convert_alpha()
    azul_img = pygame.transform.scale(azul_img, (jogador_WIDTH2, jogador_HEIGHT2))


    # ----- Inicia estruturas de dados -----
    game = True

    #Criando variável para ajustar de velocidade
    clock = pygame.time.Clock()
    FPS = 30

    #Definindo all sprites e objetos para cada personagem
    all_sprites = pygame.sprite.Group()
    ob_verde = pygame.sprite.Group()
    ob_vermelho = pygame.sprite.Group()
    ob_amarelo = pygame.sprite.Group()
    ob_rosa = pygame.sprite.Group()
    ob_branco = pygame.sprite.Group()
    ob_roxo = pygame.sprite.Group()
    ob_laranja = pygame.sprite.Group()
    ob_azul = pygame.sprite.Group()

    #Criando o jogador
    player = Jogador(jogador_img)
    all_sprites.add(player)

    #Criando o personagem verde
    personagem_verde = Verde(verde_img)
    all_sprites.add(personagem_verde)
    ob_verde.add(personagem_verde)

    #Criando o personagem vermelho
    personagem_vermelho = Vermelho(vermelho_img)
    all_sprites.add(personagem_vermelho)
    ob_vermelho.add(personagem_vermelho)

    #Criando o personagem amarelo
    personagem_amarelo = Amarelo(amarelo_img)
    all_sprites.add(personagem_amarelo)
    ob_amarelo.add(personagem_amarelo)

    #Criando o personagem rosa
    personagem_rosa = Rosa(rosa_img)
    all_sprites.add(personagem_rosa)
    ob_rosa.add(personagem_rosa)
    
    #Criando o personagem branco
    personagem_branco = Branco(branco_img)
    all_sprites.add(personagem_branco)
    ob_branco.add(personagem_branco)

    #Criando o personagem roxo
    personagem_roxo = Roxo(roxo_img)
    all_sprites.add(personagem_roxo)
    ob_roxo.add(personagem_roxo)

    #Criando o personagem laranja
    personagem_laranja = Laranja(laranja_img)
    all_sprites.add(personagem_laranja)
    ob_laranja.add(personagem_laranja)

    #Criando o personagem azul
    personagem_azul = Azul(azul_img)
    all_sprites.add(personagem_azul)
    ob_azul.add(personagem_azul)

    #Fazendo o jogador parar de andar
    player.speedx = 0

    #Colocando a música de abertura de novo
    mixer.music.load('sons/abertura.mp3')
    mixer.music.play(-1)

    # ===== Loop principal =====
    while game:
        #Começando a contagem de tempo
        clock.tick(FPS)
        window.fill((0, 0, 0))

        # ----- Trata eventos -----
        for event in pygame.event.get():
            #Verificando se a pessoa quer sair do jogo
            if event.type == pygame.QUIT:
                game = False

            #Verifica se apertou alguma tecla
            if event.type == pygame.KEYDOWN:
                #Dependendo da tecla, altera a velocidade
                if event.key == pygame.K_LEFT:
                    player.speedx = -8
                    player.image = player.jogador_img_esq
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
                    player.image = player.jogador_img_dir
                if event.key == pygame.K_UP:
                    player.speedy = 8
                if event.key == pygame.K_DOWN:
                    player.speedy = -8
            
            #Verifica se soltou alguma tecla
            if event.type == pygame.KEYUP:
                #Dependendo da tecla, altera a velocidade
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    player.speedy = 0
                if event.key == pygame.K_DOWN:
                    player.speedy = 0
        
        #Escrevendo o texto
        mensagem = 'ande até o impostor'
        superficie2 = font.render(mensagem, True, red)
        window.blit(superficie2,(383-superficie2.get_rect().width/2,20))

        #Acertou o assassino            
        hit_rosa = pygame.sprite.spritecollide(player, ob_rosa, False)
        if len(hit_rosa) == 1:
            text = 'Parabéns, você acertou! :D'
            #Colocando a música
            mixer.music.load('sons/ganhou.mp3')
            mixer.music.play(-1)
           
        #Errou o assassino
        hit_vermelho = pygame.sprite.spritecollide(player, ob_vermelho, False)
        hit_amarelo = pygame.sprite.spritecollide(player, ob_amarelo, False)
        hit_verde = pygame.sprite.spritecollide(player, ob_verde, False)
        hit_branco = pygame.sprite.spritecollide(player, ob_branco, False)
        hit_roxo = pygame.sprite.spritecollide(player, ob_roxo, False)
        hit_laranja = pygame.sprite.spritecollide(player, ob_laranja, False)
        hit_azul = pygame.sprite.spritecollide(player, ob_azul, False)

        if len(hit_vermelho) == 1 or len(hit_amarelo) == 1 or len(hit_verde) or len(hit_branco) == 1 or len(hit_roxo) == 1 or len(hit_laranja) == 1 or len(hit_azul) == 1:
            text = 'Você errou, reinicie e tente de novo :('
            text2 = 'Preste atenção nos detalhes'
            text3 = 'Como ele morreu?'
            #Colocando a música de abertura
            mixer.music.load('sons/perdeu.mp3')
            mixer.music.play(-1)

        #Criando padrões para formato do texto
        superficie = font.render(text, True, white)
        superficie2 = font.render(text2, True, white)
        superficie3 = font.render(text3, True, white)

        #Posição do texto
        window.blit(superficie,(WIDTH/2 - superficie.get_rect().width/2, HEIGHT/2 - 40))
        window.blit(superficie2,(WIDTH/2 - superficie2.get_rect().width/2, HEIGHT/2))
        window.blit(superficie3,(WIDTH/2 - superficie3.get_rect().width/2, HEIGHT/2 + 40))


        # ----- Gera saídas e atualiza estado de jogo -----
        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.update()


        #Finalizando o jogo (errou o assassino)
        if len(hit_vermelho) == 1 or len(hit_amarelo) == 1 or len(hit_verde) or len(hit_branco) == 1 or len(hit_roxo) == 1 or len(hit_laranja) == 1 or len(hit_azul) == 1:
            pygame.time.delay(2000)
            pygame.quit()

        #Passando para a Explicacao (acertou o assassino)
        if len(hit_rosa) == 1:
            pygame.time.delay(3000)
            explicacao(window)

        

# ===== Finalização =====
pygame.quit()   