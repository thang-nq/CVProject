import pygame, pymunk


class Dot:
    def __init__(self, space, radian, density, elastic=1, friction=0):
        self.body = pymunk.Body(pymunk.Body.STATIC)
        self.rad = radian
        self.shape = pymunk.Circle(self.body, self.rad)
        self.shape.density = density
        self.shape.elasticity = elastic
        self.shape.friction = friction
        space.add(self.body,self.shape)
