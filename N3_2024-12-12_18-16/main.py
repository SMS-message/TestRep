import pygame


class Board:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.board = [[None] * width for _ in range(height)]
        self.left = 10
        self.right = 10
        self.cell_size = 30

    def render(self, screen: pygame.surface.Surface):
        pass


def main():
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    board = Board(7, 5)
    clock = pygame.time.Clock()
    running = True
    v = 100
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("#121212")
        board.render(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()
