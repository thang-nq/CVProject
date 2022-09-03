import pygame
from Button import CompleteButton, IconButton2
from LevelBox import NormalLevelBox, ChocolateLevelBox
from Panel import GamePanel, AboutUsCompBox, SettingCompBox
import MusicController
import Constants

WIDTH = Constants.WIDTH
HEIGHT = Constants.HEIGHT
UI_STATES = Constants.UI_STATES

# ---------------------------------- BACKGROUND IMG ----------------------------------
menuBackground = pygame.image.load('MilkTeaImages/IntroBackground.png')
screenPaddingX = 50
screenPaddingY = 50

# ---------------------------------- Common button ----------------------------------
squareButton_img = pygame.image.load('MilkTeaImages/Button_Square.png')
squareWidth = squareButton_img.get_width()
squareHeight = squareButton_img.get_height()

# ---------------------------------- END ---------------------------------------------
# ---------------------------------- Cancel button ---------------------------------------------
cancel_img = pygame.image.load('MilkTeaImages/QuitButton.png')


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

    def draw_UI(self):
        self.screen.blit(menuBackground, (0, 0))

        if self.play_Button.draw(self.screen):
            # self.sceneManager.SetOnButton()
            # LevelSelection.playLevelSelection()
            # levelSelector = selectorUI(self.screen).draw_UI()
            return UI_STATES["levelSelect"]
        if self.settingButton.draw(self.screen):
            # self.sceneManager.SetState(self.sceneManager.settingState)
            return UI_STATES["setting"]
        if self.aboutButton.draw(self.screen):
            # self.sceneManager.SetState(self.sceneManager.aboutState)
            # print(self.sceneManager.subSetting)
            return UI_STATES["about"]

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
        return UI_STATES["main"]


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

    def draw_UI(self, time_now, next_allowed):
        self.screen.blit(menuBackground, (0, 0))
        if self.returnButton.draw(self.screen):
            return UI_STATES["main"]

        for l in self.levels:
            l.draw(self.screen)
            # and not SceneManager.buttonPressed
            # if l.checkForInput():
            #     return l.level
        if (time_now > next_allowed):
            for l in self.levels:
                if l.checkForInput():
                    return len(Constants.UI_STATES) + l.level
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        return UI_STATES["levelSelect"]


