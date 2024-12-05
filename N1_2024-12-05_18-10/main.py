import pygame

if __name__ == '__main__':
    try:
        a, n = map(int, input().split())

        pygame.init()
        size = a, a
        my_screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Шахматная клетка')
        clock = pygame.time.Clock()
        running = True

        flag = True
        for i in range(n):
            for j in range(n):
                pygame.draw.rect(my_screen, 'black' if flag else 'white',
                                 ((j * a // n, i * a // n), (j * a // n + i * n, i * a // n + i * n)))
                flag -= flag

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
