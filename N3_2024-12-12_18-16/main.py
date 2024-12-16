import pygame
from copy import deepcopy


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


class Life(Board):
    def __init__(self, width: int, height: int, screen: pygame.surface.Surface):
        super().__init__(width, height, screen)
        self.new_board = [[Cell() for _ in range(width)] for _ in range(height)]

    def next_move(self, enabled: bool = False):
        if enabled:
            for x in range(self.w):
                for y in range(self.h):
                    s = sum([])
                    if s in (2, 3):
                        self.new_board[y][x] = Cell(True)
                    elif s > 3 or s < 2:
                        self.new_board[y][x] = Cell(False)
            self.board = deepcopy(self.new_board)
            self.new_board = [[Cell() for _ in range(self.w)] for _ in range(self.h)]


class Cell:
    def __init__(self, alive: bool = False):
        self.c = ('#000000', '#FFFFFF')
        self.val = alive

    def change(self) -> None:
        self.c = self.c[-1], *self.c[:-1]
        self.val = False if self.val else True

    def color(self) -> str:
        return self.c[0]

    def __bool__(self) -> bool:
        return self.val


def main() -> None:
    """main function of the project"""
    pygame.init()
    size = width, height = 940, 940
    screen = pygame.display.set_mode(size)
    life = Life(30, 30, screen)
    life.set_view(20, 20, 30)
    clock = pygame.time.Clock
    running = True
    flag = False
    fps = 20

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                life.get_click(event.pos)
            if event.type == pygame.K_SPACE:
                flag = not flag
            if event.type == pygame.BUTTON_WHEELUP:
                fps += 1
            if event.type == pygame.BUTTON_WHEELDOWN:
                fps -= 1

        screen.fill("#3F3020")
        life.render()
        life.next_move(flag)

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    main()
