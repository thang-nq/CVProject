import cv2
import numpy as np
import os
import pygame
import pymunk
import GameObjects
import Constants


class Bubble_tea:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.WIDTH, self.HEIGHT = Constants.WIDTH, Constants.HEIGHT
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
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
        self.collision = {"ball": 1, "goal": 2, "border": 3, "line": 4}

        # ------- CREATE BORDER ------------------------------------------
        self.border = []
        self.border.append(
            GameObjects.Seg(self.space, 1, 1, (0, 0), (0, self.HEIGHT), elastic=0, collisionType="border"))
        self.border.append(GameObjects.Seg(self.space, 1, 1, (0, self.HEIGHT), (self.WIDTH, self.HEIGHT), elastic=0,
                                           collisionType="border"))
        self.border.append(GameObjects.Seg(self.space, 1, 1, (self.WIDTH, self.HEIGHT), (self.WIDTH, 0), elastic=0,
                                           collisionType="border"))
        self.border.append(
            GameObjects.Seg(self.space, 1, 1, (self.WIDTH, 0), (0, 0), elastic=0, collisionType="border"))

        # Variables
        self.gameStart = False
        self.ended = 0
        self.X, self.Y = 0, 0
        self.apples = []
        self.blocks = []
        self.segs = []
        self.x_mouse, self.y_mouse = 0, 0
        self.game_state = 0

        # Setup the collision callback function
        self.h = self.space.add_collision_handler(self.collision['ball'], self.collision['goal'])
        self.b1 = self.space.add_collision_handler(self.collision['ball'], self.collision['border'])
        self.b2 = self.space.add_collision_handler(self.collision['goal'], self.collision['border'])
        self.b1.begin = self.through
        self.b2.begin = self.through
        self.b1.separate = self.reset_game
        self.b2.separate = self.reset_game

    # -------COLLISION HANDLER ------------------------------------------
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

    # -------END ------------------------------------------
    # ------- MAIN LOOP ------------------------------------------
    def main_loop(self):
        while True:
            self.create_blocks()
            self._event_hanlder()
            self._draw()
            self._update()

    def reset_game(self, arbiter, space, data):
        self.gameStart = False
        for shape in self.space.shapes:
            if shape.collision_type != self.collision['border']:
                self.space.remove(shape, shape.body)
        self.apples = []
        self.segs = []
        self._draw()
        return False

    # ------- CORE FUNCTIONS ------------------------------------------
    def _update(self):
        if self.game_state != 1:
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
                    self.x_mouse, self.y_mouse = pygame.mouse.get_pos()
                    print(self.x_mouse)
                    if (self.x_mouse < 60 and self.y_mouse < 155 and self.y_mouse > 90):
                        self.game_state = 1
                        print(self.game_state)
                    if self.game_state == 1:
                        if self.x_mouse > 500 and self.y_mouse > 200 and self.y_mouse < 300:
                            # Resume in the paused screen
                            self.game_state = 0
                        if self.x_mouse > 500 and self.y_mouse > 300:
                            # Restart in the paused screen
                            restart()
                            level.load_level()
                            self.game_state = 0

            if pygame.mouse.get_pressed()[0]:
                mpos = pygame.mouse.get_pos()
                self.segs.append(self.create_segments(mpos))

            if event.type == pygame.MOUSEBUTTONUP:
                self.apples.append(GameObjects.Dot(self.space, self.RAD, (200, 200), 'ball'))
                self.apples.append(self.create_goal())
                self.gameStart = True



    def _draw(self):
        self.screen.fill((247, 247, 247))
        if not self.gameStart:
            pygame.draw.circle(self.screen, (0, 0, 0), (200, 200), self.RAD)
            pygame.draw.circle(self.screen, (255, 0, 0), (400, 200), self.RAD)

        self.draw_apples(self.apples)
        self.draw_path(self.segs)
        self.draw_border(self.border)

    # -------END ------------------------------------------
    # ------- CREATE  FUNCTIONS -----------------------------------------
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
        seg = GameObjects.Dot(self.space, self.RAD, (400, 200), 'goal', color=(255, 0, 0))
        self.h.begin = self.goal_reached
        self.h.separate = self.finished
        return seg

    def create_blocks(self):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)

        body.position = (100, 100)
        shape = pymunk.Poly.create_box(body, (200, 100))
        self.space.add(body, shape)
        # pygame.draw.rect(self.screen,(0,0,0),())
        return shape

    # -------   END  -----------------------------------------

    # -------   DRAW FUNCTIONS -----------------------------------------
    def draw_blocks(self, blocks):
        for seg in segments:
            point1 = seg.a
            point2 = seg.b

            pygame.draw.line(self.screen, (0, 0, 0), point1, point2, 5)

    def draw_path(self, segments):
        for seg in segments:

            point1 = seg.a
            point2 = seg.b

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

    # -------   END  -----------------------------------------


game = Bubble_tea()
game.main_loop()
