import pygame

if __name__ == '__main__':
    try:
        w, h = map(int, input().split())

        pygame.init()
        size = w, h
        my_screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Прямоугольник')
        clock = pygame.time.Clock()
        running = True

        pygame.draw.rect(my_screen, 'red', ((1, 1), (w - 1, h - 1)))
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
