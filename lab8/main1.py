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
        self.rect.center = (W// 2,H - 100)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < W and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
# Класс монета
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W- 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > H:
            self.rect.top = 0
            self.rect.center = (random.randint(40,W - 40), 0)
# Создание объектов
P1 = Player()
E1 = Enemy()
C1 = Coin()
# спрайты
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)
# увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
# Игровой цикл
FramePerSec = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 # Отображение фона
    DISPLAYSURF.blit(background, (0, 0))
 # Отображение счета
    scores = font_small.render(str(SCORE), True, RED)
    coins_collected = font_small.render("Coins: " + str(COINS), True, RED)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_collected, (W - 100, 10))

   
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # столкновения с противником 
    if pygame.sprite.spritecollide(P1, enemies, False, pygame.sprite.collide_mask):
        crash_sound = pygame.mixer.Sound('crash.wav')
        crash_sound.play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # столкновения с монетой
    if pygame.sprite.spritecollide(P1, coins, False, pygame.sprite.collide_mask):
        COINS += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, W- 40), 0)

    pygame.display.update()
    FramePerSec.tick(60)
