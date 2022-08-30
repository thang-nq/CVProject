import pygame
from tiles import Tile
from settings import tile_size

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
    def load_map(self):

        self.tiles.draw(self.display_surface)
        self.tiles.update(self.display_surface)
        self.player.update()
        self.player.draw(self.display_surface)