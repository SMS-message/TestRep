import pygame
from random import random


def draw1(screen: pygame.surface.Surface):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, PyGame!", True, (255, 204, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0),
                     (text_x - 10, text_y - 10,
                      text_w + 20, text_h + 20),
                     1)


def draw_square(screen: pygame.surface.Surface):
    color = pygame.Color(50, 150, 50)
    pygame.draw.rect(screen, color, (20, 20, 100, 100), 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3])
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


def draw_pixels(screen: pygame.surface.Surface):
    for _ in range(3000):
        screen.fill(pygame.Color('white'), (random() * width, random() * height, 20, 2))


def draw_polygon(screen: pygame.surface.Surface):
    pygame.draw.polygon(screen, pygame.Color((255, 204, 0)),
                        [(0, 150), (200, 250), (100, 350)])


if __name__ == '__main__':
    pygame.init()
    size = width, height = (800, 600)
    my_screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw1(my_screen)
        draw_square(my_screen)
        draw_polygon(my_screen)
        draw_pixels(my_screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
