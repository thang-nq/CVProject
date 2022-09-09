import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill((60,61,71))
        self.rect = self.image.get_rect(topleft = pos)
class Slope():
    def __init__(self,pos1,pos2,pos3):
        self.color = (60,61,71)
        self.position = (pos1,pos2,pos3)
