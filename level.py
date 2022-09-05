import pygame, pymunk
from tiles import Tile
from level_map import tile_size

class Level:
    def __init__(self, level_data, surface, tiles):
        self.display_surface = surface
        self.tileSprites = tiles
        self.setup_level(level_data)

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    self.tileSprites.add(Tile((x, y), tile_size))

    def load_map(self):
        self.tileSprites.draw(self.display_surface)
        self.tileSprites.update(self.display_surface)

    def level1(self, platforms):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 640), (1280, 640), 0)
        platforms.append(shape1)
        self.space.add(box_body, shape1)

    def level2(self, platforms):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 600), (1280, 640), 0)
        platforms.append(shape1)
        self.space.add(box_body, shape1)

    def level3(self, platforms):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 240), (160, 240), 0)
        shape2 = pymunk.Segment(box_body, (160, 240), (400, 480), 0)
        shape3 = pymunk.Segment(box_body, (400, 480), (400, 560), 0)
        shape4 = pymunk.Segment(box_body, (400, 560), (560, 560), 0)
        shape5 = pymunk.Segment(box_body, (560, 560), (560, 480), 0)
        shape6 = pymunk.Segment(box_body, (560, 480), (720, 480), 0)
        shape7 = pymunk.Segment(box_body, (720, 480), (720, 560), 0)
        shape8 = pymunk.Segment(box_body, (720, 560), (880, 560), 0)
        shape9 = pymunk.Segment(box_body, (880, 560), (880, 480), 0)
        shape10 = pymunk.Segment(box_body, (880, 480), (1120, 240), 0)
        shape11 = pymunk.Segment(box_body, (1120, 240), (1280, 240), 0)
        platforms.extend(shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9, shape10,
                         shape11)

        pygame.draw.line(self.screen, (0, 0, 255), (160, 240), (400, 480), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (880, 480), (1120, 240), 1)
        self.space.add(box_body, shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9, shape10,
                       shape11)


    def level4(self, platforms):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (240, 320), (320, 320), 0)
        shape2 = pymunk.Segment(box_body, (320, 320), (320, 480), 0)
        shape3 = pymunk.Segment(box_body, (320, 480), (160, 480), 0)
        shape4 = pymunk.Segment(box_body, (160, 480), (160, 400), 0)
        shape5 = pymunk.Segment(box_body, (160, 400), (240, 400), 0)
        shape6 = pymunk.Segment(box_body, (240, 400), (240, 320), 0)
        shape7 = pymunk.Segment(box_body, (1280, 240), (1040, 240), 0)
        shape8 = pymunk.Segment(box_body, (1040, 240), (560, 720), 0)
        platforms.extend(shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8)

        pygame.draw.line(self.screen, (0, 0, 255), (240, 320), (320, 320), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (320, 320), (320, 480), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (320, 480), (160, 480), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (160, 480), (160, 400), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (160, 400), (240, 400), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (240, 400), (240, 320), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1280, 240), (1040, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1040, 240), (560, 720), 1)
        self.space.add(box_body, shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8)

    def level5(self, platforms):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (560, 160), (960, 160), 0)
        shape2 = pymunk.Segment(box_body, (960, 160), (960, 240), 0)
        shape3 = pymunk.Segment(box_body, (960, 240), (560, 240), 0)
        shape4 = pymunk.Segment(box_body, (560, 240), (560, 160), 0)
        shape5 = pymunk.Segment(box_body, (0, 480), (480, 480), 0)
        shape6 = pymunk.Segment(box_body, (480, 480), (480, 640), 0)
        shape7 = pymunk.Segment(box_body, (480, 640), (960, 640), 0)
        shape8 = pymunk.Segment(box_body, (960, 640), (960, 560), 0)
        shape9 = pymunk.Segment(box_body, (960, 560), (1280, 560), 0)
        platforms.extend(shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9)

        pygame.draw.line(self.screen, (0, 0, 255), (560, 160), (960, 160), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 160), (960, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 240), (560, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (560, 240), (560, 160), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (0, 480), (480, 480), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (480, 480), (480, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (480, 640), (960, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 640), (960, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 560), (1280, 560), 1)
        self.space.add(box_body, shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9)

    def level6(self, platforms):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (560, 240), (640, 240), 0)
        shape2 = pymunk.Segment(box_body, (640, 240), (640, 320), 0)
        shape3 = pymunk.Segment(box_body, (640, 320), (560, 320), 0)
        shape4 = pymunk.Segment(box_body, (560, 320), (560, 240), 0)
        shape5 = pymunk.Segment(box_body, (0, 640), (1280, 640), 0)
        platforms.extend(shape1, shape2, shape3, shape4, shape5)

        pygame.draw.line(self.screen, (0, 0, 255), (560, 240), (640, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (640, 240), (640, 320), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (640, 320), (560, 320), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (560, 320), (560, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (0, 640), (1280, 640), 1)
        self.space.add(box_body, shape1, shape2, shape3, shape4, shape5)

    def level7(self, platforms):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 240), (160, 240), 0)
        shape2 = pymunk.Segment(box_body, (160, 240), (480, 560), 0)
        shape3 = pymunk.Segment(box_body, (480, 560), (960, 560), 0)
        shape4 = pymunk.Segment(box_body, (960, 560), (960, 640), 0)
        shape5 = pymunk.Segment(box_body, (960, 640), (1040, 640), 0)
        shape6 = pymunk.Segment(box_body, (1040, 640), (1040, 480), 0)
        shape7 = pymunk.Segment(box_body, (1040, 480), (1280, 480), 0)
        platforms.extend(shape1, shape2, shape3, shape4, shape5, shape6, shape7)

        pygame.draw.line(self.screen, (0, 0, 255), (0, 240), (160, 240), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (160, 240), (480, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (480, 560), (960, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 560), (960, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (960, 640), (1040, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1040, 640), (1040, 480), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1040, 480), (1280, 480), 1)
        self.space.add(box_body, shape1, shape2, shape3, shape4, shape5, shape6, shape7)

    def level8(self, platforms):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 80), (560, 640), 0)
        shape2 = pymunk.Segment(box_body, (560, 640), (720, 640), 0)
        shape3 = pymunk.Segment(box_body, (720, 640), (1280, 80), 0)
        platforms.extend(shape1, shape2, shape3)

        pygame.draw.line(self.screen, (0, 0, 255), (0, 80), (560, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (560, 640), (720, 640), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (720, 640), (1280, 80), 1)
        self.space.add(box_body, shape1, shape2, shape3)

    def level9(self, platforms):
        box_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape1 = pymunk.Segment(box_body, (0, 160), (400, 560), 0)
        shape2 = pymunk.Segment(box_body, (400, 560), (640, 560), 0)
        shape3 = pymunk.Segment(box_body, (640, 560), (1040, 160), 0)
        shape4 = pymunk.Segment(box_body, (1040, 160), (1280, 160), 0)
        platforms.extend(shape1, shape2, shape3, shape4)

        pygame.draw.line(self.screen, (0, 0, 255), (0, 160), (400, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (400, 560), (640, 560), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (640, 560), (1040, 160), 1)
        pygame.draw.line(self.screen, (0, 0, 255), (1040, 160), (1280, 160), 1)
        self.space.add(box_body, shape1, shape2, shape3, shape4)

    def load_level(self):
        try:
            build_name = "level" + str(self.number)
            getattr(self, build_name)()
        except AttributeError:
            self.number = 0
            build_name = "level" + str(self.number)
            getattr(self, build_name)()