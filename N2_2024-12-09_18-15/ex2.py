import pygame

pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
v = 100
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#121212")

    if event.type == pygame.MOUSEMOTION:
        pygame.draw.circle(screen, "#303030", event.pos, 40)
        pygame.draw.circle(screen, "#303030", (event.pos[0], height - event.pos[1]), 40)
        pygame.draw.circle(screen, "#303030", (width - event.pos[0], event.pos[1]), 40)
        pygame.draw.circle(screen, "#303030", (width - event.pos[0], height - event.pos[1]), 40)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
