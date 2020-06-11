import pygame
from classes import *

def Final(window):
    #Criando tela
    WIDTH = 383*2
    HEIGHT = 286*2

    #Criando variáveis
    text = ''
    mensagem = ''

    #Criando a cor branca
    white = (255, 255, 255) 
    red = (255,0,0)

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

    vermelho_img = pygame.image.load('imagens/Among_Us_Vermelho.png').convert_alpha()
    vermelho_img = pygame.transform.scale(vermelho_img, (jogador_WIDTH2, jogador_HEIGHT2))

    amarelo_img = pygame.image.load('imagens/Among_Us_Amarelo.png').convert_alpha()
    amarelo_img = pygame.transform.scale(amarelo_img, (jogador_WIDTH2, jogador_HEIGHT2))

    preto_img = pygame.image.load('imagens/Among_Us_Preto.png').convert_alpha()
    preto_img = pygame.transform.scale(preto_img, (jogador_WIDTH2, jogador_HEIGHT2))

    rosa_img = pygame.image.load('imagens/Among_Us_Rosa.png').convert_alpha()
    rosa_img = pygame.transform.scale(rosa_img, (jogador_WIDTH2, jogador_HEIGHT2))

    branco_img = pygame.image.load('imagens/Among_Us_Branco.png').convert_alpha()
    branco_img = pygame.transform.scale(branco_img, (jogador_WIDTH2, jogador_HEIGHT2))

    roxo_img = pygame.image.load('imagens/Among_Us_Roxo.png').convert_alpha()
    roxo_img = pygame.transform.scale(roxo_img, (jogador_WIDTH2, jogador_HEIGHT2))

    laranja_img = pygame.image.load('imagens/Among_Us_Laranja.png').convert_alpha()
    laranja_img = pygame.transform.scale(laranja_img, (jogador_WIDTH2, jogador_HEIGHT2))

    azul_img = pygame.image.load('imagens/Among_Us_Azul.png').convert_alpha()
    azul_img = pygame.transform.scale(azul_img, (jogador_WIDTH2, jogador_HEIGHT2))
        


    # ----- Inicia estruturas de dados
    game = True

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    FPS = 30

    #Definindo all sprites
    all_sprites = pygame.sprite.Group()
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

    #Criando o personagem preto
    personagem_preto = Preto(preto_img)
    all_sprites.add(personagem_preto)
    ob_preto.add(personagem_preto)

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

    #Jogador para de andar
    player.speedx = 0
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
                    player.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
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
        mensagem = 'ande até o assassino'
        superficie2 = font.render(mensagem, True, red)
        window.blit(superficie2,(383-superficie2.get_rect().width/2,20))

        #Acertou o assassino            
        hit_verde = pygame.sprite.spritecollide(player, ob_verde, False)
        if len(hit_verde) == 1:
            text = 'Parabéns, você acertou! :D'
           
        
        #Errou o assassino
        hit_vermelho = pygame.sprite.spritecollide(player, ob_vermelho, False)
        hit_amarelo = pygame.sprite.spritecollide(player, ob_amarelo, False)
        hit_preto = pygame.sprite.spritecollide(player, ob_preto, False)
        hit_rosa = pygame.sprite.spritecollide(player, ob_rosa, False)
        hit_branco = pygame.sprite.spritecollide(player, ob_branco, False)
        hit_roxo = pygame.sprite.spritecollide(player, ob_roxo, False)
        hit_laranja = pygame.sprite.spritecollide(player, ob_laranja, False)
        hit_azul = pygame.sprite.spritecollide(player, ob_azul, False)
        if len(hit_vermelho) == 1 or len(hit_amarelo) == 1 or len(hit_preto) == 1 or len(hit_rosa) == 1 or len(hit_branco) == 1 or len(hit_roxo) == 1 or len(hit_laranja) == 1 or len(hit_azul) == 1:
            text = 'Você errou, reinicie e tente de novo :('
            

        #Criando padrões para formato do texto
        superficie = font.render(text, True, white)

        #Posição do texto
        window.blit(superficie,(383-superficie.get_rect().width/2,286))


        # ----- Gera saídas
        
        all_sprites.update()
        
        all_sprites.draw(window)
        
        pygame.display.update()  # Mostra o novo frame para o jogador

        #fim
        if len(hit_vermelho) == 1 or len(hit_amarelo) == 1 or len(hit_preto) == 1 or len(hit_rosa) == 1 or len(hit_verde) or len(hit_branco) == 1 or len(hit_roxo) == 1 or len(hit_laranja) == 1 or len(hit_azul) == 1:
            pygame.time.delay(2000)
            pygame.quit()
    
pygame.quit()


    