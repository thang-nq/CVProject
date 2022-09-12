import pygame, pymunk
from Button import CompleteButton, IconButton2
import Constants

# init screen
pygame.init()

# create the screen
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))

from SceneManager import manager

#
# space.gravity = (0, 981)

FPS = Constants.FPS

# caption
pygame.display.set_caption("MilkTea")

gameManager = manager(screen)


def main():
    clock = pygame.time.Clock()
    gameManager.gameState = Constants.UI_STATES["main"]
    # ----------------- Game loop --------------------------------
    while True:
        gameManager.time_now = pygame.time.get_ticks()
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

        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()
