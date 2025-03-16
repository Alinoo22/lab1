import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball")
x_m_ball = WIDTH // 2
y_m_ball = HEIGHT // 2
speed = 20
radius = 25  
running = True
while running:
    screen.fill((255, 255, 255)) 
    pygame.draw.circle(screen, (255, 0, 0), (x_m_ball, y_m_ball), radius) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y_m_ball - radius >= speed:
                y_m_ball -= speed
            elif event.key == pygame.K_DOWN and y_m_ball + radius <= HEIGHT - speed:
                y_m_ball += speed
            elif event.key == pygame.K_LEFT and x_m_ball - radius >= speed:
                x_m_ball -= speed
            elif event.key == pygame.K_RIGHT and x_m_ball + radius <= WIDTH - speed:
                x_m_ball += speed
    pygame.display.flip()
    
pygame.quit()
sys.exit()