import pygame
from images import *

class Player:
    def __init__(self):
        self.x = 100
        self.y = 400
        self.width = 64
        self.height = 64
        self.size = 64
        self.speed = 450 # px/s
        self.destroyed = False

        self.ship = Images.player
        self.explosion = Images.explosion
    
    def move_up(self, dy, elapsed_time):
        self.y -= dy*elapsed_time
    
    def move_down(self, dy, elapsed_time):
        self.y += dy*elapsed_time

    def destroy(self):
        self.destroyed = True

    def check_position(self, height):
        if self.y < 0:
            self.y = 0
        if self.y > height - self.height:
            self.y = height - self.height

    def draw(self, win):
        win.blit(self.ship, (self.x,self.y))
        if self.destroyed:
            win.blit(self.explosion, (self.x, self.y))