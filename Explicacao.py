#Importando bibliotecas
import pygame

def explicacao(window):
    #Criando tela
    WIDTH = 383*2
    HEIGHT = 286*2

    #Criando o personagem assassino
    rosa_img = pygame.image.load('imagens/Among_Us_Rosa_esq.png').convert_alpha()
    rosa_img = pygame.transform.scale(rosa_img, (125, 150))

    #Criando fundo
    cadeia = pygame.image.load('imagens/cadeia.png').convert() 
    cadeia = pygame.transform.scale(cadeia, (WIDTH, 140))

    #Definindo all sprites
    all_sprites = pygame.sprite.Group()

    class Rosa(pygame.sprite.Sprite):
        def __init__(self, img):
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH - 100
            self.rect.centery = HEIGHT - 350
    
    #Criando o personagem rosa
    personagem_rosa = Rosa(rosa_img)
    all_sprites.add(personagem_rosa)


    # ----- Inicia estruturas de dados
    game = True

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    FPS = 30


    #Criando a cor branco
    red = (255,255,255)

    #Criando variáveis
    mensagem_final = ''

    #Criando a fonte para o texto
    font_fim = pygame.font.SysFont(None, 40)


    while game:

        clock.tick(FPS)
        window.fill((0, 0, 0))  # Preenche com a cor preta

        mensagem_final= 'Obrigado pelo trabalho! O policial rosa está preso'
        superficie_1 = font_fim.render(mensagem_final, True, red)
        window.blit(superficie_1,(383-superficie_1.get_rect().width/2, 20))

        mensagem_final2 = 'O policial viu o dono do museu correndo com o quadro'
        superficie_2 = font_fim.render(mensagem_final2, True, red)
        window.blit(superficie_2,(383-superficie_2.get_rect().width/2, 60))

        mensagem_final3 = 'que salvou do incêndio, achou que ele'
        superficie_3 = font_fim.render(mensagem_final3, True, red)
        window.blit(superficie_3,(383-superficie_3.get_rect().width/2, 100))

        mensagem_final4 = 'estava roubando e atirou'
        superficie_4 = font_fim.render(mensagem_final4, True, red)
        window.blit(superficie_4,(383-superficie_4.get_rect().width/2, 140))

        mensagem_final5 = ''
        superficie_5 = font_fim.render(mensagem_final5, True, red)
        window.blit(superficie_5,(383-superficie_5.get_rect().width/2, 100))

        mensagem_final6 = ''
        superficie_6 = font_fim.render(mensagem_final6, True, red)
        window.blit(superficie_6,(383-superficie_6.get_rect().width/2, 100))

        mensagem_final7 = ''
        superficie_7 = font_fim.render(mensagem_final7, True, red)
        window.blit(superficie_7,(383-superficie_7.get_rect().width/2, 100))


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                 #Aperta para sair
                if event.key == pygame.K_SPACE:
                    pygame.quit()




        # ----- Gera saídas
        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.update()  # Mostra o novo frame para o jogador
        window.blit(cadeia, (0, 0))

    pygame.quit()
