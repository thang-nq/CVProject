import cv2
import numpy as np
import os
import pygame
import pymunk
import GameObjects
import HandTrackingModule as htm
import Constants
import GameUI

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
        self.collision = Constants.COLLISION_TYPES

        # Variables
        self.gameStart = 0
        self.X, self.Y = 0, 0
        self.cX, self.cY = 0, 0
        self.stroke = 0
        self.ended = 0
        self.inGameUI = GameUI.inGameUI(self.screen)

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

        # Level init
        # self.level1 = Level(level_map1, self.screen)
        # self.level2 = Level(level_map2, self.screen)


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
            self.event_hanlder()
            self.draw()
            self.update()

    def update(self):
        self.space.step(self.DT)
        pygame.display.update()
        self.clock.tick(self.FPS)

    def reset_game(self, arbiter, space, data):
        self.gameStart = False
        for shape in self.space.shapes:
            if shape.collision_type != self.collision['border']:
                self.space.remove(shape, shape.body)
        self.apples = []
        self.segs = []
        self.draw()
        return False

    def event_hanlder(self):
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

    def draw(self):
        self.screen.fill((247, 247, 247))
        if not self.gameStart:
            pygame.draw.circle(self.screen, (0, 0, 0), (200, 200), self.RAD)
            pygame.draw.circle(self.screen, (255, 0, 0), (400, 200), self.RAD)

        # draw_goal(goal)
        self.inGameUI.draw()
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


    def level1_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 640), (1280, 640), 0)
        self.space.add(box_body, shape1)

    def level2_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 600), (1280, 640), 0)
        self.space.add(box_body, shape1)

    def level3_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 240), (160, 240),0)
        shape2 = pymunk.Segment(box_body, (160,240),(400,480),0)
        shape3 = pymunk.Segment(box_body, (400,480),(400,560), 0)
        shape4 = pymunk.Segment(box_body, (400,560),(560,560), 0)
        shape5 = pymunk.Segment(box_body, (560,560),(560,480), 0)
        shape6 = pymunk.Segment(box_body, (560,480),(720,480), 0)
        shape7 = pymunk.Segment(box_body, (720, 480), (720, 560), 0)
        shape8 = pymunk.Segment(box_body, (720, 560), (880, 560), 0)
        shape9 = pymunk.Segment(box_body, (880, 560), (880, 480), 0)
        shape10 = pymunk.Segment(box_body, (880, 480), (1120, 240), 0)
        shape11 = pymunk.Segment(box_body, (1120, 240), (1280, 240), 0)
        pygame.draw.line(self.screen,(0,0,255),(160,240),(400,480),1)
        pygame.draw.line(self.screen, (0, 0, 255), (880, 480), (1120, 240), 1)
        self.space.add(box_body, shape1,shape2,shape3,shape4,shape5,shape6,shape7,shape8,shape9,shape10,shape11)

    def level4_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1=pymunk.Segment(box_body,(240,320),(320,320),0)
        shape2 = pymunk.Segment(box_body, (320,320), (320,480), 0)
        shape3 = pymunk.Segment(box_body, (320,480), (160,480), 0)
        shape4 = pymunk.Segment(box_body, (160,480), (160,400), 0)
        shape5 = pymunk.Segment(box_body, (160,400), (240,400), 0)
        shape6 = pymunk.Segment(box_body, (240,400), (240,320), 0)
        shape7 = pymunk.Segment(box_body, (1280,240), (1040,240), 0)
        shape8 = pymunk.Segment(box_body, (1040,240), (560,720), 0)

        pygame.draw.line(self.screen,(0, 0, 255),(240,320),(320,320),1)
        pygame.draw.line(self.screen,(0, 0, 255),(320,320),(320,480),1)
        pygame.draw.line(self.screen,(0, 0, 255),(320,480),(160,480),1)
        pygame.draw.line(self.screen,(0, 0, 255),(160,480),(160,400),1)
        pygame.draw.line(self.screen,(0, 0, 255),(160,400),(240,400),1)
        pygame.draw.line(self.screen,(0, 0, 255),(240,400),(240,320),1)
        pygame.draw.line(self.screen,(0, 0, 255),(1280,240),(1040,240),1)
        pygame.draw.line(self.screen,(0, 0, 255),(1040,240),(560,720),1)
        self.space.add(box_body,shape1,shape2,shape3,shape4,shape5,shape6,shape7,shape8)

    def level5_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (560,160), (960,160), 0)
        shape2 = pymunk.Segment(box_body, (960,160), (960, 240), 0)
        shape3 = pymunk.Segment(box_body, (960,240), (560, 240), 0)
        shape4 = pymunk.Segment(box_body, (560, 240), (560, 160), 0)
        shape5 = pymunk.Segment(box_body, (0, 480), (480,480), 0)
        shape6 = pymunk.Segment(box_body, (480, 480), (480, 640), 0)
        shape7 = pymunk.Segment(box_body, (480, 640), (960, 640), 0)
        shape8 = pymunk.Segment(box_body, (960, 640), (960, 560), 0)
        shape9 = pymunk.Segment(box_body, (960,560), (1280, 560), 0)

        pygame.draw.line(self.screen,(0, 0, 255),(560,160),(960,160),1)
        pygame.draw.line(self.screen, (0, 0, 255), (960,160), (960, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960,240), (560, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (560, 240), (560, 160), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (0, 480), (480,480), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (480, 480), (480, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (480, 640), (960, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 640), (960, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960,560), (1280, 560), 1)
        self.space.add(box_body,shape1,shape2,shape3,shape4,shape5,shape6,shape7,shape8,shape9)

    def level6_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (560,240),(640,240), 0)
        shape2 = pymunk.Segment(box_body, (640, 240), (640, 320), 0)
        shape3 = pymunk.Segment(box_body, (640, 320), (560, 320), 0)
        shape4 = pymunk.Segment(box_body, (560, 320), (560, 240), 0)
        shape5 = pymunk.Segment(box_body, (0, 640), (1280, 640), 0)

        pygame.draw.line(self.screen,(0, 0, 255),(560,240),(640,240),1)
        pygame.draw.line(self.screen, (0, 0, 255), (640, 240), (640, 320), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (640, 320), (560, 320), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (560, 320), (560, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (0, 640), (1280, 640), 1)
        self.space.add(box_body,shape1,shape2,shape3,shape4,shape5)

    def level7_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0,240),(160,240), 0)
        shape2 = pymunk.Segment(box_body, (160, 240), (480, 560), 0)
        shape3 = pymunk.Segment(box_body, (480, 560), (960, 560), 0)
        shape4 = pymunk.Segment(box_body, (960, 560), (960, 640), 0)
        shape5 = pymunk.Segment(box_body, (960,640), (1040, 640), 0)
        shape6 = pymunk.Segment(box_body, (1040, 640), (1040, 480), 0)
        shape7 = pymunk.Segment(box_body, (1040, 480), (1280, 480), 0)

        pygame.draw.line(self.screen,(0, 0, 255),(0,240),(160,240),1)
        pygame.draw.line(self.screen, (0, 0, 255), (160, 240), (480, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (480, 560), (960, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 560), (960, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960,640), (1040, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1040, 640), (1040, 480), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1040, 480), (1280, 480), 1)
        self.space.add(box_body,shape1,shape2,shape3,shape4,shape5,shape6,shape7)

    def level8_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0,80),(560,640), 0)
        shape2 = pymunk.Segment(box_body, (560,640), (720, 640), 0)
        shape3 = pymunk.Segment(box_body, (720,640), (1280, 80), 0)

        pygame.draw.line(self.screen,(0, 0, 255),(0,80),(560,640),1)
        pygame.draw.line(self.screen, (0, 0, 255), (560,640), (720, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (720,640), (1280, 80), 1)
        self.space.add(box_body,shape1,shape2,shape3)

    def level9_map(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0,160),(400,560), 0)
        shape2 = pymunk.Segment(box_body, (400, 560), (640, 560), 0)
        shape3 = pymunk.Segment(box_body, (640,560), (1040, 160), 0)
        shape4 = pymunk.Segment(box_body, (1040, 160), (1280, 160), 0)

        pygame.draw.line(self.screen,(0, 0, 255),(0,160),(400,560),1)
        pygame.draw.line(self.screen, (0, 0, 255), (400, 560), (640, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (640,560), (1040, 160), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1040, 160), (1280, 160), 1)
        self.space.add(box_body,shape1,shape2,shape3,shape4)

game = Bubble_tea()
game.main_loop()
