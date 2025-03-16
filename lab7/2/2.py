import pygame
import sys
import pygame.mixer

pygame.init()
pygame.mixer.init()
pygame.font.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music player")

music_album = [
    r"C:\Users\Admin\Downloads\Ariana_Grande_Social_House_-_boyfriend_65861838.mp3",#0
    r"C:\Users\Admin\Downloads\The_Neighbourhood_-_Sweater_Weather_47959107.mp3",#1
    r"C:\Users\Admin\Downloads\Radiohead_-_Creep_48022418.mp3",#2
    r"C:\Users\Admin\Downloads\IOWA_-_Radost_47949841.mp3",#3
    r"C:\Users\Admin\Downloads\IOWA_-_Ulybajjsya_47949842.mp3",#4
    r"C:\Users\Admin\Downloads\IOWA_-_Marshrutka_48051532.mp3"#5
]

music_pictures = [
    pygame.image.load(r"C:\Users\Admin\Downloads\sweater_weather.png"),#0
    pygame.image.load(r"C:\Users\Admin\Downloads\creep.png"),#1
    pygame.image.load(r"C:\Users\Admin\Downloads\boyfriend.png"),#2
    pygame.image.load(r"C:\Users\Admin\Downloads\улыбайся.png")#3
]

music_names = [
    "Boyfriend",
    "Sweater Weather",
    "Creep",
    "Radost",
    "Ulybaisya",
    "Marshrutka"
]

def start_music(index):
    pygame.mixer.music.load(music_album[index])
    pygame.mixer.music.play()

track = 0

MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)

start_music(track)
is_paused = False

font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 150, HEIGHT // 2 - 180, 300, 300), 2)

    if track == 1:
        image = music_pictures[0]  # The_Neighbourhood
    elif track == 2:
        image = music_pictures[1]  # Radiohead
    elif track == 0:
        image = music_pictures[2]  # Ariana_Grande_Social_House
    elif track in [3, 4, 5]:
        image = music_pictures[3]  # IOWA

    image = pygame.transform.scale(image, (300, 300))
    screen.blit(image, (WIDTH // 2 - 150, HEIGHT // 2 - 180))

    track_text = font.render(music_names[track], True, (255, 255, 255))
    text_rect = track_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 140))
    screen.blit(track_text, text_rect)

    pygame.draw.line(screen, (255, 255, 255), (WIDTH // 2 - 150, HEIGHT // 2 + 167), (WIDTH // 2 + 150, HEIGHT // 2 + 167), 2)

    pygame.draw.polygon(screen, (255, 255, 255), [
        (WIDTH // 2 - 90, HEIGHT // 2 + 180),
        (WIDTH // 2 - 110, HEIGHT // 2 + 200),
        (WIDTH // 2 - 90, HEIGHT // 2 + 220)
    ])

    pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 15, HEIGHT // 2 + 183, 30, 30))

    pygame.draw.polygon(screen, (255, 255, 255), [
        (WIDTH // 2 + 90, HEIGHT // 2 + 180),
        (WIDTH // 2 + 110, HEIGHT // 2 + 200),
        (WIDTH // 2 + 90, HEIGHT // 2 + 220)
    ])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MUSIC_END:
            track = (track + 1) % len(music_album)
            start_music(track)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                else:
                    pygame.mixer.music.pause()
                    is_paused = True

            elif event.key == pygame.K_RIGHT:
                track = (track + 1) % len(music_album)
                start_music(track)

            elif event.key == pygame.K_LEFT:
                track = (track - 1) % len(music_album)
                start_music(track)

    pygame.display.update()

pygame.quit()
sys.exit()