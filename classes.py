#Importando biblioteca
import pygame
from pygame import mixer

#Criando tela
WIDTH = 383*2
HEIGHT = 286*2

def toca_musica(musica):
    mixer.music.load(musica)
    mixer.music.play(-1)

#Criando classes dos personagens
class Jogador(pygame.sprite.Sprite):
    def __init__(self, img, width, height, x, y):
        #Construindo a classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        #Criando variáveis para o jogador olhar para a esquerda e a direita
        jogador_WIDTH = 50
        jogador_HEIGHT = 70
        self.jogador_img_esq = pygame.image.load('imagens/Among_Us_detetive_esq.png').convert_alpha()
        self.jogador_img_esq = pygame.transform.scale(self.jogador_img_esq, (width, height))
        self.jogador_img_dir = pygame.image.load('imagens/Among_Us_detetive.png').convert_alpha()
        self.jogador_img_dir = pygame.transform.scale(self.jogador_img_dir, (width, height))

        self.image = self.jogador_img_dir
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = 0
        self.speedy = 0
        
    def update(self):
        #Atualizando a posição do personagem
        self.rect.x += self.speedx
        self.rect.y -= self.speedy

        #Mantendo dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

#Criando classe do título
class Titulo(pygame.sprite.Sprite):
        def __init__(self, img, x, y):
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y

class Personagens(pygame.sprite.Sprite):
    def __init__(self, img,x,y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y