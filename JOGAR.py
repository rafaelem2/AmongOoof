#Importando bibliotecas
import pygame
from principal import *
from pygame import mixer
from classes import *

#Inicializando
pygame.init()

#Criando tela
WIDTH = 383*2
HEIGHT = 286*2
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Among OOOF')

#Criando a fonte para o texto
font_ola = pygame.font.SysFont(None, 80)
font_outros = pygame.font.SysFont(None, 30) 

#Criando variáveis
text = ''
mensagem = ''

#Criando as cores
white = (255, 255, 255) 
blood = (208, 35, 44)

#Criando fundo
fundo = pygame.image.load('imagens/museu_fogo.png').convert()
fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))

#Criando o título
titulo_img = pygame.image.load('imagens/titulo_among_ooof.png').convert()
titulo_img = pygame.transform.scale(titulo_img, (203, 47))

#Definindo all sprites
all_sprites = pygame.sprite.Group()

#Criando o título
titulo = Titulo(titulo_img, WIDTH/2, 210)
all_sprites.add(titulo)

#Criando o personagem preto morto
preto_img = pygame.image.load('imagens/morto.png').convert_alpha()
preto_img = pygame.transform.scale(preto_img, (150, 125))

personagem_preto = Personagens(preto_img, WIDTH/2, (HEIGHT/2) + 220 )
all_sprites.add(personagem_preto)


# ----- Inicia estruturas de dados -----
game = True

#Criando variável para ajustar de velocidade
clock = pygame.time.Clock()
FPS = 30

#Colocando a música de abertura
toca_musica('sons/abertura.mp3')

# ===== Loop principal =====
while game:
    #Começando a contagem de tempo
    tempo_principal = pygame.time.get_ticks()
    clock.tick(FPS)

    # ----- Trata eventos -----
    for event in pygame.event.get():
        #Verificando se a pessoa quer sair do jogo
        if event.type == pygame.QUIT:
            game = False

    #Escrevendo os textos
    mensagem1 = 'Olá, detetive!'
    superficie_1 = font_ola.render(mensagem1, True, blood)
    window.blit(superficie_1,(383-superficie_1.get_rect().width/2, 20))

    mensagem2 = 'converse com os personagens'
    superficie_2 = font_outros.render(mensagem2, True, blood)
    window.blit(superficie_2,(383-superficie_2.get_rect().width/2, 120))

    mensagem3 = 'e descubra quem é o impostor'
    superficie_3 = font_outros.render(mensagem3, True, blood)
    window.blit(superficie_3,(383-superficie_3.get_rect().width/2, 150))
    
    mensagem4 = 'use as setas para andar pelo mapa,'
    superficie_4 = font_outros.render(mensagem4, True, blood)
    window.blit(superficie_4,(383-superficie_4.get_rect().width/2, 90))

    #Passando para o final
    if tempo_principal >= 20000:
        Principal(window)

    # ----- Gera saídas e atualiza estado de jogo -----
    all_sprites.update()
    all_sprites.draw(window)
    pygame.display.update()  
    window.blit(fundo, (0, 0))

# ===== Finalização =====
pygame.quit()