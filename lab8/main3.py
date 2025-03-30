import pygame

pygame.init()
# Размер и цвета
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")

# Переменные для работы с инструментами
drawing = False
mode = "brush"  # Modes: "brush", "rectangle", "circle", "eraser"
start_pos = None
selected_color = BLACK
brush_size = 5

running = True
clock = pygame.time.Clock()

# Фоновый слой 
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(WHITE)

while running:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if mode in ["rectangle", "circle"] and start_pos:
                end_pos = event.pos
                if mode == "rectangle":
                    pygame.draw.rect(background, selected_color, pygame.Rect(
                        *start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]
                    ), 2)
                elif mode == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 / 2)
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    pygame.draw.circle(background, selected_color, center, radius, 2)
            drawing = False
        elif event.type == pygame.KEYDOWN:
            # Выбор инструментов
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_b:
                mode = "brush"
            # Выбор цветов
            elif event.key == pygame.K_1:
                selected_color = BLACK
            elif event.key == pygame.K_2:
                selected_color = RED
            elif event.key == pygame.K_3:
                selected_color = GREEN
            elif event.key == pygame.K_4:
                selected_color = BLUE
            elif event.key == pygame.K_5:
                selected_color = YELLOW

    # Рисование кистью или ластиком
    if drawing and mode == "brush":
        pygame.draw.circle(background, selected_color, pygame.mouse.get_pos(), brush_size)
    elif drawing and mode == "eraser":
        pygame.draw.circle(background, WHITE, pygame.mouse.get_pos(), brush_size)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

"""
1-5 ---> (Черный, Красный, Зеленый, Синий, Желтый)

R ---> прямоугольник, C ---> круг, B ---> кисть, E ---> ластик
"""
