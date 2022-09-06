import pygame, pymunk

import GameObjects
from tiles import Tile
import level_map


class Level:
    def __init__(self, space, level_num, surface, tilesSprites, platforms):
        self.screen = surface
        self.space = space
        self.tileSprites = tilesSprites
        self.number = level_num

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
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 640), (1280, 640), 0)
        self.platforms.append(shape1)
        self.space.add(box_body, shape1)

    def level2(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 600), (1280, 640), 0)
        self.platforms.append(shape1)
        self.space.add(box_body, shape1)

    def level3(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = GameObjects.Seg(self.space, 0, 1, (0, 240), (160, 240), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (160, 240), (400, 480), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (400, 480), (400, 560), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (400, 560), (560, 560), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (560, 560), (560, 480), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (560, 480), (720, 480), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1, (720, 480), (720, 560), elastic=0).getShape()
        shape8 = GameObjects.Seg(self.space, 0, 1, (720, 560), (880, 560), elastic=0).getShape()
        shape9 = GameObjects.Seg(self.space, 0, 1, (880, 560), (880, 480), elastic=0).getShape()
        shape10 = GameObjects.Seg(self.space, 0, 1, (880, 480), (1120, 240), elastic=0).getShape()
        shape11 = GameObjects.Seg(self.space, 0, 1, (1120, 240), (1280, 240), elastic=0).getShape()
        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9, shape10,
                               shape11])

        pygame.draw.line(self.screen, (0, 0, 255), (160, 240), (400, 480), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (880, 480), (1120, 240), 1)

    def level4(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = GameObjects.Seg(self.space, 0, 1, (240, 320), (320, 320), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (320, 320), (320, 480), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (320, 480), (160, 480), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (160, 480), (160, 400), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (160, 400), (240, 400), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (240, 400), (240, 320), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1, (1280, 240), (1040, 240), elastic=0).getShape()
        shape8 = GameObjects.Seg(self.space, 0, 1, (1040, 240), (560, 720), elastic=0).getShape()


        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8])

        pygame.draw.line(self.screen, (0, 0, 255), (240, 320), (320, 320), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (320, 320), (320, 480), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (320, 480), (160, 480), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (160, 480), (160, 400), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (160, 400), (240, 400), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (240, 400), (240, 320), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1280, 240), (1040, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1040, 240), (560, 720), 1)


    def level5(self):

        shape1 = GameObjects.Seg(self.space, 0, 1,(560, 160), (960, 160), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (960, 160), (960, 240), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (960, 240), (560, 240), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (560, 240), (560, 160), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (0, 480), (480, 480), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (480, 480), (480, 640), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1, (480, 640), (960, 640), elastic=0).getShape()
        shape8 = GameObjects.Seg(self.space, 0, 1, (960, 640), (960, 560), elastic=0).getShape()
        shape9 = GameObjects.Seg(self.space, 0, 1, (960, 560), (1280, 560), elastic=0).getShape()

        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9])

        pygame.draw.line(self.screen, (0, 0, 255), (560, 160), (960, 160), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 160), (960, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 240), (560, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (560, 240), (560, 160), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (0, 480), (480, 480), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (480, 480), (480, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (480, 640), (960, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 640), (960, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 560), (1280, 560), 1)


    def level6(self):
        shape1 = GameObjects.Seg(self.space, 0, 1,(560, 240), (640, 240), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (640, 240), (640, 320), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (640, 320), (560, 320), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (560, 320), (560, 240), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (0, 640), (1280, 640), elastic=0).getShape()

        self.platforms.extend([shape1, shape2, shape3, shape4, shape5])

        pygame.draw.line(self.screen, (0, 0, 255), (560, 240), (640, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (640, 240), (640, 320), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (640, 320), (560, 320), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (560, 320), (560, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (0, 640), (1280, 640), 1)


    def level7(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = GameObjects.Seg(self.space, 0, 1, (0, 240), (160, 240), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (160, 240), (480, 560), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (480, 560), (960, 560), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (960, 560), (960, 640), elastic=0).getShape()
        shape5 = GameObjects.Seg(self.space, 0, 1, (960, 640), (1040, 640), elastic=0).getShape()
        shape6 = GameObjects.Seg(self.space, 0, 1, (1040, 640), (1040, 480), elastic=0).getShape()
        shape7 = GameObjects.Seg(self.space, 0, 1, (1040, 480), (1280, 480), elastic=0).getShape()

        self.platforms.extend([shape1, shape2, shape3, shape4, shape5, shape6, shape7])

        pygame.draw.line(self.screen, (0, 0, 255), (0, 240), (160, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (160, 240), (480, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (480, 560), (960, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 560), (960, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 640), (1040, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1040, 640), (1040, 480), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1040, 480), (1280, 480), 1)


    def level8(self):

        shape1 = GameObjects.Seg(self.space, 0, 1, (0, 80), (560, 640), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (560, 640), (720, 640), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (720, 640), (1280, 80), elastic=0).getShape()
        self.platforms.extend([shape1, shape2, shape3])

        pygame.draw.line(self.screen, (0, 0, 255), (0, 80), (560, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (560, 640), (720, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (720, 640), (1280, 80), 1)

    def level9(self):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = GameObjects.Seg(self.space, 0, 1, (0, 160), (400, 560), elastic=0).getShape()
        shape2 = GameObjects.Seg(self.space, 0, 1, (400, 560), (640, 560), elastic=0).getShape()
        shape3 = GameObjects.Seg(self.space, 0, 1, (640, 560), (1040, 160), elastic=0).getShape()
        shape4 = GameObjects.Seg(self.space, 0, 1, (1040, 160), (1280, 160), elastic=0).getShape()

        self.platforms.extend([shape1, shape2, shape3, shape4])

        pygame.draw.line(self.screen, (0, 0, 255), (0, 160), (400, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (400, 560), (640, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (640, 560), (1040, 160), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1040, 160), (1280, 160), 1)


    def load_level(self):
        try:
            build_name = "level" + str(self.number)
            getattr(self, build_name)()
        except AttributeError:
            self.number = 1
            build_name = "level" + str(self.number)
            getattr(self, build_name)()
