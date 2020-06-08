#------Inicialização-----
#Importando bibliotecas
import pygame
import random

#Inicializando
pygame.init()

#Criando tela
WIDTH = 383
HEIGHT = 286
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Among OOOF')

#Criando o fundo e os personagens
jogador_WIDTH = 200
jogador_HEIGHT = 200
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('imagens/mapa teste.png').convert()
jogador_img = pygame.image.load('imagens/Among_Us_Ciano.png').convert_alpha()
#jogador_img = pygame.transform.scale(jogador_img, (jogador_WIDTH, jogador_HEIGHT))


# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Jogador(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
           

# ----- Inicia estruturas de dados
game = True

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando o jogador
all_sprites = pygame.sprite.Group()
player = Jogador(jogador_img)
all_sprites.add(player)

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor preta
    window.blit(background, (0, 0))
    #window.blit(jogador, (meteor_x, meteor_y))

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

