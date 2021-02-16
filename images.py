import pygame


class Images:
    player = pygame.image.load('sprites/ship.png')
    enemy = pygame.image.load('sprites/ship_enemy.png')
    explosion = pygame.image.load('sprites/explosion.png')

    def convert_alpha():
        Images.player.convert_alpha()
        Images.enemy.convert_alpha()
        Images.explosion.convert_alpha()

Images.enemy = pygame.transform.rotate(Images.enemy, 90)
Images.player = pygame.transform.rotate(Images.player, -90)