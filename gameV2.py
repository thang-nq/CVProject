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
        self.tileSprites = pygame.sprite.Group()

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
        self.level = Level(self.space, self.number, screen, self.tileSprites, self.platforms)

    # -------COLLISION HANDLER ------------------------------------------
    # -------START ------------------------------------------
    # Define collision callback function, will be called when X touches Y
    def through(self, arbiter, space, data):
        return False

    def goal_reached(self, arbiter, space, data):
        if self.ended == 0:
            print("you reached the goal!")
            self.ended += 1
        return True

    # Define collision callback function, will be called when X touches Y
    def finished(self, arbiter, space, data):
        ball_shape1 = arbiter.shapes[0]
        space.remove(ball_shape1, ball_shape1.body)
        ball_shape2 = arbiter.shapes[1]
        space.remove(ball_shape2, ball_shape2.body)
        return True

    def collide_reset_game(self, arbiter, space, data):
        # FIX HERE =============================================
        print("trigger!")
        self.gameStart = 0
        for shape in self.space.shapes:
            if (shape.collision_type != self.collision['border']):
                self.space.remove(shape, shape.body)
        self.balls = []
        self.segs = []
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

            if event.type == pygame.MOUSEBUTTONUP and self.gameStart < 1:
                self.balls.append(GameObjects.Dot(self.space, self.RAD, (200, 200), 'ball').getShape())
                self.balls.append(self.create_goal().getShape())
                self.gameStart += 1

    def draw (self):
        self.screen.fill((247, 247, 247))
        if self.gameStart == 0:
            pygame.draw.circle(self.screen, (0, 0, 0), (200, 200), self.RAD)
            pygame.draw.circle(self.screen, (255, 0, 0), (400, 200), self.RAD)

        self.draw_apples(self.balls)
        self.draw_path(self.segs)
        
        self.border.draw(self.screen)
        self.tileSprites.draw(self.screen)

    def restart(self):
        self.gameStart = 0
        for ball in self.balls:
            self.space.remove(ball.shape,ball.shape.body)

        for shape in self.segs:
            self.space.remove(shape, shape.body)

        self.balls = []
        self.segs = []
        self.draw()

    def clear(self):
        self.gameStart = 0
        
        for shape in self.platforms:
            self.space.remove(shape, shape.body)
        for shape in self.balls:
            self.space.remove(shape, shape.body)
        for shape in self.segs:
            if shape is None:
                self.segs.remove(shape)
            else:
                self.space.remove(shape, shape.body)
        self.balls = []
        if self.ended == 0 :
            for ball in self.balls:
                self.space.remove(ball.shape,ball.shape.body)
        self.balls.clear()
        self.segs = []
        self.platforms = []
        self.tileSprites.empty()

    def load(self):
        self.level.number = self.number
        self.level.platforms = self.platforms
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

    def create_segments2(self, segs_coor):
        for seg in segs_coor:
            pos1 = seg[0]
            pos2 = seg[1]
            seg = GameObjects.Seg2(self.space, 5, 1, pos1, pos2)
            seg_shape = seg.shape
            self.segs.append(seg_shape)

    def create_goal(self):
        ball = GameObjects.Dot(self.space, self.RAD, (400, 200), 'goal', color=(255, 0, 0))

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
            pos_x = int(ball.body.position.x)
            pos_y = int(ball.body.position.y)

            pygame.draw.circle(self.screen,(255,255,0), (pos_x, pos_y), self.RAD)

    # --------------------------------------------------------
    # -------   END  -----------------------------------------

    # ------   Level loader FUNCTIONS -----------------------------------------
    # --------------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------------
    # ------   END -----------------------------------------

#
# game = Bubble_tea()
# game.main_loop()
