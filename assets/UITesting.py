import pygame
from Button import CompleteButton, IconButton2
# import LevelSelection
import Setting
from SceneManager import manager
from GameUI import inGameUI
from GameUI import wonPanelUI,losePanelUI
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
wonPanel = wonPanelUI(screen)
losePanel = losePanelUI(screen)
menuBackground = pygame.image.load('MilkTeaImages/Background.png')
def main():
    clock = pygame.time.Clock()
    running = True
    # ----------------- Game loop --------------------------------
    while running:
        gameManager.time_now = pygame.time.get_ticks()
        screen.blit(menuBackground, (0, 0))
        #inGameUI.draw()
        #wonPanel.draw()
        losePanel.draw()
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()
pygame.quit()