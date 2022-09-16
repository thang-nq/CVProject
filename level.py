from asyncio import constants
import pygame, pymunk

import GameObjects
import GameSprites
import level_map
import Constants


class Level:
    def __init__(self, space, surface, level_num, tilesSprites, platforms,platformtemp, slopes, balls, ballsPos):
        self.screen = surface
        self.space = space
        self.tileSprites = tilesSprites
        self.number = level_num
        self.slopes = slopes
        self.balls = balls
        self.tempPos = ballsPos
        self.platforms = platforms
        self.platformtemp = platformtemp
        self.player = pygame.image.load('assets/MilkTeaImages/Bubble_Small.png').convert_alpha()
        self.goal_img = pygame.image.load('assets/MilkTeaImages/TeaBall.png').convert_alpha()
        self.die_img = pygame.image.load('assets/MilkTeaImages/MilkBall.png').convert_alpha()

        self.setup_level(level_map.getMap(level_num))
        self.load_level()

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * level_map.tile_size
                y = row_index * level_map.tile_size
                if cell == 'X':
                    self.tileSprites.add(GameSprites.Tile((x, y), level_map.tile_size))

    def built(self):
        self.setup_level(level_map.getMap(self.number))
        self.load_level()

    def level1(self):
        shape1 = GameObjects.Seg(self.space, 2, 1, (0, 700), (Constants.WIDTH, 700), elastic=0).getShape()
        self.tempPos.append((Constants.WIDTH * 0.35, 200))
        self.tempPos.append((Constants.WIDTH * 0.65, 200))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[0], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.player))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[1], (Constants.GOAL_RAD * 2.18, Constants.GOAL_RAD * 2.18), self.goal_img))

        self.platforms.append(shape1)

    def level2(self):
        shape1 = GameObjects.Seg(self.space, 2, 1, (0, 700), (Constants.WIDTH, 700), elastic=0).getShape()
        self.platforms.append(shape1)
        self.tempPos.append((Constants.WIDTH * 0.35, 200))
        self.tempPos.append((Constants.WIDTH * 0.65, 650))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[0], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.player, color=(103,192,169)))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[1], (Constants.GOAL_RAD * 2.18, Constants.GOAL_RAD * 2.18), self.goal_img, color=(241,186,80)))

    def level3(self):
        shape1 = GameObjects.Seg(self.space, 0, 1, (0, 300), (200, 300), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (200, 300), (600, 700), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (600, 700), (700, 700), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (700, 700), (700, 600), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (700, 600), (800, 600), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (800, 600), (800, 700), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1, (800, 700), (900, 700), elastic=0).getShape()
        shape8 = GameObjects.Seg(self.space, 0, 1, (900, 700), (1300, 300), elastic=0).getShape()
        shape9 = GameObjects.Seg(self.space, 0, 1, (1300, 300), (1500, 300), elastic=0).getShape()

        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9])

        self.slopes.append(GameSprites.Slope((200, 300), (200, 700), (600, 700)))
        self.slopes.append(GameSprites.Slope((1300, 300), (1300, 700), (900, 700)))

        self.tempPos.append((210, 250))
        self.tempPos.append((1290, 250))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[0], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.player))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[1], (Constants.GOAL_RAD * 2.18, Constants.GOAL_RAD * 2.18), self.goal_img))

    def level4(self):

        shape1 = GameObjects.Seg(self.space, 0, 1, (350, 300), (400, 300), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (400, 300), (400, 450), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (400, 450), (250, 450), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (250, 450), (250, 400), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (250, 400), (350, 400), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (350, 400), (350, 300), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1, (1500, 300), (1300, 300), elastic=0).getShape()
        shape8 = GameObjects.Seg(self.space, 0, 1, (1300, 300), (700, 800), elastic=0).getShape()

        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8])
        self.slopes.append(GameSprites.Slope((1300, 300), (1300, 800), (700, 800)))

        self.tempPos.append((150, 300))
        self.tempPos.append((1290, 250))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[0], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.player))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[1], (Constants.GOAL_RAD * 2.18, Constants.GOAL_RAD * 2.18), self.goal_img))

    def level5(self):
        shape1 = GameObjects.Seg(self.space, 0, 1, (650, 300), (1050, 300), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (1050, 300), (1050, 350), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (1050, 350), (650, 350), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (650, 350), (650, 300), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (0, 500), (550, 500), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (550, 500), (550, 700), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1, (550, 700), (1050, 700), elastic=0).getShape()
        shape8 = GameObjects.Seg(self.space, 0, 1, (1050, 700), (1050, 650), elastic=0).getShape()
        shape9 = GameObjects.Seg(self.space, 0, 1, (1050, 650), (1500, 650), elastic=0).getShape()

        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9])

        self.tempPos.append((1030, 630))
        self.tempPos.append((Constants.WIDTH * 0.65, 150))

        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[0], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.player))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[1], (Constants.GOAL_RAD * 2.18, Constants.GOAL_RAD * 2.18), self.goal_img))

    def level6(self):

        shape1 = GameObjects.Seg(self.space, 2, 1, (0, 700), (Constants.WIDTH, 700), elastic=0).getShape()
        self.platforms.extend([shape1])

        self.tempPos.append((Constants.WIDTH * 0.35, 200))
        self.tempPos.append((Constants.WIDTH * 0.65, 200))
        self.tempPos.append((Constants.WIDTH * 0.5, 200))

        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[0], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.player))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[1], (Constants.GOAL_RAD * 2.18, Constants.GOAL_RAD * 2.18), self.goal_img))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[2], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.die_img))

    def level7(self):
        shape1 = GameObjects.Seg(self.space, 0, 1, (0, 300), (200, 300), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (200, 300), (600, 650), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (600, 650), (1050, 650), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (1050, 650), (1050, 700), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (1050, 700), (1150, 700), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (1150, 700), (1150, 600), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1, (1150, 600), (1500, 600), elastic=0).getShape()

        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7])
        self.slopes.append(GameSprites.Slope((200, 300), (200, 650), (600, 650)))

        self.tempPos.append((210, 150))
        self.tempPos.append((1100, 650))
        self.tempPos.append((400, 200))

        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[0], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.player))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[1], (Constants.GOAL_RAD * 2.18, Constants.GOAL_RAD * 2.18), self.goal_img))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[2], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.die_img))

    def level8(self):
        shape1 = GameObjects.Seg(self.space, 0, 1, (0, 150), (700, 700), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (700, 700), (800, 700), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (800, 700), (1500, 150), elastic=0).getShape()
        self.platforms.extend([shape1, shape2, shape3])

        self.slopes.append(GameSprites.Slope((0, 150), (0, 700), (700, 700)))
        self.slopes.append(GameSprites.Slope((1500, 150), (1500, 700), (800, 700)))

        self.tempPos.append((1250, 100))
        self.tempPos.append((750, 650))
        self.tempPos.append((1150, 200))

        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[0], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.player))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[1], (Constants.GOAL_RAD * 2.18, Constants.GOAL_RAD * 2.18), self.goal_img))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[2], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.die_img))

    def level9(self):
        shape1 = GameObjects.Seg(self.space, 0, 1, (0, 300), (500, 700), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (500, 700), (600, 700), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (600, 700), (1200, 150), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (1200, 150), (1500, 150), elastic=0).getShape()

        self.platforms.extend([shape1, shape2, shape3, shape4])

        self.slopes.append(GameSprites.Slope((0, 300), (0, 700), (500, 700)))
        self.slopes.append(GameSprites.Slope((1200, 150), (1200, 700), (600, 700)))

        self.tempPos.append((1150, 100))
        self.tempPos.append((550, 650))
        self.tempPos.append((1050, 200))
        self.tempPos.append((200, 100))

        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[0], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.player))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[1], (Constants.GOAL_RAD * 2.18, Constants.GOAL_RAD * 2.18), self.goal_img))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[2], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.die_img))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[3], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.die_img))

    def level10(self):
        shape1 = GameObjects.Seg(self.space, 5, 1, (0, 700), (1500, 700), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 1, 1, (450, 700), (450, 450), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (450, 450), (500, 450), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (500, 450), (500, 700), elastic=0).getShape()

        shape5 = GameObjects.Seg(self.space, 0, 1, (1000, 700), (1000, 450), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (1000, 450), (1050, 450), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1, (1050, 450), (1050, 700), elastic=0).getShape()
        shape8 = GameObjects.Seg(self.space, 0, 1, (1050, 700), (1050, Constants.WIDTH), elastic=0).getShape()

        shape9 = GameObjects.Seg(self.space, 0, 1, (650, 0), (650, 350), elastic=0).getShape()
        shape10 = GameObjects.Seg(self.space, 0, 1, (650, 350), (850, 350), elastic=0).getShape()
        shape11 = GameObjects.Seg(self.space, 0, 1, (850, 350), (850, 0), elastic=0).getShape()

        shape12 = ((100, 250), (300, 250))
        shape13 = ((1400, 250), (1200, 250))

        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9, shape10,shape11])
        self.platformtemp.extend([shape12,shape13])

        self.tempPos.append((100, 250))
        self.tempPos.append((1400, 250))
        self.tempPos.append((300, 200))
        self.tempPos.append((1200, 200))

        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[0], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.player))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[1], (Constants.GOAL_RAD * 2.18, Constants.GOAL_RAD * 2.18), self.goal_img))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[2], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.die_img))
        # self.balls.add(
        #     GameSprites.Ball(self.tempPos[3], (Constants.PLAYER_RAD * 2.38, Constants.PLAYER_RAD * 2.38), self.die_img))

        pygame.draw.line(self.screen, (60, 61, 71), (50, 250), (400, 225), 5)
        pygame.draw.line(self.screen, (60, 61, 71), (1450, 250), (1100, 225), 5)


    def load_level(self):
        try:
            build_name = "level" + str(self.number)
            getattr(self, build_name)()
        except AttributeError:
            self.number = 1
            build_name = "level" + str(self.number)
            getattr(self, build_name)()
