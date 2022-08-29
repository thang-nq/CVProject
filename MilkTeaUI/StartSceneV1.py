import pygame
from Button import CompleteButton, IconButton2
# import LevelSelection
import Setting
from SceneManager import manager
# import About
import MusicController
import GameUI
import Constants
# Tracking
import HandTrackingModule as htm
import cv2
import config
# init screen
pygame.init()

# create the screen
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
FPS = Constants.FPS
# Tracking
cap = cv2.VideoCapture(0)
cap.set(3, 1500)
cap.set(4, 810)
detector = htm.handDetector(detectCon=0.5)
# caption
pygame.display.set_caption("MilkTea")
gameManager = manager(screen)
handstate = 'None'
isHand = False
config.init()
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
            config.currentpos = value
            config.state = detector.getHandState()
            isHand = True
        else:
            isHand = False
            config.currentpos = (0, 0)


        if gameManager.gameState == 0:
            gameManager.getMainUI()

        elif gameManager.gameState == 1:
            gameManager.getLevelSelect()

        elif gameManager.gameState == 2:
            gameManager.getSetting()

        elif gameManager.gameState == 3:
            gameManager.getAbout()
        if isHand:
            pygame.draw.circle(screen, "blue", config.currentpos, 5)
        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()