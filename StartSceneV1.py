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
detector = htm.handDetector(detectCon=0.55)
position.init()
isHand = False
# caption
pygame.display.set_caption("MilkTea")

gameManager = manager(screen)




def main():
    global isHand
    clock = pygame.time.Clock()
    gameManager.gameState = Constants.UI_STATES["main"]
    # ----------------- Game loop --------------------------------
    while True:

        #---- Tracking ---#
        gameManager.time_now = pygame.time.get_ticks()
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
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
            gameManager.getLosePanel()

        elif gameManager.gameState >= len(Constants.UI_STATES):
            gameManager.game.number = gameManager.gameState - len(Constants.UI_STATES)
            gameManager.getGame()

        elif gameManager.gameState == Constants.UI_STATES["restart"]:
            gameManager.gameState = len(Constants.UI_STATES) + gameManager.game.number
            gameManager.restartGame()

        #-- Show cursor if hand is in the canvas
        if isHand:
            pygame.draw.circle(screen, "blue", position.currentpos, 5)
            position.previouspos = position.currentpos

        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()
