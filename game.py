import cv2
import numpy as np
import os
import pygame
import pymunk
import GameObjects
import HandTrackingModule as htm
import Constants


class Bubble_tea:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.WIDTH, self.HEIGHT = Constants.WIDTH, Constants.HEIGHT
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("First Game!")
        self.space = pymunk.Space()
        self.space.gravity = (0, 981)

        # CONSTANTS
        self.FPS = Constants.FPS
        self.VEL = 5
        self.DT = 1 / self.FPS
        self.RAD = 20
        self.LINE_WEIGHT = 10

        # Add a new collision type
        self.COLLTYPE_BALL = 2
        self.COLLTYPE_GOAL = 3

        # Variables
        self.gameStart = 0
        self.X, self.Y = 0, 0
        self.cX, self.cY = 0, 0
        self.stroke = 0
        self.ended = 0


        self.apples = []
        self.dots = []
        self.segs = []

        # ------------------------------------------ CREATE BORDER ------------------------------------------
        self.border = []
        self.border.append(
            GameObjects.Seg(self.space, 1, 1, (0, 0), (0, self.HEIGHT), elastic=0, collisionType="border"))
        self.border.append(GameObjects.Seg(self.space, 1, 1, (0, self.HEIGHT), (self.WIDTH, self.HEIGHT), elastic=0,
                                           collisionType="border"))
        self.border.append(GameObjects.Seg(self.space, 1, 1, (self.WIDTH, self.HEIGHT), (self.WIDTH, 0), elastic=0,
                                           collisionType="border"))
        self.border.append(
            GameObjects.Seg(self.space, 1, 1, (self.WIDTH, 0), (0, 0), elastic=0, collisionType="border"))

        # ------------------------------------------ END BORDER ------------------------------------------
        # Set up the collision callback function
        self.h = self.space.add_collision_handler(self.collision['ball'], self.collision['goal'])
        self.h.begin = self.goal_reached
        self.h.separate = self.finished

        self.b1 = self.space.add_collision_handler(self.collision['ball'], self.collision['border'])
        self.b2 = self.space.add_collision_handler(self.collision['goal'], self.collision['border'])
        self.b1.begin = self.through
        self.b2.begin = self.through
        self.b1.separate = self.reset_game
        self.b2.separate = self.reset_game


        # Tracking module config
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1280)
        self.capture.set(4, 720)
        self.detector = htm.handDetector(detectCon=0.85)

    # ==================================================================================================================
    # Define collision callback function, will be called when X touches Y
    def through(self, arbiter, space, data):
        return False

    def goal_reached(self, arbiter, space, data):
        if self.ended == 0:
            print("you reached the goal!")
            self.ended += 1
        return True

    def finished(self, arbiter, space, data):
        ball_shape1 = arbiter.shapes[0]
        space.remove(ball_shape1, ball_shape1.body)
        ball_shape2 = arbiter.shapes[1]
        space.remove(ball_shape2, ball_shape2.body)
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
        success, img = self.capture.read()
        img = cv2.flip(img, 1)
        img.flags.writeable = False
        img = self.detector.findHands(img, draw=True)
        lmList = self.detector.findPosition(img)
        handState = 'None'
        if len(lmList) != 0:
            (self.cX, self.cY) = lmList[8][1:]
            handState = self.detector.getHandState()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if handState == "Drawing":
            self.segs.append(self.create_segments((self.X, self.Y), (self.cX, self.cY)))
            self.X, self.Y = self.cX, self.cY
            print(self.X, self.Y)
        if handState == "Selecting" and self.gameStart < 1:
            self.apples.append(GameObjects.Dot(self.space, self.RAD, (200, 200), self.COLLTYPE_BALL))
            self.apples.append(self.create_goal())
            self.gameStart += 1

        # print(handState)

        # if pygame.mouse.get_pressed()[0]:
        #     mpos = pygame.mouse.get_pos()
        #     self.segs.append(self.create_segments(mpos))

    def _draw(self):
        self.screen.fill((247, 247, 247))
        if not self.gameStart:
            pygame.draw.circle(self.screen, (0, 0, 0), (200, 200), self.RAD)
            pygame.draw.circle(self.screen, (255, 0, 0), (400, 200), self.RAD)

        # draw_goal(goal)
        self.draw_apples(self.apples)
        self.draw_path(self.segs)

    def create_segments(self, previouspos, currentpos):
        if previouspos == (0, 0):  # if the pen is not inside the canvas or first start the app
            previouspos = currentpos  # pass the current coordinate of the pen
        # draw a line from previous frame location of the pen to current frame position
        seg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        seg_shape = pymunk.Segment(seg_body, previouspos, currentpos, self.LINE_WEIGHT)
        seg_shape.elasticity = 0.5
        self.space.add(seg_body, seg_shape)
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

    def draw_apples(self, apples):
        for apple in apples:
            pos_x = int(apple.body.position.x)
            pos_y = int(apple.body.position.y)

            pygame.draw.circle(self.screen, apple.color, (pos_x, pos_y), self.RAD)


game = Bubble_tea()
game.main_loop()
