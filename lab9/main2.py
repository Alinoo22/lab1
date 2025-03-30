import pygame
import random
import sys
pygame.init()
# Размеры окна
W, H = 600, 400
size = 20
row, col = H // size, W // size
# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
snake = [(W // 2, H // 2)]  # Начальная позиция змеи
snake_act = (size, 0)  # движения змейки
speed = 10

# Очки и уровень
score = 0
level = 1

# ЭКРАН
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

food_types = {
    "norm": (RED, 1),  # Красная еда --> 1 очко
    "bonus": (YELLOW, 3),  # Жёлтая еда ---->3 очка,но быстро исчезает
}

# Таймер исчезновения еды
food_timer = 0
food_lifetime = 100  # Время существования еды в кадрах

#  генерации случайного местоположения еды
def FOOD ():
    while True:
        x = random.randint(0, col - 1) * size
        y = random.randint(0, row - 1) * size
        if (x, y) not in snake:
            return x, y

# Начальная еда
food = FOOD()
current_food_type = "norm"

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, size, size))

def draw_food():
    color, _ = food_types[current_food_type]
    pygame.draw.rect(screen, color, (*food, size, size))

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
            if event.key == pygame.K_UP and snake_act != (0, size):
                snake_act = (0, -size)
            elif event.key == pygame.K_DOWN and snake_act != (0, -size):
                snake_act = (0, size)
            elif event.key == pygame.K_LEFT and snake_act != (size, 0):
                snake_act = (-size, 0)
            elif event.key == pygame.K_RIGHT and snake_act != (-size, 0):
                snake_act = (size, 0)
    
    # Движение змейки
    new_head = (snake[0][0] + snake_act[0], snake[0][1] + snake_act[1])
    
    # Столкновение со стенами
    if new_head[0] < 0 or new_head[0] >= W or new_head[1] < 0 or new_head[1] >= H:
        running = False
    
    # Столкновение с собой
    if new_head in snake:
        running = False
    
    # Добавление новой головы
    snake.insert(0, new_head)
    
   
    if new_head == food:
        score += food_types[current_food_type][1]  # Добавляем очки в зависимости от типа еды
        food = FOOD()
        food_timer = 0  # Сбрасываем таймер
        current_food_type = random.choice(["norm", "bonus"]) 
        # Увеличение уровня каждые 5 очков
        if score % 5 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()  # Убираем хвост,если не съели еду
    
   
    food_timer += 1
    if food_timer > food_lifetime and current_food_type == "bonus":
        food = FOOD()
        food_timer = 0
        current_food_type = "norm"  # После исчезновения бонусной еды появляется обычная
    
   
    draw_snake()
    draw_food()
    draw_score()
    pygame.display.flip()
    clock.tick(speed)  

pygame.quit()
sys.exit()