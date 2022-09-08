import cv2
import numpy as np
import os
import pygame
import pymunk
import GameObjects
import HandTrackingModule as htm
from settings import *
from level import Level

class Bubble_tea:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.WIDTH, self.HEIGHT = 1500, 800
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
        self.gameStart = 0
        self.X, self.Y = 0, 0
        self.cX, self.cY = 0, 0
        self.apples = []
        self.dots = []
        self.segs = []

        # Setup the collision callback function
        self.h = self.space.add_collision_handler(self.COLLTYPE_BALL, self.COLLTYPE_GOAL)

        #Tracking module config
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1280)
        self.capture.set(4, 720)
        self.detector = htm.handDetector(detectCon=0.85)

        self.level1 = Level(level_map1, self.screen)
        self.level2 = Level(level_map2, self.screen)
        self.level3 = Level(level_map3, self.screen)
        self.level4 = Level(level_map4, self.screen)
        self.level5 = Level(level_map5, self.screen)
        self.level6 = Level(level_map6, self.screen)
        self.level7 = Level(level_map7, self.screen)
        self.level8 = Level(level_map8, self.screen)
        self.level9 = Level(level_map9, self.screen)

        # self.level2 = Level(level_map2, self.screen)
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
                return
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
        self.level9.load_map()
        self.level9_map()
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

    def draw_apples(self,apples):
        for apple in apples:
            pos_x = int(apple.body.position.x)
            pos_y = int(apple.body.position.y)

            pygame.draw.circle(self.screen, apple.color, (pos_x, pos_y), self.RAD)

    def level1_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 700), (1500, 700), 0)
        self.space.add(box_body, shape1)

    def level2_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 700), (1500, 700), 0)
        self.space.add(box_body, shape1)

    def level3_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 300), (200, 300),0)
        shape2 = pymunk.Segment(box_body, (200,300),(600,700),0)
        shape3 = pymunk.Segment(box_body, (600,700),(700,700), 0)
        shape4 = pymunk.Segment(box_body, (700,700),(700,600), 0)
        shape5 = pymunk.Segment(box_body, (700,600),(800,600), 0)
        shape6 = pymunk.Segment(box_body, (800,600),(800,700), 0)
        shape7 = pymunk.Segment(box_body, (800, 700), (900, 700), 0)
        shape8 = pymunk.Segment(box_body, (900, 700), (1300, 300), 0)
        shape9 = pymunk.Segment(box_body, (1300, 300), (1500, 300), 0)

        pygame.draw.polygon(self.screen,(60,61,71),((200,300),(200,700),(600,700)))
        pygame.draw.polygon(self.screen,(60,61,71),((1300,300),(1300,700),(900,700)))
        self.space.add(box_body, shape1,shape2,shape3,shape4,shape5,shape6,shape7,shape8,shape9)

    def level4_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1=pymunk.Segment(box_body,(350,300),(400,300),0)
        shape2 = pymunk.Segment(box_body, (400,300),(400,450), 0)
        shape3 = pymunk.Segment(box_body, (400,450),(250,450), 0)
        shape4 = pymunk.Segment(box_body, (250,450),(250,400), 0)
        shape5 = pymunk.Segment(box_body, (250,400),(350,400), 0)
        shape6 = pymunk.Segment(box_body, (350,400),(350,300), 0)
        shape7 = pymunk.Segment(box_body, (1500,300), (1300,300), 0)
        shape8 = pymunk.Segment(box_body, (1300,300), (700,800), 0)

        pygame.draw.polygon(self.screen,(60,61,71),((1300,300),(1300,800),(700,800)))
        self.space.add(box_body,shape1,shape2,shape3,shape4,shape5,shape6,shape7,shape8)

    def level5_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (650,300),(1050,300), 0)
        shape2 = pymunk.Segment(box_body, (1050,300), (1050, 350), 0)
        shape3 = pymunk.Segment(box_body, (1050,350), (650, 350), 0)
        shape4 = pymunk.Segment(box_body, (650, 350), (650,300 ), 0)
        shape5 = pymunk.Segment(box_body, (0, 500), (550,500), 0)
        shape6 = pymunk.Segment(box_body, (550, 500), (550, 700), 0)
        shape7 = pymunk.Segment(box_body, (550, 700), (1050, 700), 0)
        shape8 = pymunk.Segment(box_body, (1050, 700), (1050, 650), 0)
        shape9 = pymunk.Segment(box_body,(1050,650), (1500, 650), 0)

        self.space.add(box_body,shape1,shape2,shape3,shape4,shape5,shape6,shape7,shape8,shape9)

    def level6_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (560,240),(640,240), 0)
        shape2 = pymunk.Segment(box_body, (640, 240), (640, 320), 0)
        shape3 = pymunk.Segment(box_body, (640, 320), (560, 320), 0)
        shape4 = pymunk.Segment(box_body, (560, 320), (560, 240), 0)
        shape5 = pymunk.Segment(box_body, (0, 640), (1280, 640), 0)

        self.space.add(box_body,shape1,shape2,shape3,shape4,shape5)

    def level7_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0,300),(200,300), 0)
        shape2 = pymunk.Segment(box_body, (200, 300), (600, 650), 0)
        shape3 = pymunk.Segment(box_body, (600,650),(1050,650), 0)
        shape4 = pymunk.Segment(box_body, (1050, 650), (1050, 700), 0)
        shape5 = pymunk.Segment(box_body, (1050, 700), (1150, 700), 0)
        shape6 = pymunk.Segment(box_body, (1150,700), (1150, 600), 0)
        shape7 = pymunk.Segment(box_body, (1150, 600), (1500, 600), 0)

        pygame.draw.polygon(self.screen,(60,61,71),((200,300),(200,650),(600,650)))
        self.space.add(box_body,shape1,shape2,shape3,shape4,shape5,shape6,shape7)

    def level8_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0,150),(700,700), 0)
        shape2 = pymunk.Segment(box_body, (700,700), (800, 700), 0)
        shape3 = pymunk.Segment(box_body, (800,700), (1500, 150), 0)

        pygame.draw.polygon(self.screen,(60,61,71),((0,150),(0,700),(700,700)))
        pygame.draw.polygon(self.screen,(60,61,71),((1500,150),(1500,700),(800,700)))
        self.space.add(box_body,shape1,shape2,shape3)

    def level9_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0,300),(500,700), 0)
        shape2 = pymunk.Segment(box_body, (500, 700), (600, 700), 0)
        shape3 = pymunk.Segment(box_body, (600,700), (1200, 150), 0)
        shape4 = pymunk.Segment(box_body, (1200, 150), (1500, 150), 0)

        pygame.draw.polygon(self.screen,(60,61,71),((0,300),(0,700),(500,700)))
        pygame.draw.polygon(self.screen, (60,61,71), ((1200,150),(1200,700),(600,700)))
        self.space.add(box_body,shape1,shape2,shape3,shape4)

game = Bubble_tea()
game.main_loop()