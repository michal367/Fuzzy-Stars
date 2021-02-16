import random
from obstacle import *
from utils import *

class ObstaclesManager:
    def __init__(self, screen_width, screen_height, difficulty):
        self.obstacles = []
        self.elapsed_time = 0

        self.min_size = 24
        self.max_size = 64

        if difficulty == DIFFICULTY_NORMAL:
            self.time_to_obstacle = 0.3 # seconds
            self.min_speed = 600 # px/s
            self.max_speed = 600 # px/s
        elif difficulty == DIFFICULTY_HARD:
            self.time_to_obstacle = 0.15 # seconds
            self.min_speed = 400 # px/s
            self.max_speed = 900 # px/s

        self.screen_width = screen_width
        self.screen_height = screen_height

    
    def add(self):
        size = random.randint(self.min_size, self.max_size)
        speed = random.randint(self.min_speed, self.max_speed)
        y = random.randint(0,self.screen_height - size)
        self.obstacles.append(Obstacle(self.screen_width,y, size,speed))

    def remove_unused(self):
        old_amount = len(self.obstacles)
        self.obstacles = list(filter(lambda obst: obst.x > -obst.size, self.obstacles))
        #self.obstacles = [obst for obst in self.obstacles if obst.x > -obst.size]
        return old_amount - len(self.obstacles)

    def manage_obstacles(self, elapsed_time):
        for obst in self.obstacles:
            obst.update(elapsed_time)

        score_diff = self.remove_unused()

        self.elapsed_time += elapsed_time
        if self.elapsed_time >= self.time_to_obstacle:
            self.add()
            self.elapsed_time = 0
        return score_diff
            