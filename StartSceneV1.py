import pygame, pymunk
from Button import CompleteButton, IconButton2
from SceneManager import manager
import MusicController
import GameUI
import Constants
import HandTrackingModule as htm
# init screen
pygame.init()

# create the screen
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
# space = pymunk.Space()
#
# space.gravity = (0, 981)

FPS = Constants.FPS

# TRacking

# caption
pygame.display.set_caption("MilkTea")

gameManager = manager(screen)



def main():
    clock = pygame.time.Clock()

    # ----------------- Game loop --------------------------------
    while True:
        gameManager.time_now = pygame.time.get_ticks()

        if gameManager.gameState == 0:
            gameManager.getMainUI()

        elif gameManager.gameState == 1:
            gameManager.getLevelSelect()

        elif gameManager.gameState == 2:
            gameManager.getSetting()

        elif gameManager.gameState == 3:
            # gameManager.getAbout()
            gameManager.getGame()

        elif gameManager.gameState >= len(Constants.UI_STATES):
            gameManager.getGame()

        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()