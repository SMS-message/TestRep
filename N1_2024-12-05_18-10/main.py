import pygame


def check_color(n: int) -> int:
    if n == 1:
        return -1
    if n == 0:
        return 1
    if n < 0:
        return 0
    return check_color(n - 3)


if __name__ == '__main__':
    try:
        w, n = map(int, input().split())
        r = w * n * 2
        pygame.init()
        size = width, height = (r, r)
        my_screen = pygame.display.set_mode(size)
        color_scheme = ((0, 255, 0), (0, 0, 255), (255, 0, 0))
        clock = pygame.time.Clock()
        running = True

        center = r // 2, r // 2
        for i in range(n, 0, -1):
            pygame.draw.circle(my_screen, color_scheme[check_color(n)], center, w * i)
            color_scheme = color_scheme[-1], color_scheme[0], color_scheme[1]
            pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
    except Exception as err:
        print("Неправильный формат ввода")
        quit(1)
