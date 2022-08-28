import pygame
from Button import CompleteButton, IconButton2
from LevelBox import NormalLevelBox,ChocolateLevelBox
import LevelSelection
import Setting
import SceneManager
import About
import MusicController

WIDTH = 1500
HEIGHT = 810
UI_STATES = {"main": 0, "levelSelect": 1, "setting": 2, "about": 3, "game": 4}
# ---------------------------------- BACKGROUND IMG ----------------------------------
menuBackground = pygame.image.load('MilkTeaImages/IntroBackground.png')
screenPaddingX = 50
screenPaddingY = 50

# ---------------------------------- Common button ----------------------------------
squareButton_img = pygame.image.load('MilkTeaImages/Button_Square.png')
squareWidth = squareButton_img.get_width()
squareHeight = squareButton_img.get_height()


# ---------------------------------- END ---------------------------------------------

class mainUI:
    def __init__(self, screen):

        self.screen = screen
        self.running = True

        # Main property
        # ---------------------------------- End ----------------------------------------------

        # ---------------------------------- TITLE IMG ----------------------------------------------
        self.title = pygame.image.load('MilkTeaImages/IntroTitle.png')
        self.titleX = WIDTH / 2 - self.title.get_width() / 2
        self.titleY = 200 - self.title.get_height() / 2

        # ---------------------------------- End ----------------------------------------------

        # Play button
        self.playButton_img = pygame.image.load('MilkTeaImages/PlayButton.png')
        self.playButtonScale = 0.6
        self.playButtonX = WIDTH / 2 - int(self.playButton_img.get_width() / 2 * self.playButtonScale)
        self.playButtonY = HEIGHT / 2 - int(self.playButton_img.get_height() / 2 * self.playButtonScale)

        # Common button
        self.squareButton_img = squareButton_img
        self.squareWidth = self.squareButton_img.get_width()
        self.squareHeight = self.squareButton_img.get_height()

        self.buttonScale = 1
        self.iconButtonScale = 0.5

        # Setting button
        self.settingIcon_img = pygame.image.load('MilkTeaImages/SettingIcon.png')
        self.settingButtonX = screenPaddingX
        self.settingButtonY = HEIGHT - screenPaddingY - int(self.squareWidth * self.buttonScale)

        # About button
        self.aboutIcon_img = pygame.image.load('MilkTeaImages/AboutIcon.png')
        self.aboutButtonX = self.settingButtonX + 150
        self.aboutButtonY = self.settingButtonY

        # about property
        self.exitIcon_img = pygame.image.load("MilkTeaImages/ExitIcon.png")

        # exit property
        self.exitButtonX = WIDTH - screenPaddingX - self.exitIcon_img.get_width() / 2
        self.exitButtonY = self.settingButtonY
        self.play_Button = CompleteButton(self.playButtonX, self.playButtonY, self.playButton_img, self.playButtonScale)
        self.settingButton = IconButton2(self.settingButtonX, self.settingButtonY, self.squareButton_img,
                                         self.settingIcon_img, self.buttonScale,
                                         self.iconButtonScale)
        self.aboutButton = IconButton2(self.aboutButtonX, self.aboutButtonY, self.squareButton_img, self.aboutIcon_img,
                                       self.buttonScale,
                                       self.iconButtonScale)
        self.exitButton = IconButton2(self.exitButtonX, self.exitButtonY, self.squareButton_img, self.exitIcon_img,
                                      self.buttonScale, self.iconButtonScale)
        self.sceneManager = SceneManager.manager(self.screen)

    def draw_UI(self,gameState):


        self.screen.blit(menuBackground, (0, 0))

        if self.play_Button.draw(self.screen):
            self.sceneManager.SetOnButton()
            # LevelSelection.playLevelSelection()
            # levelSelector = selectorUI(self.screen).draw_UI()
            return "levelSelect"
        if self.settingButton.draw(self.screen):
            self.sceneManager.SetState(self.sceneManager.settingState)
            # return "setting"
        if self.aboutButton.draw(self.screen):
            self.sceneManager.SetState(self.sceneManager.aboutState)
            print(self.sceneManager.subSetting)
            return "about"
        if self.exitButton.draw(self.screen):
            self.running = False
            pygame.quit()

        # -------------------Display submenu-------------------
        # if self.sceneManager.CheckSetting():
        #     Setting.run(self.screen)
        # if self.sceneManager.CheckAbout():
        #     About.run(self.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        return "main"


class selectorUI:
    def __init__(self, screen):
        self.screen = screen
        # return Button
        self.squareButton_img = squareButton_img
        self.squareWidth = squareButton_img.get_width()
        self.squareHeight = squareButton_img.get_height()
        self.buttonScale = 0.8

        # icon
        self.returnIcon = pygame.image.load('MilkTeaImages/ReturnIcon.png')
        self.returnButtonX = screenPaddingX
        self.returnButtonY = screenPaddingY
        self.iconScale = 0.5

        # generate
        self.returnButton = IconButton2(self.returnButtonX, self.returnButtonY, self.squareButton_img, self.returnIcon,
                                        self.buttonScale,
                                        self.iconScale)

        # level_1=NormalLevelBox(400,400,"1",0.6,0)
        self.levels = []

        # append data
        self.boxScale = 0.9
        self.spaceX = 250
        self.spaceY = 250
        self.originX = 160
        self.originY = 200
        self.chocolateOffset = 0  # chocolate box not counted as normal and they don't use number

        for i in range(0, 10):
            if ((i + 1) % 5 == 0):
                # chocolate box
                tempLevel = ChocolateLevelBox(self.originX + self.spaceX * (i % 5), self.originY, self.boxScale, 0, i)
                self.levels.append(tempLevel)
                self.chocolateOffset += 1
                # reset
                self.originX = 160
                self.originY += self.spaceY
            else:
                tempLevel = NormalLevelBox(self.originX + self.spaceX * (i % 5), self.originY,
                                           i + 1 - self.chocolateOffset, self.boxScale, 0, i)
                self.levels.append(tempLevel)

    def draw_UI(self):
        self.screen.blit(menuBackground, (0, 0))
        if self.returnButton.draw(self.screen):
            running = False
        for l in self.levels:
            l.draw(self.screen)
            if l.checkForInput() and not SceneManager.buttonPressed:
                return l.level

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
