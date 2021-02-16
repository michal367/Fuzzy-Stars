import pygame
from menu import *
from player import *
from obstacle import *
from utils import *
from images import *
from obstacles_manager import *
from logic import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.width = 800
        self.height = 600
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fuzzy Stars")
        pygame.mouse.set_cursor(*pygame.cursors.tri_left)
        Images.convert_alpha()

        self.running = False
        self.FPS = 30
        self.clock = pygame.time.Clock()

        self.font_big = pygame.font.SysFont('Impact', 60)
        self.font_normal = pygame.font.SysFont('Impact', 30)


    def init_game(self, difficulty):
        self.player = Player()
        self.player.x = 100
        self.player.y = self.height//2 - self.player.height//2
        self.obstacles = ObstaclesManager(self.width, self.height, difficulty)

        self.playing = True
        self.score = 0

    def check_collision(self):
        for obst in self.obstacles.obstacles:
            if dist_square2(obst, self.player) < (self.player.size/2 + 8)**2:
                self.player.destroy()
                self.playing = False
                # show_logic_sim()

    def game_over(self):
        textsurface = self.font_big.render('GAME OVER', True, (200, 0, 0))
        x = (self.width - textsurface.get_width())/2
        y = (self.height - textsurface.get_height())/2
        self.win.blit(textsurface,(x,y))


    def update(self, elapsed_time):
        self.player.check_position(self.height)
        score_diff = self.obstacles.manage_obstacles(elapsed_time)
        self.score += score_diff

        self.check_collision()


    def controls(self, elapsed_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.player.move_up(self.player.speed, elapsed_time)
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.player.move_down(self.player.speed, elapsed_time)

        # elif keys[pygame.K_l]:
        #     show_logic_sim()

    def draw_score(self):
        textsurface = self.font_normal.render('score: ' + str(self.score), True, (200, 0, 0))
        self.win.blit(textsurface,(5,self.height - textsurface.get_height() - 5))

    def draw(self):
        self.win.fill((0,0,0))

        for obst in self.obstacles.obstacles:
            obst.draw(self.win)
        self.player.draw(self.win)

        self.draw_score()

        if not self.playing:
            self.game_over()
        pygame.display.update()

    def logic_update(self, elapsed_time):
        if len(self.obstacles.obstacles) > 0:
            dists = [(obst, dist_square2(obst, self.player)) for obst in self.obstacles.obstacles if obst.x > self.player.x - self.player.size/3]
            first_obst = min(dists, key=lambda k: k[1])[0]

            first_time = (first_obst.x - self.player.x) / first_obst.speed
            dist = (self.player.y+self.player.height/2) - (first_obst.y+first_obst.size/2)
            player_y = self.player.y+self.player.size/2
            dy = logic_calc(first_time, dist, player_y)

            if dy > self.player.speed:
                dy = self.player.speed
            self.player.move_down(dy, elapsed_time)

            #print("input:", first_time, dist, player_y, "   output:", dy)

    def game_loop(self, player, difficulty):
        self.running = True
        self.init_game(difficulty)

        while self.running:
            elapsed_time = 1
            while elapsed_time > 0.5: # hack to bypass long elapsed time when game stops while dragging window
                elapsed_time = self.clock.tick(self.FPS)*0.001 # seconds

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if ((not self.playing
                        and event.key != pygame.K_w and event.key != pygame.K_UP
                        and event.key != pygame.K_s and event.key != pygame.K_DOWN)
                        or event.key == pygame.K_ESCAPE):
                        self.running = False

            if self.playing:
                if player == PLAYER_COMPUTER:
                    self.logic_update(elapsed_time)
                elif player == PLAYER_PLAYER:
                    self.controls(elapsed_time)
                self.update(elapsed_time)

            self.draw()


    def run(self):
        menu = Menu(self.win)
        while True:
            player, difficulty = menu.run()
            self.game_loop(player, difficulty)
