import pygame
import random

# Initialisiere pygame
pygame.init()

# Spiel-Fenster
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Farben
white = (255, 255, 255)
pastel_pink = (255, 182, 193)
pastel_purple = (216, 191, 216)
black = (0, 0, 0)

# Snake-Blockgröße
block_size = 10

# Schriftart
font_style = pygame.font.SysFont('bahnschrift', 25, bold=True)

# Snake
def draw_snake(block_size, snake_body):
    for x in snake_body:
        pygame.draw.rect(screen, pastel_pink, [x[0], x[1], block_size, block_size])

# Herz (für das Futter)
def draw_heart(x, y):
    # Erstelle ein einfaches Herz mit Polygonen
    heart = [
        (x, y + 3), 
        (x + 5, y), 
        (x + 10, y + 3),
        (x + 10, y + 8), 
        (x + 5, y + 15), 
        (x, y + 8)
    ]
    pygame.draw.polygon(screen, pastel_purple, heart)

# Spiel-Schleife
def gameLoop():
    game_over = False
    game_close = False

    # Snake Startposition
    x = screen_width / 2
    y = screen_height / 2
    x_change = 0
    y_change = 0

    snake_body = []
    length_of_snake = 1

    # Futter Position
    foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            screen.fill(white)
            message = font_style.render("Oh nooo, you lose! Press Q for Quit or C and try again, babe", True, (255, 105, 180))
            screen.blit(message, [screen_width / 6, screen_height / 3])
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        # Wenn die Snake die Wand berührt
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(white)
        draw_heart(foodx, foody)  # Zeichne das Herz statt eines Kreises
        draw_snake(block_size, snake_body)

        # Überprüfe, ob die Snake das Futter isst
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)

        if len(snake_body) > length_of_snake:
            del snake_body[0]

        # Wenn die Snake sich selbst berührt
        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        pygame.display.update()

        # Wenn die Snake das Futter isst
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(15)

    pygame.quit()
    quit()

gameLoop()