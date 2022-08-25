import numpy as np
import os
import pygame
import pymunk
import GameObjects

FPS = 60
VEL = 5
DT = 1 / FPS
WIDTH, HEIGHT = 900, 500
RAD = 20
LINE_WEIGHT = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
space = pymunk.Space()
space.gravity = (0, 981)





def draw_border(segments):
    for seg in segments:
        point1 = (seg.shape.a.x, seg.shape.a.y)
        point2 = (seg.shape.b.x + 10, seg.shape.b.y)

        pygame.draw.line(screen, (0, 0, 0), point1, point2, width=15)


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)

        pygame.draw.circle(screen, apple.color, (pos_x, pos_y), RAD)


def game():
    clock = pygame.time.Clock()
    run = True
    x_mouse, y_mouse =0,0
    game_state = 0

    gameStart = False
    border = []
    apples = []
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    apples.append(GameObjects.Dot(space, RAD, event.pos, 'ball'))
                    # print(event.pos)
                if (x_mouse < 60 and y_mouse < 155 and y_mouse > 90):
                    game_state = 1
                    print(game_state)
                if game_state == 1:
                    if x_mouse > 500 and y_mouse > 200 and y_mouse < 300:
                        # Resume in the paused screen
                        game_state = 0
                    if x_mouse > 500 and y_mouse > 300:
                        # Restart in the paused screen
                        restart()
                        level.load_level()
                        game_state = 0
                        bird_path = []
        x_mouse, y_mouse = pygame.mouse.get_pos()
        screen.fill((247, 247, 247))

        # apples.append(GameObjects.Dot(space, RAD, (450,450), 'ball'))
        # border.append(
        #     GameObjects.Seg(space, 10, 1, (0, 400), (400, 400), elastic=0, collisionType="border"))

        draw_apples(apples)
        # draw_border(border)
        if game_state != 1:
            space.step(DT)

        pygame.display.update()
        clock.tick(FPS)


game()
pygame.quit()
