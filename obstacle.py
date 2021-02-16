from images import *


class Obstacle:
    def __init__(self, x,y, size=10, speed=300):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

        self.ship = Images.enemy
        self.ship = pygame.transform.scale(self.ship, (self.size, self.size))
    
    def update(self, elapsed_time):
        self.x -= self.speed * elapsed_time

    def draw(self, win):
        win.blit(self.ship, (self.x,self.y))