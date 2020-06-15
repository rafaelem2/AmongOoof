#Importando bibliotecas
import pygame
from principal import *
from pygame import mixer

#Inicializando
pygame.init()

#Criando tela
WIDTH = 383*2
HEIGHT = 286*2
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Among OOOF')
 
#Criando variáveis
text = ''
mensagem = ''

#Criando fundo
fundo = pygame.image.load('imagens/museu_fogo.png').convert()
fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))

#Criando o título
titulo_img = pygame.image.load('imagens/titulo_among_ooof.png').convert()
titulo_img = pygame.transform.scale(titulo_img, (203, 47))

#Criando a fonte para o texto
font_ola = pygame.font.SysFont(None, 80)
font_outros = pygame.font.SysFont(None, 30)

#Criando a cor branca
white = (255, 255, 255) 
blood = (208, 35, 44)

# ----- Inicia estruturas de dados
game = True

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30
    
#Definindo all sprites
all_sprites = pygame.sprite.Group()

#Criando o título
titulo = Titulo(titulo_img)
all_sprites.add(titulo)

#Criando o personagem morto
preto_img = pygame.image.load('imagens/morto.png').convert_alpha()
preto_img = pygame.transform.scale(preto_img, (150, 125))

class Preto(pygame.sprite.Sprite): 
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = (HEIGHT/2) + 220

#Criando o personagem preto
personagem_preto = Preto(preto_img)
all_sprites.add(personagem_preto)

#Colocando a música de abertura
mixer.music.load('sons/abertura.mp3')
mixer.music.play(-1)

while game:
    #Começando a contagem de tempo
    tempo_principal = pygame.time.get_ticks()

    clock.tick(FPS)

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
    
    mensagem5 = 'use as setas para andar pelo mapa,'
    superficie_5 = font_outros.render(mensagem5, True, blood)
    window.blit(superficie_5,(383-superficie_5.get_rect().width/2, 90))

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    
    #Para o final
    if tempo_principal >= 10000:
        Principal(window)

    # ----- Gera saídas
    all_sprites.update()
    all_sprites.draw(window)
    pygame.display.update()  # Mostra o novo frame para o jogador
    window.blit(fundo, (0, 0))

pygame.quit()
