from ast import Constant
import cv2
import numpy as np
import os
import pygame
import pymunk
import GameObjects
import Constants
import GameUI
from level import Level


class Bubble_tea:
    def __init__(self, screen):
        # pygame.init()
        # pygame.font.init()
        self.WIDTH, self.HEIGHT = Constants.WIDTH, Constants.HEIGHT
        self.screen = screen

        # self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # self.clock = pygame.time.Clock()

        self.space = pymunk.Space()
        # self.space = space
        self.space.gravity = (0, Constants.GRAVITY)
        self.background = pygame.image.load('assets/MilkTeaImages/Background.png').convert_alpha()
        self.player_img = pygame.image.load('assets/MilkTeaImages/Bubble_Small.png').convert_alpha()
        self.goal_img = pygame.image.load('assets/MilkTeaImages/TeaBall.png').convert_alpha()
        self.die_img = pygame.image.load('assets/MilkTeaImages/MilkBall.png').convert_alpha()

        # CONSTANTS
        self.FPS = Constants.FPS
        self.VEL = 5
        self.DT = 1 / self.FPS
        self.RAD = 20
        self.LINE_WEIGHT = 10
        # Add a new collision type
        self.collision = Constants.COLLISION_TYPES

        # ------- CREATE BORDER ------------------------------------------
        self.border = GameObjects.Wall(self.space)
        # Variables
        self.gameStart = 0
        self.ended = 0
        self.number = 1

        # Arrays
        self.balls = []
        self.blocks = []
        self.segs = []
        self.death = []
        self.platforms = []
        # self.platforms2 = []
        self.platformtemp = []
        self.slopes = []

        self.tileSprites = pygame.sprite.Group()
        self.tempSprites = pygame.sprite.Group()
        self.tempBallPos = []

        self.level = Level(self.space, screen, self.number, self.tileSprites, self.platforms,self.platformtemp, self.slopes,
                           self.tempSprites, self.tempBallPos)

        # Varibles
        self.X, self.Y = 0, 0
        self.x_mouse, self.y_mouse = 0, 0
        self.inGameUI = GameUI.inGameUI(self.screen)

        # Setup the collision callback function
        self.h = self.space.add_collision_handler(self.collision['ball'], self.collision['goal'])
        self.h.begin = self.goal_reached
        self.h.separate = self.finished
        self.b1 = self.space.add_collision_handler(self.collision['ball'], self.collision['border'])
        self.b2 = self.space.add_collision_handler(self.collision['goal'], self.collision['border'])
        self.b1.begin = self.through
        self.b2.begin = self.through
        self.b1.separate = self.collide_reset_game
        self.b2.separate = self.collide_reset_game
        self.d = self.space.add_collision_handler(self.collision['ball'], self.collision['die'])
        self.d.begin = self.die_reached

    # -------COLLISION HANDLER ------------------------------------------
    # -------START ------------------------------------------
    # Define collision callback function, will be called when X touches Y
    def through(self, arbiter, space, data):
        return False

    def goal_reached(self, arbiter, space, data):
        if self.ended == 0:
            # print("you reached the goal!")
            self.ended += 1
        return True

    def die_reached(self, arbiter, space, data):
        if self.ended == 0:
            # print("you die!")
            self.ended -= 1
        return True

    # Define collision callback function, will be called when X touches Y
    def finished(self, arbiter, space, data):
        for ball in self.balls:
            self.space.remove(ball.shape, ball.shape.body)
        # ball_shape1 = arbiter.shapes[0]
        # space.remove(ball_shape1, ball_shape1.body)
        # ball_shape2 = arbiter.shapes[1]
        # space.remove(ball_shape2, ball_shape2.body)
        return True

    def collide_reset_game(self, arbiter, space, data):
        # FIX HERE =============================================
        self.gameStart = 0
        self.remove_segs()
        for ball in self.balls:
            self.space.remove(ball.shape, ball.shape.body)
        self.balls.clear()
        self.segs.clear()
        self.draw()

    # -------END ------------------------------------------

    # ------- MAIN LOOP ------------------------------------------
    def main_loop(self):
        # while True:
        self.event_hanlder()
        self.draw()
        self.update()

    # ------- CORE FUNCTIONS ------------------------------------------
    # --------------------------------------------------------

    def update(self):
        # if self.game_state != 1:
        self.space.step(self.DT)
        # pygame.display.update()
        # self.clock.tick(self.FPS)

    def event_hanlder(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.X, self.Y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                mpos = pygame.mouse.get_pos()
                self.segs.append(self.create_segments(mpos))

            if event.type == pygame.MOUSEBUTTONUP :
                if self.gameStart < 1:
                    self.balls.append(GameObjects.Dot(self.space, self.RAD, self.tempBallPos[0], self.player_img,
                                                      (self.RAD * 2.4, self.RAD * 2.4), 'ball',color=(103,192,169)))
                    self.balls.append(GameObjects.Dot(self.space, Constants.GOAL_RAD, self.tempBallPos[1], self.goal_img,
                                                      (Constants.GOAL_RAD * 2.2, Constants.GOAL_RAD * 2.2), 'goal',color=(241,186,80)))
                    if len(self.tempBallPos) > 2:
                        for i in range(2, len(self.tempBallPos)):
                            self.balls.append(GameObjects.Dot(self.space, self.RAD, self.tempBallPos[i], self.die_img,
                                                              (self.RAD * 2.4, self.RAD * 2.4), 'die', color=(0,0,0)))
                    # self.platforms2.append(GameObjects.Seg2(self.space, 5, 1, pos1=self.platformtemp[0][0],pos2=self.platformtemp[0][1], elastic=0).getShape())
                    # self.platforms2.append(
                    #     GameObjects.Seg2(self.space, 5, 1, pos1=self.platformtemp[1][0], pos2=self.platformtemp[1][1],
                    #                       elastic=0).getShape())
                    self.gameStart += 1
                else:
                    self.gameStart += 1

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        if self.gameStart == 0:
            pygame.draw.circle(self.screen, (103,192,169), self.tempBallPos[0], self.RAD)
            pygame.draw.circle(self.screen, (241,186,80), self.tempBallPos[1], Constants.GOAL_RAD)

            if len(self.tempBallPos) > 2:
                for i in range(2, len(self.tempBallPos)):
                    pygame.draw.circle(self.screen, (0, 0, 0), self.tempBallPos[i], self.RAD)
            # self.tempSprites.draw(self.screen)

        self.draw_apples(self.balls)
        self.draw_path(self.segs)
        self.draw_slopes(self.slopes)
        # self.draw_path(self.platforms2)

        self.border.draw(self.screen)
        self.tileSprites.draw(self.screen)

    def restart(self):
        self.gameStart = 0
        self.remove_segs()
        if self.ended <= 0:
            for ball in self.balls:
                self.space.remove(ball.shape, ball.shape.body)
        self.balls = []
        # self.platforms2 = []
        self.segs = []
        self.draw()

    def clear(self):
        self.gameStart = 0
        for shape in self.platforms:
            self.space.remove(shape, shape.body)
        # if len(self.platforms2) > 0:
        #     for shape in self.platforms2:
        #         self.space.remove(shape, shape.body)
        self.remove_segs()

        if self.ended <= 0:
            for ball in self.balls:
                self.space.remove(ball.shape, ball.shape.body)
        self.balls.clear()
        self.segs = []
        self.tempBallPos = []
        self.platforms = []
        # self.platforms2 = []
        self.slopes.clear()
        self.tileSprites.empty()
        self.tempSprites.empty()

    def load(self):
        self.level.number = self.number
        self.level.platforms = self.platforms
        self.level.platformtemp = self.platformtemp
        self.level.slopes = self.slopes
        self.level.tempPos = self.tempBallPos
        self.level.built()

    # --------------------------------------------------------

    # -------END ------------------------------------------

    # ------- CREATE  FUNCTIONS -----------------------------------------
    # --------------------------------------------------------
    def get_position(self, pos):
        x1, y1 = pos

        # The drawing function will draw a line from 2 point
        if self.X == 0 and self.Y == 0:  # if the pen is not inside the canvas or first start the app
            self.X, self.Y = x1, y1  # pass the current coordinate of the pen
        else:  # draw a line from previous frame location of the pen to current frame position
            # seg = GameObjects.Seg(self.space, 5, 1, (self.X, self.Y), (x1, y1))
            # seg_shape = seg.shape
            self.segs_coor.append(((self.X, self.Y), (x1, y1)))
            self.X, self.Y = x1, y1  # after drawing, the current position become previous position
            # return seg_shape

    def create_segments(self, pos):
        x1, y1 = pos

        # The drawing function will draw a line from 2 point
        if self.X == 0 and self.Y == 0:  # if the pen is not inside the canvas or first start the app
            self.X, self.Y = x1, y1  # pass the current coordinate of the pen
        else:  # draw a line from previous frame location of the pen to current frame position
            seg = GameObjects.Seg(self.space, 5, 1, (self.X, self.Y), (x1, y1))
            seg_shape = seg.shape
            # self.segs_coor.append(((self.X, self.Y), (x1, y1)))
            self.X, self.Y = x1, y1  # after drawing, the current position become previous position
            return seg_shape


    def create_goal(self):
        return ball

    # --------------------------------------------------------
    # -------   END  -----------------------------------------

    # -------   DRAW FUNCTIONS -----------------------------------------
    # --------------------------------------------------------
    def draw_blocks(self, blocks):
        for seg in blocks:
            point1 = seg.a
            point2 = seg.b

            pygame.draw.line(self.screen, (0, 0, 0), point1, point2, 5)

    def draw_path(self, segments):
        for seg in segments:
            if (seg is not None):
                point1 = seg.a
                point2 = seg.b

                pygame.draw.line(self.screen, (0, 0, 0), point1, point2, 5)

    def draw_tmp_path(self, segments):
        for seg in segments:
            point1 = seg[0]
            point2 = seg[1]

            pygame.draw.line(self.screen, (0, 0, 0), point1, point2, 5)

    def draw_border(self, segments):
        for seg in segments:
            point1 = seg.shape.a
            point2 = seg.shape.b

            pygame.draw.line(self.screen, (0, 0, 0), point1, point2, 5)

    def draw_apples(self, balls):
        for ball in balls:
            # pos_x = int(ball.body.position.x)
            # pos_y = int(ball.body.position.y)
            ball.draw(self.screen)
            # pygame.draw.circle(self.screen, ball.color, (pos_x, pos_y), self.RAD)

    def draw_slopes(self, slopes):
        for slope in slopes:
            pos_1 = slope.position[0]
            pos_2 = slope.position[1]
            pos_3 = slope.position[2]

            pygame.draw.polygon(self.screen, slope.color, (pos_1, pos_2, pos_3))

    # --------------------------------------------------------
    # -------   END  -----------------------------------------

    # ------   Remove FUNCTIONS -----------------------------------------
    # --------------------------------------------------------------------------------------
    def remove_segs(self):
        for shape in self.segs:
            if shape is None:
                self.segs.remove(shape)
            else:
                self.space.remove(shape, shape.body)

    # --------------------------------------------------------------------------------------
    # ------   END -----------------------------------------

#
# game = Bubble_tea()
# game.main_loop()
