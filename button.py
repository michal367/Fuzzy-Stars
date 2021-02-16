import pygame


class Button:
    def __init__(self, win, text, font, x,y, width,height, color,hover_color, action_f=None):
        self.win = win
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.action_f = action_f

        self.textsurface = self.font.render(self.text, True, (255, 255, 255))

    def draw_text(self):
        x = self.x + self.width/2 - self.textsurface.get_width()/2
        y = self.y + self.height/2 - self.textsurface.get_height()/2
        self.win.blit(self.textsurface, (x,y))

    def draw(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if self.x < mouse[0] < self.x+self.width and self.y < mouse[1] < self.y+self.height:
            pygame.draw.rect(self.win, self.hover_color, (self.x,self.y, self.width,self.height))
            if click[0] == 1 and self.action_f != None:
                self.action_f()
        else:
            pygame.draw.rect(self.win, self.color, (self.x,self.y, self.width,self.height))
        
        self.draw_text()


class ActiveButton(Button):
    def __init__(self, win, text, font, x,y, width,height, color,hover_color, action_f=None):
        super().__init__(win, text, font, x,y, width,height, color,hover_color, action_f)
        self.active = False
    
    def set_active(self):
        self.active = True
    def set_inactive(self):
        self.active = False

    def draw(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if self.active or self.x < mouse[0] < self.x+self.width and self.y < mouse[1] < self.y+self.height:
            pygame.draw.rect(self.win, self.hover_color, (self.x,self.y, self.width,self.height))
            if click[0] == 1:
                if self.action_f != None:
                    self.action_f()
                self.set_active()
            
        else:
            pygame.draw.rect(self.win, self.color, (self.x,self.y, self.width,self.height))
        
        self.draw_text()