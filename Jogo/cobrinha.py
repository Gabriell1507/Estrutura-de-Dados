import pygame
import time
import random

pygame.init()

# Definição de cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (0, 255, 255)
blue = (255, 0, 0)

# Configurações da tela
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Jogo da cobrinha feito por Sacola Development Team')

# Configurações do jogo
snake_block = 20
snake_speed = 15

# Definição da fonte e tamanho do texto
font_style = pygame.font.SysFont(None, 30)

class SnakeNode:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.next = None

# Função para desenhar a cobra na tela
def our_snake(snake_head):
    current = snake_head
    while current:
        pygame.draw.rect(dis, current.color, [current.x, current.y, snake_block, snake_block])
        current = current.next

# Função para exibir a mensagem na tela
def Your_score(score):
    value = font_style.render("Sua pontuação: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Função para exibir a mensagem de fim de jogo e oferecer opções de reinício
def Your_score_and_message(score):
    font = pygame.font.SysFont(None, 50)
    value = font.render("Sua pontuação: " + str(score), True, black)
    dis.blit(value, [dis_width / 8, dis_height / 3])

    font = pygame.font.SysFont(None, 25)
    restart_text = font.render("Pressione C para jogar novamente ou Q para sair do jogo", True, black)
    dis.blit(restart_text, [dis_width /8, dis_height / 2])

    pygame.display.update()

# Função para gerar uma cor aleatória
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Função principal do jogo
def gameLoop():
    game_over = False
    game_close = False

    # Posição inicial da cobra
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Variação nas coordenadas para movimentar a cobra
    x1_change = 0
    y1_change = 0

    # Tamanho inicial da cobra
    snake_head = SnakeNode(x1, y1, random_color())
    length_of_snake = 1

    # Posição inicial da comida
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    while not game_over:
        while game_close:
            Your_score_and_message(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Atualiza as coordenadas da cabeça da cobra
        x1 += x1_change
        y1 += y1_change

        # Verifica se a cobra colide com as bordas
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Atualiza a tela
        dis.fill(red)  # Muda a cor da tela para vermelho
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])

        # Atualiza a posição da cabeça da cobra
        new_head = SnakeNode(x1, y1, random_color())
        new_head.next = snake_head
        snake_head = new_head

        # Verifica se a cobra colide com a comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            length_of_snake += 1
        else:
            # Remove a cauda da cobra para manter o tamanho correto
            current = snake_head
            while current.next.next:
                current = current.next
            current.next = None

        our_snake(snake_head)
        Your_score(length_of_snake - 1)

        # Atualiza a taxa de atualização
        pygame.display.update()
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

# Inicia o loop principal do jogo
gameLoop()
