import pygame
import random
from paletka import Paddle
from ball import Ball
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
running = True
rect_height = 200


paddle = Paddle(screen, (255,255,255),  20, 300, 20,  200, SCREEN_HEIGHT)
paddle_two = Paddle(screen, (255,255,255),  1250, 300, 20,  200, SCREEN_HEIGHT)
ball = Ball(screen, (255,255,255), 660,350, 10, 10, SCREEN_HEIGHT, SCREEN_WIDTH)
while running:
    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle.move_up()
        if keys[pygame.K_s]:
            paddle.move_down()
        if keys[pygame.K_UP]:
            paddle_two.move_up()
        if keys[pygame.K_DOWN]:
            paddle_two.move_down()

    screen.fill((0,0,0))

    paddle.draw()
    paddle_two.draw()
    ball.draw()
    ball.move()
    if paddle.rect.colliderect(ball.rect) or paddle_two.rect.colliderect(ball.rect):
        ball.collision()
    paddle.check_screen()
    paddle_two.check_screen()
    pygame.display.flip()

    clock.tick(FPS)