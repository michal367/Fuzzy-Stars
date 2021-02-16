import pygame
from button import *
from utils import *


class Menu:
    def __init__(self, win):
        self.win = win
        self.font_big = pygame.font.SysFont('Impact', 80)
        self.font_normal = pygame.font.SysFont('Impact', 24)
        self.FPS = 30
        self.clock = pygame.time.Clock()

        self.running = True

        self.title_textsurface = self.font_big.render('FUZZY STARS', True, (200, 0, 0))

        button_color = (69,73,77)
        button_hover_color = (150,160,169)
        self.buttons = [
            ActiveButton(win, "Player", self.font_normal, 260,230, 120,50, button_color, button_hover_color, self.player_button_handler),
            ActiveButton(win, "Computer", self.font_normal, 420,230, 120,50, button_color, button_hover_color, self.computer_button_handler),
            ActiveButton(win, "Normal", self.font_normal, 260,320, 120,50, button_color, button_hover_color, self.normal_button_handler),
            ActiveButton(win, "Hard", self.font_normal, 420,320, 120,50, button_color, button_hover_color, self.hard_button_handler),
            Button(win, "Start", self.font_normal, 340,410, 120,50, button_color, button_hover_color, self.start),
            Button(win, "Quit", self.font_normal, 340,480, 120,50, button_color, button_hover_color, self.quit_game),
        ]

        self.player = PLAYER_PLAYER
        self.difficulty = DIFFICULTY_NORMAL
        self.buttons[0].set_active()
        self.buttons[2].set_active()


    def player_button_handler(self):
        self.buttons[1].set_inactive()
        self.player = PLAYER_PLAYER
    def computer_button_handler(self):
        self.buttons[0].set_inactive()
        self.player = PLAYER_COMPUTER
    def normal_button_handler(self):
        self.buttons[3].set_inactive()
        self.difficulty = DIFFICULTY_NORMAL
    def hard_button_handler(self):
        self.buttons[2].set_inactive()
        self.difficulty = DIFFICULTY_HARD
    
    def start(self):
        self.running = False
    def quit_game(self):
        pygame.quit()
        quit()

    def draw_title(self):
        x = (800 - self.title_textsurface.get_width())/2
        y = 70
        self.win.blit(self.title_textsurface,(x,y))

    def draw(self):
        self.win.fill((0,0,0))
        self.draw_title()
        for button in self.buttons:
            button.draw()
        pygame.display.update()

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(self.FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.draw()
            
        return (self.player, self.difficulty)