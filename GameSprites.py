import pygame, pymunk, Constants

collision = Constants.COLLISION_TYPES
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((60, 61, 71))
        self.rect = self.image.get_rect(topleft=pos)

class Slope():
    def __init__(self,pos1,pos2,pos3):
        self.color = (60,61,71)
        self.position = (pos1,pos2,pos3)

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, size, img_path ):
        super().__init__()
        self.image = img_path
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()
        self.rect.center = pos
