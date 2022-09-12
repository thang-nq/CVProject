import pygame

# property-----------------------------------------------------------------------------------------------------
pygame.init()
font = pygame.font.SysFont("Ravie", 90)

# level box
levelBox_img = pygame.image.load('assets/MilkTeaImages/GreenLevelSelection.png')


# challenge box
challengeBox_img = pygame.image.load('assets/MilkTeaImages/ChallengeLevelSelection.png')


# box shared property
boxScale = 0.9
boxX = levelBox_img.get_width() * boxScale
boxY = levelBox_img.get_height() * boxScale
boxX_2 = boxX / 2
boxY_2 = boxY / 2


# text setting
textOffsetY = 5


# milktea
milktea_img = pygame.image.load('assets/MilkTeaImages/MilkTea_Normal_Small.png')
milkteaBackground_img = pygame.image.load('assets/MilkTeaImages/MilkTeaBackground_Normal.png')
chocotea_img = pygame.image.load('assets/MilkTeaImages/MilkTea_Chocolate_Small.png')
chocoteaBackground_img = pygame.image.load('assets/MilkTeaImages/MilkTeaBackground_Chocolate.png')


# compute shared property of milktea
milkteaScale = 1
milkteaSizeX = int(milkteaScale * milktea_img.get_width())
milkteaSizeY = int(milkteaScale * milktea_img.get_height())
milkteaPos = [-10, boxX_2 - milkteaSizeX / 2, 10 + boxX - milkteaSizeX]
milkteaPosY = boxY - 20


# for normal level
class NormalLevelBox():
    def __init__(self, x, y, text, scale, teaStar, level):
        width = levelBox_img.get_width()
        height = levelBox_img.get_height()
        self.level = level
        self.image = pygame.transform.scale(levelBox_img, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # render text
        self.value = font.render(str(text), True, (255, 255, 255))
        self.milkTea = pygame.transform.scale(milktea_img, (milkteaSizeX, milkteaSizeY))
        self.milkTeaBackground = pygame.transform.scale(milkteaBackground_img, (milkteaSizeX, milkteaSizeY))
        # assign amount fo start
        self.star = teaStar
        self.clicked = False

    def checkForInput(self):
        pos = pygame.mouse.get_pos()
        action = False
        # check mouse over and clicked condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

    def draw(self, screen):
        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # draw text value
        textWidth = self.value.get_width()
        textHeight = self.value.get_height()
        screen.blit(self.value,
                    (self.rect.x + boxX_2 - textWidth / 2, self.rect.y + boxY_2 - textHeight / 2 + textOffsetY))
        # place milktea at the bottom
        for i in range(0, 3):
            if (i < self.star):
                screen.blit(self.milkTea, (self.rect.x + milkteaPos[i], self.rect.y + milkteaPosY))
            else:
                screen.blit(self.milkTeaBackground, (self.rect.x + milkteaPos[i], self.rect.y + milkteaPosY))


class ChocolateLevelBox():
    def __init__(self, x, y, scale, teaStar, level):
        width = levelBox_img.get_width()
        height = levelBox_img.get_height()
        self.level = level
        self.image = pygame.transform.scale(challengeBox_img, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # render text
        self.milkTea = pygame.transform.scale(chocotea_img, (milkteaSizeX, milkteaSizeY))
        self.milkTeaBackground = pygame.transform.scale(chocoteaBackground_img, (milkteaSizeX, milkteaSizeY))
        # assign amount fo start
        self.star = teaStar
        self.clicked = False

    def checkForInput(self):
        pos = pygame.mouse.get_pos()
        action = False
        # check mouse over and clicked condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

    def draw(self, screen):
        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # place milktea at the bottom
        for i in range(0, 3):
            if (i < self.star):
                screen.blit(self.milkTea, (self.rect.x + milkteaPos[i], self.rect.y + milkteaPosY))
            else:
                screen.blit(self.milkTeaBackground, (self.rect.x + milkteaPos[i], self.rect.y + milkteaPosY))
