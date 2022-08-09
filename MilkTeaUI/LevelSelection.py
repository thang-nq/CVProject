import pygame
from Button import IconButton2
# init screen
pygame.init()

# create the screen
screenWidth = 1500
screenHeight = 810
screen = pygame.display.set_mode((screenWidth, screenHeight))
font = pygame.font.SysFont("Ravie", 90)
# caption
pygame.display.set_caption("MilkTea")
# background
menuBackground = pygame.image.load('MilkTeaImages/Background.png')
screenPaddingX = 50
screenPaddingY = 50

# level box
levelBox_img = pygame.image.load('MilkTeaImages/GreenLevelSelection.png')
# challenge box
challengeBox_img = pygame.image.load('MilkTeaImages/ChallengeLevelSelection.png')
# box shared property
boxScale = 0.9
boxX = levelBox_img.get_width() * boxScale
boxY = levelBox_img.get_height() * boxScale
boxX_2 = boxX / 2
boxY_2 = boxY / 2
# text setting
textOffsetY = 5
# milktea
milktea_img = pygame.image.load('MilkTeaImages/MilkTea_Normal_Small.png')
milkteaBackground_img = pygame.image.load('MilkTeaImages/MilkTeaBackground_Normal.png')
chocotea_img = pygame.image.load('MilkTeaImages/MilkTea_Chocolate_Small.png')
chocoteaBackground_img = pygame.image.load('MilkTeaImages/MilkTeaBackground_Chocolate.png')
# compute shared property of milktea
milkteaScale = 1
milkteaSizeX = int(milkteaScale * milktea_img.get_width())
milkteaSizeY = int(milkteaScale * milktea_img.get_height())
milkteaPos = [-10, boxX_2 - milkteaSizeX / 2,10+ boxX - milkteaSizeX]
milkteaPosY = boxY - 20
# return Button
squareButton_img = pygame.image.load('MilkTeaImages/Button_Square.png')
squareWidth = squareButton_img.get_width()
squareHeight = squareButton_img.get_height()
buttonScale = 0.8
# icon
returnicon_img = pygame.image.load('MilkTeaImages/ReturnIcon.png')
returnButtonX = screenPaddingX
returnButtonY = screenPaddingY
iconScale = 0.5

# for normal level
class NormalLevelBox():
    def __init__(self, x, y, text, scale, teaStar):
        width = levelBox_img.get_width()
        height = levelBox_img.get_height()
        self.image = pygame.transform.scale(levelBox_img, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # render text
        self.value = font.render(str(text), True, (255, 255, 255))
        self.milkTea = pygame.transform.scale(milktea_img, (milkteaSizeX, milkteaSizeY))
        self.milkTeaBackground = pygame.transform.scale(milkteaBackground_img, (milkteaSizeX, milkteaSizeY))
        # assign amount fo start
        self.star = teaStar

    def draw(self):
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


# generate
returnButton = IconButton2(returnButtonX, returnButtonY, squareButton_img, returnicon_img, buttonScale, iconScale)
# level_1=NormalLevelBox(400,400,"1",0.6,0)
levels = []
# appenda data
spaceX = 250
spaceY = 250
originX = 160
originY = 200
for i in range(0, 10):
    tempLevel = NormalLevelBox(originX + spaceX * (i % 5), originY, i + 1, boxScale, 1)
    if ((i + 1) % 5 == 0 and i != 0):
        # reset
        originX = 160
        originY += spaceY
    levels.append(tempLevel)
# Game loop
def playLevelSelection():
    running = True
    while running:
        screen.blit(menuBackground, (0, 0))
        returnButton.draw(screen)
        for l in levels:
            l.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        pygame.display.update()
