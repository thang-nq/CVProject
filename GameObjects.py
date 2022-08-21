import pygame
import pymunk


class Dot:
    """
    param
    """

    def __init__(self, space, radian, pos, collisionType, density=1, elastic=1, friction=0, color=(0, 0, 0)):
        self.body = pymunk.Body(pymunk.Body.DYNAMIC)
        self.rad = radian
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, self.rad)
        self.shape.density = density
        self.shape.elasticity = elastic
        self.shape.friction = friction
        self.shape.collision_type = collisionType
        self.color = color
        space.add(self.body, self.shape)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.body.position.x, self.body.position.y), self.rad)


class Seg:
    """

    """

    def __init__(self, space, weight, density, pos1, pos2, elastic=0.5, friction=0):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.weight = weight
        self.shape = pymunk.Segment(self.body, pos1, pos2, weight)
        self.shape.density = density
        self.shape.elasticity = elastic
        self.shape.friction = friction
        space.add(self.body, self.shape)
