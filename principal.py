#------Inicialização-----
#Importando bibliotecas
import pygame
import math
import time
from final import *
from classes import *

#Inicializando
pygame.init()

#Criando tela
WIDTH = 383*2
HEIGHT = 286*2
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Among OOOF')

#Criando o fundo e os personagens
jogador_WIDTH = 50
jogador_HEIGHT = 50
font = pygame.font.SysFont(None, 48)

background = pygame.image.load('imagens/mapa teste.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

jogador_img = pygame.image.load('imagens/Among_Us_Ciano.png').convert_alpha()
jogador_img = pygame.transform.scale(jogador_img, (jogador_WIDTH, jogador_HEIGHT))

verde_img = pygame.image.load('imagens/Among_Us_Green.png').convert_alpha()
verde_img = pygame.transform.scale(verde_img, (jogador_WIDTH, jogador_HEIGHT))

vermelho_img = pygame.image.load('imagens/Among_Us_Vermelho.png').convert_alpha()
vermelho_img = pygame.transform.scale(vermelho_img, (jogador_WIDTH, jogador_HEIGHT))

amarelo_img = pygame.image.load('imagens/Among_Us_Amarelo.png').convert_alpha()
amarelo_img = pygame.transform.scale(amarelo_img, (jogador_WIDTH, jogador_HEIGHT))

preto_img = pygame.image.load('imagens/Among_Us_Preto.png').convert_alpha()
preto_img = pygame.transform.scale(preto_img, (jogador_WIDTH, jogador_HEIGHT))

rosa_img = pygame.image.load('imagens/Among_Us_Rosa.png').convert_alpha()
rosa_img = pygame.transform.scale(rosa_img, (jogador_WIDTH, jogador_HEIGHT))

# ----- Inicia estruturas de dados
# Definindo os novos tipos



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

#Definindo o valor RGB para branco, verde e azul (cores das fontes)
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 

#Criando variáveis
text = ''
tempo = pygame.time.get_ticks()
tempo_verde = pygame.time.get_ticks()
tempo_vermelho = pygame.time.get_ticks()
tempo_amarelo = pygame.time.get_ticks()
tempo_preto = pygame.time.get_ticks()
tempo_rosa = pygame.time.get_ticks()

'''
#Criando função para objetos do texto
def objetos_textinho(texto, font):
    superficie = font.render(texto, True, white, blue)
    return superficie, superficie.get_rect()

#Criando função para textos
def message_display(texto):
    textinho = pygame.font.Font('freesansbold.ttf', 60)
    superficie_textinho, retangulo_textinho = objetos_textinho(texto, textinho)
    retangulo_textinho.centerx = WIDTH / 2
    retangulo_textinho.centery = HEIGHT - 60
    pygame.display.blit(superficie_textinho, retangulo_textinho)
    
    #pygame.display.update()

    #time.sleep(3)

#Criando a função da fala do personagem verde
def fala_verde():
    message_display('Eu sou o assassino')
'''

# ===== Loop principal =====
while game:
    clock.tick(FPS)

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

    # ----- Atualiza estado do jogo
    all_sprites.update()

    #Verificando se houve colisão entre o jogador e o personagem verde
    hit_verde = pygame.sprite.spritecollide(player, ob_verde, False)
    if len(hit_verde) == 1:
        #fala_verde()
        text = 'bom dia'
        tempo_verde = pygame.time.get_ticks()
        
    #Verificando se houve colisão entre o jogador e o personagem vermelho
    hit_vermelho = pygame.sprite.spritecollide(player, ob_vermelho, False)
    if len(hit_vermelho) == 1:
        text = 'eae'
        tempo_vermelho = pygame.time.get_ticks()

    #Verificando se houve colisão entre o jogador e o personagem amarelo
    hit_amarelo = pygame.sprite.spritecollide(player, ob_amarelo, False)
    if len(hit_amarelo) == 1:
        text = 'eae'
        tempo_amarelo = pygame.time.get_ticks()

    #Verificando se houve colisão entre o jogador e o personagem preto
    hit_preto = pygame.sprite.spritecollide(player, ob_preto, False)
    if len(hit_preto) == 1:
        text = 'eae'
        tempo_preto = pygame.time.get_ticks()

    #Verificando se houve colisão entre o jogador e o personagem rosa
    hit_rosa = pygame.sprite.spritecollide(player, ob_rosa, False)
    if len(hit_rosa) == 1:
        text = 'eae'
        tempo_rosa = pygame.time.get_ticks()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor preta
    window.blit(background, (0, 0))

    #Criando padrões para formato do texto
    superficie = font.render(text, True, blue)
    tempo = pygame.time.get_ticks()

    #Para o verde
    if tempo - tempo_verde < 1000:
        window.blit(superficie, (0,0))
    #window.blit(jogador, (meteor_x, meteor_y))

    #Para o vermelho
    if tempo - tempo_vermelho < 1000:
        window.blit(superficie, (0,0))

    #Para o amarelo
    if tempo - tempo_amarelo < 1000:
        window.blit(superficie, (0,0))

    #Para o preto
    if tempo - tempo_preto < 1000:
        window.blit(superficie, (0,0))

    #Para o rosa
    if tempo - tempo_rosa < 1000:
        window.blit(superficie, (0,0))

    #Para o final
    if tempo > 10000:
        Final(window)

    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

