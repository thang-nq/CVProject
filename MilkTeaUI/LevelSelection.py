import pygame
from Button import IconButton2
from LevelBox import NormalLevelBox,ChocolateLevelBox
import SceneManager
import prototype_game2_seg
# init screen
pygame.init()

# create the screen
screenWidth = 1500
screenHeight = 810
screen = pygame.display.set_mode((screenWidth, screenHeight))
# caption
pygame.display.set_caption("MilkTea")
# background
menuBackground = pygame.image.load('MilkTeaImages/Background.png')
screenPaddingX = 50
screenPaddingY = 50

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

# generate
returnButton = IconButton2(returnButtonX, returnButtonY, squareButton_img, returnicon_img, buttonScale, iconScale)
# level_1=NormalLevelBox(400,400,"1",0.6,0)
levels = []
# appenda data'
boxScale = 0.9
spaceX = 250
spaceY = 250
originX = 160
originY = 200
chocolateOffset =0 # chocolate box not counted as normal and they don't use number
for i in range(0, 10):
    if ((i + 1) % 5 == 0):
        #chocolate box
        tempLevel = ChocolateLevelBox(originX + spaceX * (i % 5), originY, boxScale, 1)
        levels.append(tempLevel)
        chocolateOffset += 1
        # reset
        originX = 160
        originY += spaceY
    else :
        tempLevel = NormalLevelBox(originX + spaceX * (i % 5), originY, i + 1 - chocolateOffset, boxScale, 1)
        levels.append(tempLevel)
# Game loop
def playLevelSelection():
    running = True
    while running:
        screen.blit(menuBackground, (0, 0))
        if returnButton.draw(screen):
            running = False
        for l in levels:
            l.draw(screen)
            if(SceneManager.buttonPressed):
                print("waiting to restore input:")
            if(l.checkForInput() and not SceneManager.buttonPressed):
                #run the function that lead to a game scene
                prototype_game2_seg.game()
                print("clicked a level")
                pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        pygame.display.update()
