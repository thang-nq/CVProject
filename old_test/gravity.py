import os

import numpy
import pygame
import pymunk
import sys
from pymunk.pygame_util import to_pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 900, 500
RAD = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
screen2 = pygame.display.set_mode((WIDTH+100, HEIGHT))
pygame.display.set_caption("Second Game!")
space = pymunk.Space()
space.gravity = (0, 981)


def create_apple(space, pos):
    body = pymunk.Body(1, 100)
    body.position = pos
    shape = pymunk.Circle(body, RAD)
    space.add(body, shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), RAD)

def to_pygame(p):
    """Small helper to convert pymunk vec2d to pygame integers"""
    return round(p.x), round(p.y)

def add_static_L(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-150, 0), (255, 0), 5)  # 2
    l2 = pymunk.Segment(body, (-150, 0), (-150, -50), 5)
    l1.friction = 1  # 3
    l2.friction = 1

    space.add(body, l1, l2)  # 4
    return l1, l2

def add_L(space):
    """Add a inverted L shape with two joints"""
    rotation_center_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    rotation_center_body.position = (300,300)

    rotation_limit_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    rotation_limit_body.position = (200,300)

    body = pymunk.Body(10, 10000)
    body.position = (300,300)

    l1 = pymunk.Segment(body, (-150, 0), (255.0, 0.0), 2.0)
    l2 = pymunk.Segment(body, (-150.0, 0), (-150.0, -50.0), 2.0)

    l1.friction = 1
    l2.friction = 1

    l1.mass = 8
    l2.mass = 1

    rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (100,0), (0,0))
    joint_limit = 25
    rotation_limit_joint = pymunk.SlideJoint(body, rotation_limit_body, (-100,0), (0,0), 0, joint_limit)

    space.add(l1, l2, body, rotation_center_joint, rotation_limit_joint)
    return l1,l2


def draw_lines(screen, lines):
    for line in lines:
        body = line.body
        pv1 = body.position + line.a.rotated(body.angle)  # 1
        pv2 = body.position + line.b.rotated(body.angle)
        p1 = to_pygame(pv1)  # 2
        p2 = to_pygame(pv2)
        pygame.draw.lines(screen, (255, 0, 0), False, [p1, p2])


apples = []

FPS = 60
VEL = 5
DT = 1 / FPS


def main():
    clock = pygame.time.Clock()
    run = True
    lines = add_static_L(space)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                apples.append(create_apple(space, event.pos))
        screen.fill((247, 247, 247))
        draw_apples(apples)
        draw_lines(screen,lines)
        screen2.fill((247, 247, 247))
        #space.debug_draw(draw_options)
        space.step(DT)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
