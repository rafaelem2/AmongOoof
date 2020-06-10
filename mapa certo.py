#------Inicialização-----
#Importando bibliotecas
import pygame
import math
import time

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

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Jogador(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        
    def update(self):
        # Atualização da posição do personagem
        self.rect.x += self.speedx
        self.rect.y -= self.speedy

        posicaox = self.rect.x
        posicaoy = self.rect.y

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
        self.rect.centerx = WIDTH - 60
        self.rect.centery = HEIGHT - 70


# ----- Inicia estruturas de dados
game = True

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

#Definindo all sprites
all_sprites = pygame.sprite.Group()
ob = pygame.sprite.Group()

# Criando o jogador
player = Jogador(jogador_img)
all_sprites.add(player)

#Criando o personagem verde
personagem_verde = Verde(verde_img)
all_sprites.add(personagem_verde)
ob.add(personagem_verde)

#Definindo o valor RGB para branco, verde e azul (cores das fontes)
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 

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
    pygame.display.blit = (superficie_textinho, retangulo_textinho)
    #
    pygame.display.update()

    #time.sleep(3)

#Criando a função da fala do personagem verde
def fala_verde():
    message_display('Eu sou o assassino')

#Criando contador
contador = 0

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
    hit_verde = pygame.sprite.spritecollide(player, ob, False)
    if len(hit_verde) == 1:
        fala_verde()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor preta
    window.blit(background, (0, 0))
    #window.blit(jogador, (meteor_x, meteor_y))

    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