class aboutUI:
    def __init__(self, screen):
        self.screen = screen

        # -------------- Overlay color ----------------
        self.overlay = pygame.Surface((WIDTH, HEIGHT))
        self.overlay.set_alpha(80)
        self.overlay.fill((0, 0, 0))

        # -------------- Overlay Panel ----------------
        self.aboutPanel_img = pygame.image.load('MilkTeaImages/AboutUs.png')
        self.aboutPanel = GamePanel(WIDTH / 2, HEIGHT / 2, self.aboutPanel_img, 1)

        # ------------------------ Cancel Panel ------------------------
        self.cancel_img = cancel_img
        # cancel property
        self.cancelX = WIDTH / 2 + 500
        self.cancelY = HEIGHT / 2 - 300
        self.cancelButton = CompleteButton(self.cancelX, self.cancelY, self.cancel_img, 0.8)
        # --------------------------- END -------------------------------

        # ------------------------------- AVATARS -------------------------------
        self.avatarSample1 = pygame.image.load('MilkTeaImages/Avatar_Beereel.png')
        self.avatarSample2 = pygame.image.load('MilkTeaImages/Avatar_Princess.png')
        self.avatarSample3 = pygame.image.load('MilkTeaImages/Avatar_Tinia.png')
        self.avatarSample4 = pygame.image.load('MilkTeaImages/Avatar_Scyn.png')

        self.khoaX = WIDTH / 2 - 250
        self.khoaY = HEIGHT / 2 - 50
        self.khoa_Box = AboutUsCompBox(self.khoaX, self.khoaY, self.avatarSample1, "Tran Nguyen Anh Khoa", "s3863956",
                                       "I worked on the aesthetic, UX/ UI of the game ", 1)

        self.khaiX = WIDTH / 2 - 200
        self.khaiY = HEIGHT / 2 + 100
        self.khai_Box = AboutUsCompBox(self.khaiX, self.khaiY, self.avatarSample2, "Khai", "s3863956",
                                       "I worked on the physics simulation",
                                       1)

        self.thangX = WIDTH / 2 - 70
        self.thangY = HEIGHT / 2 + 250
        self.thang_Box = AboutUsCompBox(self.thangX, self.thangY, self.avatarSample3, "Thang", "s3863956",
                                        "I worked in the computer vision system", 1)

        self.ducX = WIDTH / 2 + 250
        self.ducY = HEIGHT / 2 - 150
        self.duc_Box = AboutUsCompBox(self.ducX, self.ducY, self.avatarSample4, "Duc", "s3863956",
                                      "I worked in the computer vision system",
                                      1)

        # ----------------------------------- END ----------------------------------------

    def draw_UI(self):
        self.screen.blit(self.overlay, (0, 0))
        self.aboutPanel.draw(self.screen)
        self.khoa_Box.draw(self.screen)
        self.khai_Box.draw(self.screen)
        self.thang_Box.draw(self.screen)
        self.duc_Box.draw(self.screen)
        if (self.cancelButton.draw(self.screen)):
            # SceneManager.SetState(SceneManager.mainState)
            return UI_STATES["main"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        return UI_STATES["about"]


class settingUI:
    def __init__(self, screen):
        self.screen = screen
        # -------------- Overlay color ----------------
        self.overlay = pygame.Surface((WIDTH, HEIGHT))
        self.overlay.set_alpha(80)
        self.overlay.fill((0, 0, 0))
        # -------------- Overlay Panel ----------------
        self.settingPanel_img = pygame.image.load('MilkTeaImages/Setting.png')
        self.settingPanel = GamePanel(WIDTH / 2, HEIGHT / 2, self.settingPanel_img, 1)

        # -------------- Cancel symbol ----------------
        self.cancel_img = cancel_img
        # cancel property
        self.cancelX = WIDTH / 2 + 200
        self.cancelY = HEIGHT / 2 - 240
        self.cancelButton = CompleteButton(self.cancelX, self.cancelY, self.cancel_img, 0.8)
        # -------------- Music icon ----------------
        self.musicIcon_img = pygame.image.load('MilkTeaImages/MusicIcon.png')
        self.musicSettingX = WIDTH / 2
        self.musicSettingY = HEIGHT / 2 - 50
        self.musicSetting = SettingCompBox(self.musicSettingX, self.musicSettingY, self.musicIcon_img, "Music", 1)

    def draw_UI(self):
        self.screen.blit(self.overlay, (0, 0))
        self.settingPanel.draw(self.screen)
        if self.musicSetting.draw(self.screen):
            MusicController.PlayMusic()
        else:
            MusicController.StopMusic()
        if self.cancelButton.draw(self.screen):
            return UI_STATES["main"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        return UI_STATES["setting"]


class inGameUI:
    def __init__(self, screen):
        self.screen = screen
        buttonScale = 0.6
        iconScale = 0.3
        # ------------------------ Restart Button ------------------------
        restartIcon = pygame.image.load('MilkTeaImages/RestartIcon.png')
        restartPosX = Constants.WIDTH - screenPaddingX - restartIcon.get_width() / 2
        restartPosY = screenPaddingY
        self.restartButton = IconButton2(restartPosX, restartPosY, squareButton_img, restartIcon, buttonScale,
                                         iconScale)

        # ------------------------ Return Button ------------------------
        returnIcon = pygame.image.load('MilkTeaImages/ReturnIcon.png')
        returnPosX = screenPaddingX
        returnPosY = screenPaddingY
        self.returnButton = IconButton2(returnPosX, returnPosY, squareButton_img, returnIcon, buttonScale, iconScale)

    def draw(self):
        if self.returnButton.draw(self.screen):
            return UI_STATES["levelSelect"]
        if self.restartButton.draw(self.screen):
            return UI_STATES["pause"]
        return UI_STATES["game"]