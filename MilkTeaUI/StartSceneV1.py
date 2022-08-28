import pygame
from Button import CompleteButton, IconButton2
import LevelSelection
import Setting
import SceneManager
import About
import MusicController
import GameUI

# init screen
pygame.init()

# create the screen
screenWidth = 1500
screenHeight = 810
screen = pygame.display.set_mode((screenWidth, screenHeight))

# caption
pygame.display.set_caption("MilkTea")
UI_STATES = {"main": 0, "levelSelect": 1, "setting": 2, "about": 3, "game": 4}
gameState = UI_STATES["main"]


def main():
    # ----------------- Game loop --------------------------------
    global gameState
    while True:
        if gameState == 0:
            mainUI = GameUI.mainUI(screen)
            mainUI.draw_UI(gameState)
            print(gameState)
        elif gameState == 1:
            selectUI = GameUI.selectorUI(screen)
            print(selectUI.draw_UI())
        # print(gameState)
        pygame.display.update()


main()
pygame.quit()
