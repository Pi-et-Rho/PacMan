import pygame
from PacMan_Class import PacMan

pygame.init()

# Constantes
tilesize = 32
size = (28, 12)
fps = 30
player_speed = 150
next_move = 0
show_grid = True

ground_color = "#000000"
player_color = "#FFFF00"
wall_color = "#0000FF"

screen = pygame.display.set_mode((size[0] * tilesize, size[1] * tilesize))
clock = pygame.time.Clock()
DeltaTime = 0

keys = {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0}

player_pos = pygame.Vector2(1, 6)

map = PacMan(28, 12, 'Level1.csv', pygame.Color(wall_color))
map.ReadFile()


running = True
while running:
    screen.fill(ground_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                keys["UP"] = 1
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                keys["DOWN"] = 1
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                keys["LEFT"] = 1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                keys["RIGHT"] = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                keys["UP"] = 0
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                keys["DOWN"] = 0
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                keys["LEFT"] = 0
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                keys["RIGHT"] = 0

            if event.key == pygame.K_ESCAPE:
                running = False
        

    next_move += DeltaTime

    if next_move > 0:
        next_player_pos = player_pos.copy()

        if keys["UP"] == 1:
            next_player_pos.y -= 1
            next_move = -player_speed
        elif keys["DOWN"] == 1:
            next_player_pos.y += 1
            next_move = -player_speed
        elif keys["LEFT"] == 1:
            next_player_pos.x -= 1
            next_move = -player_speed
        elif keys["RIGHT"] == 1:
            next_player_pos.x += 1

        if map.GetMatrice()[int(next_player_pos.y)][int(next_player_pos.x)] != 1:
            player_pos = next_player_pos

        if player_pos.y < 0:
            player_pos.y = 0
        if player_pos.y >= size[1]:
            player_pos.y = size[1] - 1
        if player_pos.x < 0:
            player_pos.x = 0
        if player_pos.x > size[0] - 1:
            player_pos.x = size[0] - 1   

        next_move = -player_speed

    map.DrawMap(screen, tilesize)

    pygame.draw.circle(screen, player_color, (int(player_pos.x * tilesize + tilesize // 2), int(player_pos.y * tilesize + tilesize // 2)), tilesize / 2)

    pygame.display.flip()
    DeltaTime = clock.tick(fps)

pygame.quit()