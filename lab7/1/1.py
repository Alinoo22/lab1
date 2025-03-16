import pygame
import sys
import math
from datetime import datetime
pygame.init()
clock_image = pygame.image.load("clock.png")
min_hand = pygame.image.load("min_hand.png")
sec_hand = pygame.image.load("sec_hand.png")

width,height = clock_image.get_size()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Mickey Mouse Clock")
clock_center = (width // 2,height // 2)

def rotate(surf,image,angle,pivot):
    rotated_image = pygame.transform.rotate(image,angle)
    new_rect = rotated_image.get_rect(center=pivot)
    surf.blit(rotated_image, new_rect.topleft)
running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(clock_image,(0, 0))  

    now = datetime.now()
    

    minutes = now.minute
    seconds = now.second
    min_angle = -(minutes * 6)+90
    sec_angle = -(seconds * 6)+90
    rotate(screen,min_hand,min_angle,clock_center)
    rotate(screen,sec_hand,sec_angle,clock_center)

    pygame.display.flip() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()

