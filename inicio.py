import pygame

def Inicio(window):
    #Criando tela
    WIDTH = 383*2
    HEIGHT = 286*2

    #Criando variáveis
    text = ''
    mensagem = ''

    #Criando a cor branca
    white = (255, 255, 255) 
    red = (255,0,0)

    # ----- Inicia estruturas de dados
    game = True

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    FPS = 30

   
    


    while game:
        clock.tick(FPS)
        window.fill((0, 0, 0)) # Preenche com a cor preta

        #Escrevendo os textos
        mensagem1 = 'Olá, detetive!'
        superficie_1 = font.render(mensagem, True, red)
        window.blit(superficie_1,(383-superficie_1.get_rect().width/2, 20))

        mensagem2 = 'Converse com os personagens e \n descubra quem é o impostor'
        superficie_2 = font.render(mensagem, True, red)
        window.blit(superficie2,(383-superficie_2.get_rect().width/2, 400))

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False

            #Verifica se apertou alguma tecla
            if event.type == pygame.KEYDOWN:
                #Dependendo da tecla, altera a velocidade
                if event.key == pygame.K_KP_ENTER:
                    break

        # ----- Gera saídas
        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.update()  # Mostra o novo frame para o jogador

pygame.quit()