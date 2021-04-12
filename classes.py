#Importando biblioteca
import pygame

#Criando tela
WIDTH = 383*2
HEIGHT = 286*2

def toca_musica(musica):
    mixer.music.load(musica)
    mixer.music.play(-1)

#Criando classes dos personagens
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        #Construindo a classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        #Criando variáveis para o jogador olhar para a esquerda e a direita
        jogador_WIDTH = 50
        jogador_HEIGHT = 70
        self.jogador_img_esq = pygame.image.load('imagens/Among_Us_detetive_esq.png').convert_alpha()
        self.jogador_img_esq = pygame.transform.scale(self.jogador_img_esq, (jogador_WIDTH, jogador_HEIGHT))
        self.jogador_img_dir = pygame.image.load('imagens/Among_Us_detetive.png').convert_alpha()
        self.jogador_img_dir = pygame.transform.scale(self.jogador_img_dir, (jogador_WIDTH, jogador_HEIGHT))

        self.image = self.jogador_img_dir
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.centery = HEIGHT - 380
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

#Criando classes dos personagens
class Verde(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 270
        self.rect.centery = HEIGHT - 200

class Vermelho(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 120
        self.rect.centery = 250

class Amarelo(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 370
        self.rect.centery = HEIGHT - 80

class Preto(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 390
        self.rect.centery = 230

class Quadro(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 450
        self.rect.centery = 230

class Rosa(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 190
        self.rect.centery = HEIGHT - 465

class Branco(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 540
        self.rect.centery = HEIGHT - 220

class Roxo(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 600 
        self.rect.centery = HEIGHT - 50

class Laranja(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 65
        self.rect.centery = HEIGHT - 70
    
class Azul(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 500
        self.rect.centery = HEIGHT - 400

#Criando classe do título
class Titulo(pygame.sprite.Sprite):
        def __init__(self, img):
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.centery = 210