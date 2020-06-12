import pygame
from principal import *

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

#Criando a fonte para o texto
font = pygame.font.SysFont(None, 48)

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

#Criando o personagem morto
preto_img = pygame.image.load('imagens/morto.png').convert_alpha()
preto_img = pygame.transform.scale(preto_img, (200,180))

class Preto(pygame.sprite.Sprite): 
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2

#Criando o personagem preto
personagem_preto = Preto(preto_img)
all_sprites.add(personagem_preto)

while game:
    clock.tick(FPS)
    window.fill((255, 255, 255)) # Preenche com a cor branco

    #Escrevendo os textos
    mensagem1 = 'Olá, detetive!'
    superficie_1 = font.render(mensagem1, True, blood)
    window.blit(superficie_1,(383-superficie_1.get_rect().width/2, 20))

    mensagem2 = 'converse com os personagens'
    superficie_2 = font.render(mensagem2, True, blood)
    window.blit(superficie_2,(383-superficie_2.get_rect().width/2, 450))

    mensagem3 = 'e descubra quem é o impostor'
    superficie_3 = font.render(mensagem3, True, blood)
    window.blit(superficie_3,(383-superficie_3.get_rect().width/2, 500))

    mensagem4 = 'aperte espaço para começar'
    superficie_4 = font.render(mensagem4, True, blood)
    window.blit(superficie_4,(383-superficie_4.get_rect().width/2, 100))

    mensagem5 = 'use as setas para andar pelo mapa,'
    superficie_5 = font.render(mensagem5, True, blood)
    window.blit(superficie_5,(383-superficie_5.get_rect().width/2, 400))

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        #Verifica se apertou alguma tecla
        if event.type == pygame.KEYDOWN:
            #Dependendo da tecla, altera a velocidade
            if event.key == pygame.K_SPACE:
                Principal(window)
                tempo_principal = pygame.time.get_ticks()

    # ----- Gera saídas
    all_sprites.update()
    all_sprites.draw(window)
    pygame.display.update()  # Mostra o novo frame para o jogador

pygame.quit()