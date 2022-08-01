import pygame

# init screen
pygame.init()

# create the screen
screenWidth = 1500
screenHeight = 810
screen = pygame.display.set_mode((screenWidth, screenHeight))
font = pygame.font.Font("freesansbold.ttf", 80)
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
boxScale = 0.6
boxX = levelBox_img.get_width() * boxScale
boxY = levelBox_img.get_height() * boxScale
boxX_2 = boxX / 2
boxY_2 = boxY / 2
# text setting
textOffsetY = 5
# milktea
milktea_img = pygame.image.load('MilkTeaImages/MilkTea_Normal.png')
milkteaBackground_img = pygame.image.load('MilkTeaImages/MilkTeaBackground_Normal.png')
chocotea_img = pygame.image.load('MilkTeaImages/MilkTea_Chocolate.png')
chocoteaBackground_img = pygame.image.load('MilkTeaImages/MilkTeaBackground_Chocolate.png')
# compute shared property of milktea
milkteaScale = 0.15
milkteaSizeX = int(milkteaScale * milktea_img.get_width())
milkteaSizeY = int(milkteaScale * milktea_img.get_height())
milkteaPos = [0, boxX_2 - milkteaSizeX / 2, boxX - milkteaSizeX]
milkteaPosY = boxY - 20
# return Button
squareButton_img = pygame.image.load('MilkTeaImages/Button_Square.png')
squareWidth = squareButton_img.get_width()
squareHeight = squareButton_img.get_height()
buttonScale = 0.4
# icon
returnicon_img = pygame.image.load('MilkTeaImages/ReturnIcon.png')
returnButtonX = screenPaddingX
returnButtonY = screenPaddingY
iconScale = 0.3


# used for return button
class IconButton():
    def __init__(self, x, y, image, icon, scale, iconScale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        iconWidth = icon.get_width()
        iconHeight = icon.get_height()
        self.icon = pygame.transform.scale(icon, (int(iconWidth * iconScale), int(iconHeight * iconScale)))

    def draw(self):
        # draw button on the screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # draw icon on the screen
        width = self.image.get_width()
        height = self.image.get_height()
        iconWidth = self.icon.get_width()
        iconHeight = self.icon.get_height()
        screen.blit(self.icon, (
        self.rect.x + int(width / 2) - int(iconWidth / 2), self.rect.y + int(height / 2) - int(iconHeight / 2)))


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
returnButton = IconButton(returnButtonX, returnButtonY, squareButton_img, returnicon_img, buttonScale, iconScale)
# level_1=NormalLevelBox(400,400,"1",0.6,0)
levels = []
# appenda data
spaceX = 250
spaceY = 250
originX = 200
originY = 200
for i in range(0, 10):
    tempLevel = NormalLevelBox(originX + spaceX * (i % 5), originY, i + 1, boxScale, 1)
    if ((i + 1) % 5 == 0 and i != 0):
        # reset
        originX = 200
        originY += spaceY
    levels.append(tempLevel)
# Game loop
running = True
while running:
    screen.blit(menuBackground, (0, 0))
    returnButton.draw()
    for l in levels:
        l.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
