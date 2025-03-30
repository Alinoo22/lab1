import pygame, sys
from pygame.locals import *
import random, time
pygame.init()

# размер и счетчик
W= 400
H = 600
SPEED = 5
SCORE = 0
COINS = 0  
WEIGHT = 0
# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
#Настройка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
# изображения
background = pygame.image.load("background.png")

# настройка и тема экрана
DISPLAYSURF = pygame.display.set_mode((W,H))
pygame.display.set_caption("Alino's Game")

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lambprgin.png")
        self.image = pygame.transform.scale(self.image, (65, 120))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)  # Добавляем маску
        self.rect.center = (random.randint(40,W- 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top >H:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, W- 40), 0)
# Класс игрока 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tank.png")
        self.image = pygame.transform.scale(self.image, (80, 150))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)  # Добавляем маску
        self.rect.center = (W// 2, H- 100)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < W and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


# Класс монет с разными весами
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choice([("coin1.png", 1), ("coin3.png", 3), ("coin5.png", 5)])  # Монеты с разным весом
        self.image = pygame.image.load(self.type[0])
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.value = self.type[1]
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,W- 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top >H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W- 40), 0)

# Создание объектов
P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()
for _ in range(2):  # Две монеты на дороге
    coins.add(Coin())

#спрайты
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, *coins)

#увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
FramePerSec = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Отображение фона
    DISPLAYSURF.blit(background, (0, 0))

    # Отображение счета
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_collected = font_small.render(f"Coins: {COINS} (Weight: {WEIGHT})", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_collected, (10, 40))

   
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    #столкновения с противником
    if pygame.sprite.spritecollideany(P1, enemies, pygame.sprite.collide_mask):
        crash_sound = pygame.mixer.Sound('crash.wav')
        crash_sound.play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    #  столкновения с монетами
    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            COINS += 1
            WEIGHT += coin.value
            coin.rect.top = 0
            coin.rect.center = (random.randint(40, W- 40), 0)

    # Увеличение скорости врага при наборе 5, 10, 15 монет
    if COINS in [5, 10, 15]:
        SPEED += 1
        COINS += 1  # Чтобы скорость увеличивалась только один раз на N монет
    
    pygame.display.update()
    FramePerSec.tick(60)
