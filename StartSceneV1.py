
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
isHand = False
# caption
pygame.display.set_caption("MilkTea")

gameManager = manager(screen )



def main():
    global isHand
    clock = pygame.time.Clock()

    # ----------------- Game loop --------------------------------
    while True:
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
            isHand = False

        if gameManager.gameState == Constants.UI_STATES["main"]:
            gameManager.getMainUI()
            gameManager.checkMainUI()

        elif gameManager.gameState == Constants.UI_STATES["levelSelect"]:
            gameManager.getLevelSelect()

        elif gameManager.gameState == Constants.UI_STATES["setting"]:
            gameManager.getSetting()

        elif gameManager.gameState == Constants.UI_STATES["about"]:
            gameManager.getAbout()
            gameManager.getGame()

        elif gameManager.gameState >= len(Constants.UI_STATES):
            gameManager.getGame()

        elif gameManager.gameState == Constants.UI_STATES["restart"]:
            gameManager.gameState = len(Constants.UI_STATES) + gameManager.game.number
            gameManager.restartGame()
        if isHand:
            pygame.draw.circle(screen, "blue", position.currentpos, 5)
        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()
