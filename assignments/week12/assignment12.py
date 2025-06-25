import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Surface & Rectangle Game")

try:
    dino_img = pygame.image.load("dino_s.png")
    dino_img = pygame.transform.scale(dino_img, (50, 50))
    dino_rect = dino_img.get_rect()
except:
    dino_img = None
    dino_rect = pygame.Rect(0, 0, 50, 50)  # fallback if no image

background_surface = pygame.Surface((WIDTH, HEIGHT))
background_surface.fill("darkslategray")
pygame.draw.circle(background_surface, "lightblue", (300, 300), 100)
pygame.draw.rect(background_surface, "orange", pygame.Rect(250, 250, 100, 100), border_radius=10)

player_rect = pygame.Rect(0, 0, 30, 30)

obstacles = []
for _ in range(10):
    rect = pygame.Rect(random.randint(0, WIDTH - 25), random.randint(0, HEIGHT - 25), 25, 25)
    obstacles.append(rect)

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
run = True

while run:
    screen.blit(background_surface, (0, 0))

    mouse_pos = pygame.mouse.get_pos()
    player_rect.center = mouse_pos

    color = "green"
    collision_index = player_rect.collidelist(obstacles)
    if collision_index >= 0:
        color = "red"

    for i, obstacle in enumerate(obstacles):
        obstacle.move_ip(random.choice([-1, 0, 1]), random.choice([-1, 0, 1]))  # tiny movement
        obstacle.clamp_ip(screen.get_rect())  # keep it inside screen
        pygame.draw.rect(screen, "blue", obstacle)

    debug_rect = player_rect.inflate(10, 10)
    pygame.draw.rect(screen, "yellow", debug_rect, 1)

    pygame.draw.rect(screen, color, player_rect)

    if dino_img:
        dino_rect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(dino_img, dino_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
