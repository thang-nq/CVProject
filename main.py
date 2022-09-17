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
detector = htm.handDetector(detectCon=0.85)
position.init()
isHand = False
gestureMode = 'Menu'
# caption
pygame.display.set_caption("MilkTea")

gameManager = manager(screen)




def main():
    global isHand, gestureMode
    clock = pygame.time.Clock()
    gameManager.gameState = Constants.UI_STATES["main"]
    # ----------------- Game loop --------------------------------
    while True:

        #---- Tracking ---#
        gameManager.time_now = pygame.time.get_ticks()
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img, handL=8, gestureMode=gestureMode)
        if len(lmList) != 0:
            isHand = True
            value = lmList[8][1:]
            position.currentpos = value
            position.state = detector.getHandState()
            # print(position.state)
        else:
            position.currentpos = (0, 0)
            position.state = 'None'
            isHand = False

        if gameManager.gameState == Constants.UI_STATES["main"]:
            gestureMode = 'Menu'
            gameManager.getMainUI()
            gameManager.checkMainUI()

        elif gameManager.gameState == Constants.UI_STATES["levelSelect"]:
            gestureMode = 'Menu'
            gameManager.getLevelSelect()
            if gameManager.gameState > len(Constants.UI_STATES):
                gameManager.loadLevel()
                gestureMode = 'Gameplay'
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

        # cv2.imshow("Tracking", img)
        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()
