import pygame
import random

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (255, 255, 255)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cute Moving Cats")
clock = pygame.time.Clock()


class MovingImage:
    def __init__(self, image_path , start_x, start_y, speed):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))

        # Position
        self.x = start_x
        self.y = start_y

        # Speed
        self.speed = speed

    def update(self):
        # Move image
        self.x += self.speed
        if self.x > SCREEN_WIDTH:
            self.x = -self.image.get_width()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


image_objects = [
    MovingImage("cat_image.png",
                start_x=random.randint(0, SCREEN_WIDTH),
                start_y=random.randint(0, SCREEN_HEIGHT - 100),
                speed=random.randint(2, 6))
    for _ in range(7)
]

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    for obj in image_objects:
        obj.update()
        obj.draw(screen)

    pygame.display.flip()

pygame.quit()

image_objects = [
    MovingImage("cat_image.png",
                start_x=random.randint(0, SCREEN_WIDTH),
                start_y=random.randint(0, SCREEN_HEIGHT - 100),
                speed=random.randint(2, 6))
    for _ in range(5)
]
