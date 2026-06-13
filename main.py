import pygame
from map import Mapa
from player import Player
from obstacle_manager import ObstacleManager

pygame.init()

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

mapp = Mapa()
player = Player(mapp.GROUND_Y)
obstacles = ObstacleManager(mapp)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    keys = pygame.key.get_pressed()

    screen.fill("black")
 
    mapp.update()

    if keys[pygame.K_s]:
        player.duck(screen)
    else:
        player.run(screen)

    player.update()

    obstacles.update(mapp.speed)
    obstacles.draw(screen)

    if obstacles.check_collision(player.get_hitbox()):
        running = False

    mapp.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()          