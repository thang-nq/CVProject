import pygame, pymunk
from Button import CompleteButton, IconButton2
import Constants
import HandTrackingModule as htm
import position
import cv2
# init screen
pygame.init()

# create the screen
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))

from SceneManager import manager

#
# space.gravity = (0, 981)

FPS = Constants.FPS

# TRacking
cap = cv2.VideoCapture(0)
cap.set(3, 1500)
cap.set(4, 810)
detector = htm.handDetector(detectCon=0.65)
position.init()
clear = pygame.Color(0,0,0,0)
isHand = False
isInStopUI = False
controlCanvas = pygame.Surface([1500, 810], pygame.SRCALPHA, 32)
controlCanvas = controlCanvas.convert_alpha()
# caption
pygame.display.set_caption("MilkTea")

gameManager = manager(screen, controlCanvas)




def main():
    global isHand, isInStopUI
    clock = pygame.time.Clock()
    gameManager.gameState = Constants.UI_STATES["main"]
    # ----------------- Game loop --------------------------------
    while True:
        controlCanvas.fill(clear)
        print('Curren pos', position.currentpos)
        gameManager.time_now = pygame.time.get_ticks()
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img, draw=True)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            value = lmList[8][1:]
            position.currentpos = value
            position.state = detector.getHandState()
            isHand = True
        else:
            position.currentpos = (0, 0)
            position.state = 'None'
            isHand = False

        if gameManager.gameState == Constants.UI_STATES["main"]:
            gameManager.getMainUI()
            gameManager.checkMainUI()

        elif gameManager.gameState == Constants.UI_STATES["levelSelect"]:
            gameManager.getLevelSelect()
            if gameManager.gameState > len(Constants.UI_STATES):
                gameManager.loadLevel()
                gameManager.getGame()

        elif gameManager.gameState == Constants.UI_STATES["setting"]:
            gameManager.getSetting()

        elif gameManager.gameState == Constants.UI_STATES["about"]:
            gameManager.getAbout()

        elif gameManager.gameState == Constants.UI_STATES["cleared"]:
            gameManager.getWinPanel()

        elif gameManager.gameState == Constants.UI_STATES["next"]:
            gameManager.getNextLevel()

        elif gameManager.gameState == Constants.UI_STATES["lose"]:
            isInStopUI = True
            gameManager.getLosePanel()

        elif gameManager.gameState >= len(Constants.UI_STATES):
            gameManager.game.number = gameManager.gameState - len(Constants.UI_STATES)
            gameManager.getGame()

        elif gameManager.gameState == Constants.UI_STATES["restart"]:
            gameManager.gameState = len(Constants.UI_STATES) + gameManager.game.number
            gameManager.restartGame()

        if isHand:
            pygame.draw.circle(controlCanvas, "blue", position.currentpos, 5)
            position.previouspos = position.currentpos
            screen.blit(controlCanvas, (0,0))
        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()
