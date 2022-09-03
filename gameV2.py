import cv2
import numpy as np
import os
import pygame
import pymunk
import GameObjects
import Constants
import GameUI


class Bubble_tea:
    def __init__(self,screen):
        # pygame.init()
        # pygame.font.init()

        self.WIDTH, self.HEIGHT = Constants.WIDTH, Constants.HEIGHT
        self.screen = screen

        # self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        self.space = pymunk.Space()
        self.space.gravity = (0, 981)

        # CONSTANTS
        self.FPS = 60
        self.VEL = 5
        self.DT = 1 / self.FPS
        self.RAD = 20
        self.LINE_WEIGHT = 10
        # Add a new collision type
        self.collision = Constants.COLLISION_TYPES

        # ------- CREATE BORDER ------------------------------------------
        self.border = []
        self.border.extend(
            [GameObjects.Seg(self.space, 1, 1, (0, 0), (0, self.HEIGHT), elastic=0, collisionType="border"),
             GameObjects.Seg(self.space, 1, 1, (0, self.HEIGHT), (self.WIDTH, self.HEIGHT), elastic=0,
                             collisionType="border"),
             GameObjects.Seg(self.space, 1, 1, (self.WIDTH, self.HEIGHT), (self.WIDTH, 0), elastic=0,
                             collisionType="border"),
             GameObjects.Seg(self.space, 1, 1, (self.WIDTH, 0), (0, 0), elastic=0, collisionType="border")])

        # Variables
        self.gameStart = 0
        self.ended = 0
        self.number = 1

        # Arrays
        self.apples = []
        self.blocks = []
        self.segs = []
        self.tiles = pygame.sprite.Group()

        #Varibles
        self.X, self.Y = 0, 0
        self.x_mouse, self.y_mouse = 0, 0
        self.game_state = 0
        self.inGameUI = GameUI.inGameUI(self.screen)

        # Setup the collision callback function
        self.h = self.space.add_collision_handler(self.collision['ball'], self.collision['goal'])
        self.b1 = self.space.add_collision_handler(self.collision['ball'], self.collision['border'])
        self.b2 = self.space.add_collision_handler(self.collision['goal'], self.collision['border'])
        self.b1.begin = self.through
        self.b2.begin = self.through
        self.b1.separate = self.reset_game
        self.b2.separate = self.reset_game

        # self.level1 = Level(level_map1, self.screen)
        # self.level2 = Level(level_map2, self.screen)

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

    def reset_game(self, arbiter, space, data):
        self.gameStart = False
        for shape in self.space.shapes:
            if shape.collision_type != self.collision['border']:
                self.space.remove(shape, shape.body)
        self.apples = []
        self.segs = []
        self._draw()
        return False

    # -------END ------------------------------------------

    # ------- MAIN LOOP ------------------------------------------
    def main_loop(self):
        while True:
            self.event_hanlder()
            self.draw()
            self.update()

    # ------- CORE FUNCTIONS ------------------------------------------
    # --------------------------------------------------------

    def update(self):
        if self.game_state != 1:
            self.space.step(self.DT)
        # pygame.display.update()
        # self.clock.tick(self.FPS)

    def event_hanlder(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.X, self.Y = pygame.mouse.get_pos()
                    # self.x_mouse, self.y_mouse = pygame.mouse.get_pos()
                    # print(self.x_mouse)
                    # if (self.x_mouse < 60 and self.y_mouse < 155 and self.y_mouse > 90):
                    #     self.game_state = 1
                    #     print(self.game_state)
                    # if self.game_state == 1:
                    #     if self.x_mouse > 500 and self.y_mouse > 200 and self.y_mouse < 300:
                    # Resume in the paused screen
                    # self.game_state = 0
                    # if self.x_mouse > 500 and self.y_mouse > 300:
                    # Restart in the paused screen
                    # restart()
                    # level.load_level()
                    # self.game_state = 0

            if pygame.mouse.get_pressed()[0]:
                mpos = pygame.mouse.get_pos()
                self.segs.append(self.create_segments(mpos))

            if event.type == pygame.MOUSEBUTTONUP and self.gameStart < 1:
                # self.create_segments(self.segs_coor)
                self.apples.append(GameObjects.Dot(self.space, self.RAD, (200, 200), 'ball'))
                self.apples.append(self.create_goal())
                self.gameStart += 1

    def draw(self):
        self.screen.fill((247, 247, 247))

        if self.gameStart == 0:
            pygame.draw.circle(self.screen, (0, 0, 0), (200, 200), self.RAD)
            pygame.draw.circle(self.screen, (255, 0, 0), (400, 200), self.RAD)

        self.draw_apples(self.apples)
        self.draw_path(self.segs)
        self.draw_border(self.border)

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
        seg = GameObjects.Dot(self.space, self.RAD, (400, 200), 'goal', color=(255, 0, 0))
        self.h.begin = self.goal_reached
        self.h.separate = self.finished
        return seg


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
            if(seg is not None):
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

    def draw_apples(self, apples):
        for apple in apples:
            pos_x = int(apple.body.position.x)
            pos_y = int(apple.body.position.y)

            pygame.draw.circle(self.screen, apple.color, (pos_x, pos_y), self.RAD)

    # --------------------------------------------------------
    # -------   END  -----------------------------------------

    # ------   Level loader FUNCTIONS -----------------------------------------
    # --------------------------------------------------------------------------------------


    # --------------------------------------------------------------------------------------
    # ------   END -----------------------------------------


# game = Bubble_tea()
# game.main_loop()
