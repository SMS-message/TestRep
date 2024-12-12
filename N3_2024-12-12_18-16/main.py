import pygame


class Board:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.board = [[None] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen: pygame.surface.Surface) -> None:
        for x in range(self.w):
            for y in range(self.h):
                pygame.draw.rect(screen, pygame.Color('#CCCCCC'), (x * self.cell_size + self.left,
                                                                   y * self.cell_size + self.top,
                                                                   self.cell_size, self.cell_size), 1)

    def set_view(self, left: int, top: int, cell_size: int) -> None:
        self.left = left
        self.top = top
        self.cell_size = cell_size


def main() -> None:
    """main function of the project"""
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    board = Board(18, 12)
    board.set_view(100, 100, 15)
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
