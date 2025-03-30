import pygame
import random
import sys


pygame.init()

# размеры
W, H = 600, 400
size = 20
row, col = H // size, W // size

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


snake = [(W // 2, H// 2)]  # Начальная позиция
snake_act= (size, 0)  # Направление движения
speed = 10

# Очки и уровни
score = 0
level = 1

# Создание экрана
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# генерации случайного местоположения еды

def FOOD():
    while True:
        x = random.randint(0, col - 1) * size
        y = random.randint(0, row - 1) * size
        if (x, y) not in snake: 
            return x, y

food = FOOD()

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, size, size))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, size, size))

def draw_score():
    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))


running = True
while running:
    screen.fill(BLACK)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_act!= (0, size):
                snake_act= (0, -size)
            elif event.key == pygame.K_DOWN and snake_act != (0, size):
                snake_act = (0,size)
            elif event.key == pygame.K_LEFT and snake_act!= (size, 0):
                snake_act = (-size, 0)
            elif event.key == pygame.K_RIGHT and snake_act!= (-size, 0):
                snake_act = (size, 0)
    
    # Движение змейки
    new_head = (snake[0][0] + snake_act[0], snake[0][1] + snake_act[1])
    
    # столкновение со стенами
    if new_head[0] < 0 or new_head[0] >= W or new_head[1] < 0 or new_head[1] >= H:
        running = False 
    
    # столкновение с самой собой
    if new_head in snake:
        running = False 
    
    # голова змеи
    snake.insert(0, new_head)
    
   
    if new_head == food:
        score += 1
        food = FOOD()
        # Увеличение уровня каждые 3 очка
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()  # Убираем хвост,если не съели еду
    
   
    draw_snake()
    draw_food()
    draw_score()
    pygame.display.flip()
    clock.tick(speed)  # Управление скоростью игры

pygame.quit()
sys.exit()
