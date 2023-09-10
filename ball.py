import pygame
class Ball():
    def __init__(self, screen, color, x, y, width, height, SCREEN_HEIGHT, SCREEN_WIDTH):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.y_speed = 3
        self.x_speed = 3
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x,self.y),self.width,self.height)

    def move(self):
        if self.y <= 0  or self.y + self.height >= self.SCREEN_HEIGHT:
            self.y_speed = -self.y_speed
            # self.x_speed = -self.x_speed

        self.x += self.x_speed
        self.y += self.y_speed

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    def collision(self):
        self.x_speed = -self.x_speed