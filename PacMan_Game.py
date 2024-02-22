import pygame
from PacMan_Class import PacMan, Ghost

pygame.init()

# Constantes
tilesize = 32
size = (28, 12)
fps = 30
player_speed = 150
next_move = 0
show_grid = True

ground_color = "#000000"
player_image = pygame.image.load("Images\PacMan.png")
player_image = pygame.transform.scale(player_image, (tilesize, tilesize))
wall_color = "#0000FF"
ghost_image = pygame.image.load("Images\Ghost.png")
ghost_image = pygame.transform.scale(ghost_image, (tilesize, tilesize))

screen = pygame.display.set_mode((size[0] * tilesize, size[1] * tilesize))
clock = pygame.time.Clock()
DeltaTime = 0

keys = {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0}

player_pos = pygame.Vector2(1, 6)
ghost_list = [Ghost((1, 1)), Ghost((1, 2)), Ghost((1, 3))]

game_map = PacMan(28, 12, 'Level1.csv', pygame.Color(wall_color))
game_map.ReadFile()

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
        elif keys["DOWN"] == 1:
            next_player_pos.y += 1
        elif keys["LEFT"] == 1:
            next_player_pos.x -= 1
        elif keys["RIGHT"] == 1:
            next_player_pos.x += 1

        if game_map.GetMatrice()[int(next_player_pos.y)][int(next_player_pos.x)] != 1:
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

        next_ghost_positions = []
        for ghost in ghost_list:
            next_ghost_positions.append(ghost.move_random(player_pos, size, game_map.GetMatrice()))

        for i, ghost in enumerate(ghost_list):
            ghost.position = next_ghost_positions[i]

    game_map.DrawMap(screen, tilesize)

    for ghost in ghost_list:
        screen.blit(ghost_image, (int(ghost.position.x * tilesize), int(ghost.position.y * tilesize)))

    screen.blit(player_image, (int(player_pos.x * tilesize), int(player_pos.y * tilesize)))

    pygame.display.flip()
    DeltaTime = clock.tick(fps)

pygame.quit()