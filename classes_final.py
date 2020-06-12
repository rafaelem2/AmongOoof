import pygame

WIDTH = 383*2
HEIGHT = 286*2

class Jogador(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)

        #Criando variáveis para o jogador olhar para a esquerda e a direita
        jogador_WIDTH = 80
        jogador_HEIGHT = 80
        self.jogador_img_esq = pygame.image.load('imagens/Among_Us_detetive_esq.png').convert_alpha()
        self.jogador_img_esq = pygame.transform.scale(self.jogador_img_esq, (jogador_WIDTH, jogador_HEIGHT + 20))
        self.jogador_img_dir = pygame.image.load('imagens/Among_Us_detetive.png').convert_alpha()
        self.jogador_img_dir = pygame.transform.scale(self.jogador_img_dir, (jogador_WIDTH, jogador_HEIGHT + 20))

        self.image = self.jogador_img_dir
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        
    def update(self):
        # Atualização da posição do personagem
        self.rect.x += self.speedx
        self.rect.y -= self.speedy

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
           
class Verde(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 116
        self.rect.centery = HEIGHT - 200

class Vermelho(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 650
        self.rect.centery = HEIGHT - 200

class Amarelo(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 266
        self.rect.centery = HEIGHT - 100

class Rosa(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 116
        self.rect.centery = HEIGHT - 372

class Branco(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 650
        self.rect.centery = HEIGHT - 372

class Roxo(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 500 
        self.rect.centery = HEIGHT - 100

class Laranja(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 500   
        self.rect.centery = HEIGHT - 472
    
class Azul(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 266
        self.rect.centery = HEIGHT - 472