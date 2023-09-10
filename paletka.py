import pygame
class Paddle:
    def __init__(self, screen, color, x, y, width, height, SCREEN_HEIGHT):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x,self.y,self.width,self.height))
    def move_down(self):
        self.y += 10
    def move_up(self):
        self.y -= 10
    def check_screen(self):
        if self.y <= 0:
            self.y = 0

        if self.y + self.height >= self.SCREEN_HEIGHT:
            self.y = self.SCREEN_HEIGHT - self.height
    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)