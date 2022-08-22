import ball
import pygame
import pymunk
import pymunk.util as u
from pymunk import Vec2d

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 900, 500
RAD = 20
LINE_WEIGHT = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
space = pymunk.Space()
space.gravity = (0, 981)
x, y = 0, 0
FPS = 30
VEL = 5
DT = 1 / FPS


def create_dot(sp, pos):
    body = pymunk.Body(100, body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, LINE_WEIGHT)
    shape.elasticity = 1
    shape.friction = 0.5
    sp.add(body, shape)
    return shape


def create_ball(sp, pos):
    body = pymunk.Body(1, 100)
    body.position = pos
    # body.mass = 1
    shape = pymunk.Circle(body, RAD)
    shape.elasticity = 0.1
    shape.friction = 0.5
    sp.add(body, shape)
    return shape


def draw_ball(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)

        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), RAD)


def draw_path(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)

        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), LINE_WEIGHT)


# GROUP to draw
balls = []
dots = []


# MAIN GAME
def game():
    clock = pygame.time.Clock()
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left mouse button - DRAW PATH
                    x0, y0 = pygame.mouse.get_pos()
                    dots.append(create_dot(space, (x0, y0)))

                elif event.button == 3: # RMB - CREATE BALL
                    balls.append(create_ball(space, event.pos))
        # TAKE mouse position if pressed down
        if pygame.mouse.get_pressed()[0]:
            mpos = pygame.mouse.get_pos()
            dots.append(create_dot(space, mpos))

        screen.fill((247, 247, 247))

        draw_ball(balls)
        draw_path(dots)

        space.step(DT)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)


game()
pygame.quit()
