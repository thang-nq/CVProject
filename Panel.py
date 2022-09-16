import pygame
pygame.init()
# property------------------------------------------------------------------------------------------
font = pygame.font.SysFont("Ravie", 40)
tickBox_img = pygame.image.load('assets/MilkTeaImages/TickBox.png')
tick_img = pygame.image.load('assets/MilkTeaImages/Tick.png')
iconX = -180
contentX = -80
tickBoxX = 150


# about us box
# about us box has pivot of top left
desFont = pygame.font.SysFont("Comic Sans MS", 16)
profileX = 10
nameX = 30
nameY = 20
sidX = 30
sidY = 40
descriptionX = 30
descriptionY = 60


# panel------------------------------------------------------------------------------------------
class GamePanel():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x - width * scale / 2, y - height * scale / 2)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class Icon():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x - width * scale / 2, y - height * scale / 2)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class TickBox():
    def __init__(self, x, y, scale, state):

        width = tickBox_img.get_width()
        height = tickBox_img.get_height()
        self.tickBox = pygame.transform.scale(tickBox_img, (int(width * scale), int(height * scale)))
        width = tick_img.get_width()
        height = tick_img.get_height()
        self.tick = pygame.transform.scale(tick_img, (int(width * scale), int(height * scale)))
        self.online = state
        self.rect = self.tickBox.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        surface.blit(self.tickBox, (self.rect.x, self.rect.y))
        if (self.online):
            surface.blit(self.tick, (self.rect.x, self.rect.y))
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.online = not self.online
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return self.online


class SettingCompBox():
    def __init__(self, x, y, icon_img, content, scale):
        width = icon_img.get_width()
        height = icon_img.get_height()
        self.image = pygame.transform.scale(icon_img, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x - width * scale / 2, y - height * scale / 2)
        self.content = font.render(str(content), True, (255, 255, 255))
        self.online = True
        self.tickBox = TickBox(self.rect.x + tickBoxX, self.rect.y, 1, self.online)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x + iconX, self.rect.y))
        textHeight = self.content.get_height()
        surface.blit(self.content,
                     (self.rect.x + contentX, self.rect.y + textHeight / 2))
        self.online = self.tickBox.draw(surface)
        return self.online


class AboutUsCompBox():
    def __init__(self, x, y, icon_img, name, sid, content, scale):
        width = icon_img.get_width()
        height = icon_img.get_height()
        self.image = pygame.transform.scale(icon_img, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x - width * scale / 2, y - height * scale / 2)
        self.content = desFont.render(str(content), True, (255, 255, 255))
        self.name = desFont.render(str(name), True, (255, 255, 255))
        self.sid = desFont.render(str(sid), True, (255, 255, 255))
        self.online = True

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x + iconX, self.rect.y))
        nameHeight = self.name.get_height()
        surface.blit(self.name, (self.rect.x + nameX, self.rect.y + nameY + nameHeight / 2))
        sidHeight = self.name.get_height()
        surface.blit(self.sid, (self.rect.x + sidX, self.rect.y + sidY + sidHeight / 2))
        textHeight = self.content.get_height()
        surface.blit(self.content,
                     (self.rect.x + descriptionX, self.rect.y + descriptionY + textHeight / 2))
