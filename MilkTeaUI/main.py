import pygame
from Button import CompleteButton, IconButton2
import LevelSelection
import Setting
import SceneManager
import About
import MusicController
# init screen
pygame.init()

# create the screen
screenWidth = 1500
screenHeight = 810
screen = pygame.display.set_mode((screenWidth, screenHeight))

# caption
pygame.display.set_caption("MilkTea")


# create the screen
screenWidth = 1500
screenHeight = 810
#property
menuBackground = pygame.image.load('MilkTeaImages/IntroBackground.png')
screenPaddingX = 50
screenPaddingY = 50
title = pygame.image.load('MilkTeaImages/IntroTitle.png')
titleX=screenWidth/2-title.get_width()/2
titleY= 200-title.get_height()/2
# play button
playButton_img = pygame.image.load('MilkTeaImages/PlayButton.png')
# compute play button property
playButtonScale = 0.6
playButtonX = screenWidth / 2 - int(playButton_img.get_width() / 2 * playButtonScale)
playButtonY = screenHeight / 2 - int(playButton_img.get_height() / 2 * playButtonScale)
# button
squareButton_img = pygame.image.load('MilkTeaImages/Button_Square.png')
squareWidth = squareButton_img.get_width()
squareHeight = squareButton_img.get_height()
buttonScale = 1
iconButtonScale = 0.5
# setting
settingIcon_img = pygame.image.load('MilkTeaImages/SettingIcon.png')
# compute setting button property
settingButtonX = screenPaddingX
settingButtonY = screenHeight - screenPaddingY - int(squareWidth * buttonScale)
# about button
aboutIcon_img = pygame.image.load('MilkTeaImages/AboutIcon.png')
# compute setting button property
aboutButtonX = settingButtonX + 150
aboutButtonY = settingButtonY
# about property
exitIcon_img = pygame.image.load("MilkTeaImages/ExitIcon.png")
# exit property
exitButtonX = screenWidth - screenPaddingX - exitIcon_img.get_width() / 2
exitButtonY = settingButtonY
play_Button = CompleteButton(playButtonX, playButtonY, playButton_img, playButtonScale)
settingButton = IconButton2(settingButtonX, settingButtonY, squareButton_img, settingIcon_img, buttonScale,iconButtonScale)
aboutButton = IconButton2(aboutButtonX, aboutButtonY, squareButton_img, aboutIcon_img, buttonScale,iconButtonScale)
exitButton = IconButton2(exitButtonX, exitButtonY, squareButton_img, exitIcon_img, buttonScale,iconButtonScale)
def drawMainMenu():
    screen.blit(menuBackground, (0, 0))
    play_Button.draw(screen)
    settingButton.draw(screen)
    aboutButton.draw(screen)
    exitButton.draw(screen)
def levelSelection():

    LevelSelection.playLevelSelection()
    #level Selection must overlay other

# Game loop-------------------------------------------------------------------------------------------
running = True
while running:
    screen.blit(menuBackground, (0, 0))
    screen.blit(title,(titleX,titleY))
    if play_Button.draw(screen) and SceneManager.CheckMain():
        levelSelection()
    if settingButton.draw(screen) and SceneManager.CheckMain():
        SceneManager.SetState(SceneManager.settingState)
    if aboutButton.draw(screen) and SceneManager.CheckMain():
        SceneManager.SetState(SceneManager.aboutState)
    if exitButton.draw(screen):
        running = False
        continue # will ignore what come next and quit directuly
    #display submenu-------------------
    if(SceneManager.CheckSetting()):
        Setting.run(screen)
    if(SceneManager.CheckAbout()):
        About.run(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
