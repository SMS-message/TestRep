import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
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

    pygame.draw.circle(screen, "#303030", player_pos, 40)

    keys = pygame.key.get_pressed()

    if player_pos.x <= 0:
        player_pos.x += 10
        continue
    elif player_pos.x >= 1280:
        player_pos.x -= 10
        continue
    elif player_pos.y <= 0:
        player_pos.y += 10
        continue
    elif player_pos.y >= 720:
        player_pos.y -= 10
        continue
    if keys[pygame.K_w]:
        player_pos.y -= 25
    if keys[pygame.K_s]:
        player_pos.y += v * dt
    if keys[pygame.K_a]:
        player_pos.x -= v * dt
    if keys[pygame.K_d]:
        player_pos.x += v * dt
    if keys[pygame.K_UP]:
        v += 25
    if keys[pygame.K_DOWN]:
        v -= 25 if v > 0 else 0

    if player_pos.y > 0 and not keys[pygame.K_w]:
        player_pos.y += 10
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
