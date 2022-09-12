import pygame


class CompleteButton():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def checkForInput(self):
        pos = pygame.mouse.get_pos()
        action = False
        # check mouse over and clicked condition

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        else:
            self.clicked = False
        return action

    def draw(self, surface):
        # action = False
        #
        # # get mouse position
        # pos = pygame.mouse.get_pos()
        #
        # # check mouse over and clicked condition
        # if self.rect.collidepoint(pos):
        #     if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        #         self.clicked = True
        #         action = True
        # if pygame.mouse.get_pressed()[0] == 0:
        #     self.clicked = False
        # draw button on the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        # return action


class IconButton():
    def __init__(self, x, y, image, icon, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        iconWidth = icon.get_width()
        iconHeight = icon.get_height()
        self.icon = pygame.transform.scale(icon, (int(iconWidth * scale), int(iconHeight * scale)))
        self.clicked = False

    def checkInput(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            self.clicked = False

        return self.clicked

    def draw(self, surface):
        # draw button on the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        # draw icon on the screen
        width = self.image.get_width()
        height = self.image.get_height()
        iconWidth = self.icon.get_width()
        iconHeight = self.icon.get_height()
        surface.blit(self.icon, (
            self.rect.x + int(width / 2) - int(iconWidth / 2), self.rect.y + int(height / 2) - int(iconHeight / 2)))


class IconButton2():
    def __init__(self, x, y, image, icon, scale, iconScale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        iconWidth = icon.get_width()
        iconHeight = icon.get_height()
        self.icon = pygame.transform.scale(icon, (int(iconWidth * iconScale), int(iconHeight * iconScale)))
        self.clicked = False

    def checkInput(self):
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
        else:
            self.clicked = False
        return self.clicked

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        # draw icon on the screen
        width = self.image.get_width()
        height = self.image.get_height()
        iconWidth = self.icon.get_width()
        iconHeight = self.icon.get_height()
        surface.blit(self.icon, (
            self.rect.x + int(width / 2) - int(iconWidth / 2), self.rect.y + int(height / 2) - int(iconHeight / 2)))
