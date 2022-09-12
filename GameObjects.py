import pygame
import pymunk
import Constants
import math
collision = Constants.COLLISION_TYPES


class Dot:
    """
    param
    """

    def __init__(self, space, radian, pos, img_path,size, collisionType = 'ball', density=1, elastic=1, friction=0, color=(0, 0, 0)):
        # Image
        self.image = img_path
        self.image = pygame.transform.scale(self.image, size)
        self.orig_image = self.image

        self.rect = self.image.get_rect(center=pos)
        # self.rect.topleft = pos

        # Pymunk
        self.body = pymunk.Body(pymunk.Body.DYNAMIC)
        self.rad = radian
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, self.rad)
        self.shape.density = density
        self.shape.elasticity = elastic
        self.shape.friction = friction
        self.shape.collision_type = collision[collisionType]
        self.color = color
        space.add(self.body, self.shape)

    def draw(self, screen):
        # self.rect.center = self.body.position
        # self.image = pygame.transform.rotate(
        #     self.orig_image, math.degrees(self.body.angle))
        # self.rect = self.image.get_rect(center=self.rect.center)
        pygame.draw.circle(screen,self.color, (self.body.position.x, self.body.position.y), self.rad)
        # screen.blit(self.image, (self.rect.x,self.rect.y))

    def getShape(self):
        return self.shape

class Seg:
    """

    """

    def __init__(self, space, radius, density, pos1, pos2, elastic=0.5, friction=0, collisionType = 'line'):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.radius = radius
        self.shape = pymunk.Segment(self.body, pos1, pos2, radius= self.radius)
        self.shape.collision_type = collision[collisionType]
        self.shape.density = density
        self.shape.elasticity = elastic
        self.shape.friction = friction
        space.add(self.body, self.shape)

    def getShape(self):
        return self.shape

class Seg2:
    """

    """

    def __init__(self, space, radius, density, pos1, pos2, elastic=0.5, friction=0, collisionType = 'line'):
        self.body = pymunk.Body(2,body_type=pymunk.Body.DYNAMIC)
        self.radius = radius
        self.shape = pymunk.Segment(self.body, pos1, pos2, radius=self.radius)
        self.shape.collision_type = collision[collisionType]
        self.shape.density = density
        self.shape.elasticity = elastic
        self.shape.friction = friction
        space.add(self.body, self.shape)

    def getShape(self):
        return self.shape

class Wall:
    def __init__(self,space):
        self.borderTop = Seg(space, 1, 1, (0, 0), (0, Constants.HEIGHT), elastic=0, collisionType="border")
        self.borderBottom=Seg(space, 1, 1, (0, Constants.HEIGHT), (Constants.WIDTH, Constants.HEIGHT), elastic=0, collisionType="border")
        self.borderRight=Seg(space, 1, 1, (Constants.WIDTH, Constants.HEIGHT), (Constants.WIDTH, 0), elastic=0,collisionType="border")
        self.borderLeft = Seg(space, 1, 1, (Constants.WIDTH, 0), (0, 0), elastic=0, collisionType="border")
        self.allBorder = [self.borderTop ,self.borderBottom,self.borderRight,self.borderLeft]

    def draw(self,screen):
        for seg in self.allBorder:
            point1 = seg.shape.a
            point2 = seg.shape.b

            pygame.draw.line(screen, (0, 0, 0), point1, point2, 5)