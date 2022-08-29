import pygame
from Button import CompleteButton, IconButton2
# import LevelSelection
import Setting
from SceneManager import manager
from GameUI import inGameUI
# import About
import MusicController
import GameUI
import Constants

# init screen
pygame.init()

# create the screen
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
FPS = Constants.FPS

# caption
pygame.display.set_caption("MilkTea")

gameManager = manager(screen)
inGameUI = inGameUI(screen)
def main():
    clock = pygame.time.Clock()

    # ----------------- Game loop --------------------------------
    while True:
        gameManager.time_now = pygame.time.get_ticks()

        inGameUI.draw()
        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()