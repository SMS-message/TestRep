import pygame


class Board:
    def __init__(self, width: int, height: int, screen: pygame.surface.Surface):
        self.w = width
        self.h = height
        self.s = screen
        self.board = [[Cell() for _ in range(width)] for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self) -> None:
        for x in range(self.w):
            for y in range(self.h):
                color = self.board[y][x].color()
                pygame.draw.rect(self.s, 'white', (x * self.cell_size + self.left,
                                                   y * self.cell_size + self.top,
                                                   self.cell_size, self.cell_size), 1)
                pygame.draw.rect(self.s, color, (x * self.cell_size + self.left + 1,
                                                 y * self.cell_size + self.top + 1,
                                                 self.cell_size - 2, self.cell_size - 2))

    def set_view(self, left: int, top: int, cell_size: int) -> None:
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, pos: tuple[int, int]) -> None:
        cell = self.get_cell(pos)
        if cell:
            self.on_click(cell)

    def get_cell(self, pos: tuple[int, int]) -> tuple[int, int]:
        x = (pos[0] - self.left) // self.cell_size
        y = (pos[1] - self.top) // self.cell_size
        if 0 < x + 1 <= self.w and 0 < y + 1 <= self.h:
            return x, y

    def on_click(self, cell: tuple[int, int]):
        self.board[cell[1]][cell[0]].change()
        self.render()


class Cell:
    def __init__(self):
        self.c = ('black', 'blue', 'red',)

    def change(self):
        self.c = self.c[2], self.c[0], self.c[1]

    def color(self):
        return self.c[0]


def main() -> None:
    """main function of the project"""
    pygame.init()
    size = width, height = 440, 440
    screen = pygame.display.set_mode(size)
    board = Board(10, 10, screen)
    board.set_view(20, 20, 40)
    clock = pygame.time.Clock()
    running = True
    v = 100
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
                pass
        screen.fill("#121212")
        board.render()

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()
