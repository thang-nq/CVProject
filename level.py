from asyncio import constants
import pygame, pymunk

import GameObjects
from tiles import Tile,Slope
import level_map
import Constants

class Level:
    def __init__(self, space, level_num, surface, tilesSprites, platforms,slopes):
        self.screen = surface
        self.space = space
        self.tileSprites = tilesSprites
        self.number = level_num
        self.slopes = slopes

        self.setup_level(level_map.getMap(level_num))
        self.platforms = platforms
        self.load_level()

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * level_map.tile_size
                y = row_index * level_map.tile_size
                if cell == 'X':
                    self.tileSprites.add(Tile((x, y), level_map.tile_size))

    def built(self):
        self.setup_level(level_map.getMap(self.number))
        self.load_level()

    def level1(self):
        shape1 = GameObjects.Seg(self.space, 2, 1, (0, 700), (Constants.WIDTH, 700), elastic=0).getShape()
        self.platforms.append(shape1)


    def level2(self):

        shape1 = GameObjects.Seg(self.space, 2, 1, (0, 700), (Constants.WIDTH, 700), elastic=0).getShape()
        self.platforms.append(shape1)

    def level3(self):
        shape1 = GameObjects.Seg(self.space, 0, 1, (0, 300), (200, 300), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (200,300),(600,700), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (600,700),(700,700), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (700,700),(700,600), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (700,600),(800,600), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (800,600),(800,700), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1, (800, 700), (900, 700), elastic=0).getShape()
        shape8 = GameObjects.Seg(self.space, 0, 1, (900, 700), (1300, 300), elastic=0).getShape()
        shape9 = GameObjects.Seg(self.space, 0, 1, (1300, 300), (1500, 300), elastic=0).getShape()
       
        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9])

        self.slopes.append(Slope((200,300),(200,700),(600,700)))
        self.slopes.append(Slope((1300,300),(1300,700),(900,700)))

    def level4(self):

        shape1 = GameObjects.Seg(self.space, 0, 1, (350,300),(400,300), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (400,300),(400,450), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (400,450),(250,450), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (250,450),(250,400), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (250,400),(350,400), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (350,400),(350,300), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1, (1500,300), (1300,300), elastic=0).getShape()
        shape8 = GameObjects.Seg(self.space, 0, 1, (1300,300), (700,800), elastic=0).getShape()


        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8])
        self.slopes.append(Slope((1300,300),(1300,800),(700,800)))

    def level5(self):
        shape1 = GameObjects.Seg(self.space, 0, 1,(650,300),(1050,300), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (1050,300), (1050, 350), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (1050,350), (650, 350), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (650, 350), (650,300 ), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (0, 500), (550,500), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (550, 500), (550, 700), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1,(550, 700), (1050, 700), elastic=0).getShape()
        shape8 = GameObjects.Seg(self.space, 0, 1, (1050, 700), (1050, 650), elastic=0).getShape()
        shape9 = GameObjects.Seg(self.space, 0, 1, (1050,650), (1500, 650), elastic=0).getShape()

        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9])

    def level6(self):

        shape1 = GameObjects.Seg(self.space, 2, 1, (0, 700), (Constants.WIDTH, 700), elastic=0).getShape()
        self.platforms.extend([shape1])



    def level7(self):
        shape1 = GameObjects.Seg(self.space, 0, 1,  (0,300),(200,300), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (200, 300), (600, 650), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (600,650),(1050,650), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (1050, 650), (1050, 700), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (1050, 700), (1150, 700), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (1150,700), (1150, 600), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1, (1150, 600), (1500, 600), elastic=0).getShape()

        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7])
        self.slopes.append(Slope((200,300),(200,650),(600,650)))

    def level8(self):
        shape1 = GameObjects.Seg(self.space, 0, 1, (0,150),(700,700), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (700,700), (800, 700), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (800,700), (1500, 150), elastic=0).getShape()
        self.platforms.extend([shape1, shape2, shape3])

        self.slopes.append(Slope((0,150),(0,700),(700,700)))
        self.slopes.append(Slope((1500,150),(1500,700),(800,700)))


    def level9(self):
        shape1 = GameObjects.Seg(self.space, 0, 1,  (0,300),(500,700), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (500, 700), (600, 700), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (600,700), (1200, 150), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (1200, 150), (1500, 150), elastic=0).getShape()

        self.platforms.extend([shape1, shape2, shape3, shape4])

        self.slopes.append(Slope((0,300),(0,700),(500,700)))
        self.slopes.append(Slope((1200,150),(1200,700),(600,700)))



    def load_level(self):
        try:
            build_name = "level" + str(self.number)
            getattr(self, build_name)()
        except AttributeError:
            self.number = 1
            build_name = "level" + str(self.number)
            getattr(self, build_name)()
