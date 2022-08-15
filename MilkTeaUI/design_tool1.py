
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
    """

    :param sp:
    :param pos:
    :return:
    """
    body = pymunk.Body(100, body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, LINE_WEIGHT)
    shape.elasticity = 1
    shape.friction = 0.5
    sp.add(body, shape)
    return shape


def create_segments(pos):
    global x, y
    x1, y1 = pos

    # The drawing function will draw a line from 2 point
    if x == 0 and y == 0:  # if the pen is not inside the canvas or first start the app
        x, y = x1, y1  # pass the current coordinate of the pen
    else:  # draw a line from previous frame location of the pen to current frame position
        seg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        seg_shape = pymunk.Segment(seg_body, (x, y), (x1, y1), LINE_WEIGHT)
        seg_shape.elasticity = 0.5
        space.add(seg_body, seg_shape)

        x, y = x1, y1  # after drawing, the current position become previous position
        return seg_shape


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


def draw_path(dots):
    for dot in dots:
        pos_x = int(dot.body.position.x)
        pos_y = int(dot.body.position.y)

        pygame.draw.circle(screen, (255, 0, 0), (pos_x, pos_y), LINE_WEIGHT)


def draw_path2(segments):
    for seg in segments:
        point1 = seg.a
        point2 = seg.b

        pygame.draw.line(screen, (0, 0, 0), point1, point2, LINE_WEIGHT)


# GROUP to draw
segs = []
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
                if event.button == 1:  # Left mouse button - DRAW PATH
                    global x, y
                    x, y = pygame.mouse.get_pos()
                elif event.button == 3:  # RMB - CREATE BALL
                    x0, y0 = pygame.mouse.get_pos()
                    print(pygame.mouse.get_pos())
                    dots.append(create_dot(space, (x0, y0)))

        # TAKE mouse position if pressed down
        if pygame.mouse.get_pressed()[0]:
            mpos = pygame.mouse.get_pos()
            segs.append(create_segments(mpos))

        screen.fill((247, 247, 247))
        # draw_ball(balls)
        draw_path(dots)
        draw_path2(segs)

        space.step(DT)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)


pygame.quit()
