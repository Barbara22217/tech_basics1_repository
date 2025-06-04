import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FONT = pygame.font.SysFont("Segoe UI Emoji", 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emoji Drawing Game")

EMOJIS = ["🌸", "🔥", "⭐", "🎨", "🍀", "💧"]


class GameObject:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set_position(self, x, y):
        self._x = x
        self._y = y

    def get_position(self):
        return self._x, self._y

class BrushEmoji(GameObject):
    def __init__(self, x, y, emoji="⭐"):
        super().__init__(x, y)
        self.__emoji = emoji

    def set_emoji(self, emoji):
        self.__emoji = emoji

    def get_emoji(self):
        return self.__emoji

    def draw(self, surface):
        emoji_surface = FONT.render(self.__emoji, True, (0, 0, 0))
        surface.blit(emoji_surface, (self._x, self._y))

def main():
    clock = pygame.time.Clock()
    drawing = False
    brush = BrushEmoji(0, 0, EMOJIS[0])
    drawings = []

    show_instructions = True

    while True:
        screen.fill(WHITE)

        if show_instructions:
            draw_instructions()
        else:

            for b in drawings:
                b.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if show_instructions and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                show_instructions = False

            if not show_instructions:

                if event.type == pygame.KEYDOWN:
                    if event.key in range(pygame.K_1, pygame.K_1 + len(EMOJIS)):
                        index = event.key - pygame.K_1
                        brush.set_emoji(EMOJIS[index])


                if event.type == pygame.MOUSEBUTTONDOWN:
                    drawing = True


                if event.type == pygame.MOUSEBUTTONUP:
                    drawing = False

        if drawing and not show_instructions:
            x, y = pygame.mouse.get_pos()
            new_brush = BrushEmoji(x, y, brush.get_emoji())
            drawings.append(new_brush)

        pygame.display.flip()
        clock.tick(60)

def draw_instructions():
    lines = [
        "Welcome to the Emoji Drawing Game!",
        "Draw with your mouse using emoji brushes.",
        "Press 1-6 to switch between emoji types.",
        "Hold down mouse to draw.",
        "Press SPACE to start.",
        "Press ESC or close the window to quit."
    ]
    for i, line in enumerate(lines):
        text = FONT.render(line, True, (0, 0, 0))
        screen.blit(text, (50, 100 + i * 40))


if __name__ == "__main__":
    main()
