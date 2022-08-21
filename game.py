import cv2
import numpy as np
import os
import pygame
import pymunk
import GameObjects

class Bubble_tea:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.WIDTH, self.HEIGHT = 900, 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("First Game!")
        self.space = pymunk.Space()
        self.space.gravity = (0, 981)


        # CONSTANTS
        self.FPS = 60
        self.VEL = 5
        self.DT = 1 / self.FPS
        self.RAD = 20
        self.LINE_WEIGHT = 10
        # Add a new collision type
        self.COLLTYPE_BALL = 2
        self.COLLTYPE_GOAL = 3

        # Variables
        self.gameStart = False
        self.X, self.Y = 0, 0
        self.apples = []
        self.dots = []
        self.segs = []

        # Setup the collision callback function
        self.h = self.space.add_collision_handler(self.COLLTYPE_BALL, self.COLLTYPE_GOAL)

    # Define collision callback function, will be called when X touches Y
    def goal_reached(self, arbiter, space, data):
        print("you reached the goal!")
        return True

    def main_loop(self):
        self.h.begin = self.goal_reached
        while True:
            self._event_hanlder()
            self._draw()
            self._update()

    def _update(self):
        self.space.step(self.DT)
        pygame.display.update()
        self.clock.tick(self.FPS)

    def _event_hanlder(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.X, self.Y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                self.apples.append(GameObjects.Dot(self.space, self.RAD, (200, 200), self.COLLTYPE_BALL))
                self.apples.append(self.create_goal())
                self.gameStart = True

        if pygame.mouse.get_pressed()[0]:
            mpos = pygame.mouse.get_pos()
            self.segs.append(self.create_segments(mpos))

    def _draw(self):
        self.screen.fill((247, 247, 247))
        if not self.gameStart:
            pygame.draw.circle(self.screen, (0, 0, 0), (200, 200), self.RAD)
            pygame.draw.circle(self.screen, (255, 0, 0), (400, 200), self.RAD)

        # draw_goal(goal)
        self.draw_apples(self.apples)
        self.draw_path(self.segs)

    def create_segments(self, pos):
        x1, y1 = pos

        # The drawing function will draw a line from 2 point
        if self.X == 0 and self.Y == 0:  # if the pen is not inside the canvas or first start the app
            self.X, self.Y = x1, y1  # pass the current coordinate of the pen
        else:  # draw a line from previous frame location of the pen to current frame position
            seg = GameObjects.Seg(self.space, 5, 1, (self.X, self.Y), (x1, y1))
            seg_shape = seg.shape
            self.X, self.Y = x1, y1  # after drawing, the current position become previous position
            return seg_shape

    def create_goal(self):
        seg = GameObjects.Dot(self.space, self.RAD, (400, 200), self.COLLTYPE_GOAL, color=(255, 0, 0))
        seg_shape = seg.shape
        return seg

    def draw_path(self, segments):
        for seg in segments:
            point1 = seg.a
            point2 = seg.b

            pygame.draw.line(self.screen, (0, 0, 0), point1, point2, 5)

    def draw_apples(self,apples):
        for apple in apples:
            pos_x = int(apple.body.position.x)
            pos_y = int(apple.body.position.y)

            pygame.draw.circle(self.screen, apple.color, (pos_x, pos_y), self.RAD)
