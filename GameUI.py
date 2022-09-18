from ast import Constant
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
menuBackground = pygame.image.load('assets/MilkTeaImages/IntroBackground.png').convert_alpha()
screenPaddingX = 50
screenPaddingY = 50

# ---------------------------------- Common button ----------------------------------
squareButton_img = pygame.image.load('assets/MilkTeaImages/Button_Square.png').convert_alpha()
squareWidth = squareButton_img.get_width()
squareHeight = squareButton_img.get_height()

# ---------------------------------- END ---------------------------------------------
# ---------------------------------- Cancel button ---------------------------------------------
cancel_img = pygame.image.load('assets/MilkTeaImages/QuitButton.png').convert_alpha()


class mainUI:
    def __init__(self, screen):

        self.screen = screen

        # Main property
        # ---------------------------------- End ----------------------------------------------

        # ---------------------------------- TITLE IMG ----------------------------------------------
        title = pygame.image.load('assets/MilkTeaImages/IntroTitle.png').convert_alpha()
        titleX = WIDTH / 2 - title.get_width() / 2
        titleY = 200 - title.get_height() / 2

        # ---------------------------------- End ----------------------------------------------

        # Play button
        playButton_img = pygame.image.load('assets/MilkTeaImages/PlayButton.png').convert_alpha()
        playButtonScale = 0.6
        playButtonX = WIDTH / 2 - int(playButton_img.get_width() / 2 * playButtonScale)
        playButtonY = HEIGHT / 2 - int(playButton_img.get_height() / 2 * playButtonScale)
        self.play_Button = CompleteButton(playButtonX, playButtonY, playButton_img, playButtonScale)

        # Common button
        self.squareButton_img = squareButton_img
        squareWidth = squareButton_img.get_width()
        squareHeight = squareButton_img.get_height()

        buttonScale = 1
        iconButtonScale = 0.5

        # Setting button
        settingIcon_img = pygame.image.load('assets/MilkTeaImages/SettingIcon.png').convert_alpha()
        settingButtonX = screenPaddingX
        settingButtonY = HEIGHT - screenPaddingY - int(squareWidth * buttonScale)
        self.settingButton = IconButton2(settingButtonX, settingButtonY, squareButton_img,
                                         settingIcon_img, buttonScale,
                                         iconButtonScale)
        # About button
        aboutIcon_img = pygame.image.load('assets/MilkTeaImages/AboutIcon.png').convert_alpha()
        aboutButtonX = settingButtonX + 150
        aboutButtonY = settingButtonY

        self.aboutButton = IconButton2(aboutButtonX, aboutButtonY, squareButton_img, aboutIcon_img,
                                       buttonScale,
                                       iconButtonScale)
        # about property
        exitIcon_img = pygame.image.load("assets/MilkTeaImages/ExitIcon.png").convert_alpha()

        # exit property
        exitButtonX = WIDTH - screenPaddingX - exitIcon_img.get_width() / 2
        exitButtonY = settingButtonY

        self.exitButton = IconButton2(exitButtonX, exitButtonY, squareButton_img, exitIcon_img,
                                      buttonScale, iconButtonScale)

    def checkInput(self):
        if self.play_Button.checkForInput():
            return UI_STATES["levelSelect"]
        if self.settingButton.checkInput():
            return UI_STATES["setting"]
        if self.aboutButton.checkInput():
            return UI_STATES["about"]
        if self.exitButton.checkInput():
            pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # print("setting")
        return UI_STATES["main"]

    def draw_UI(self):
        self.screen.blit(menuBackground, (0, 0))

        self.play_Button.draw(self.screen)
        self.settingButton.draw(self.screen)
        self.aboutButton.draw(self.screen)
        self.exitButton.draw(self.screen)


class selectorUI:
    def __init__(self, screen):
        self.screen = screen
        # return Button
        self.squareButton_img = squareButton_img
        buttonScale = 0.8

        # icon
        returnIcon = pygame.image.load('assets/MilkTeaImages/ReturnIcon.png').convert_alpha()
        returnButtonX = screenPaddingX
        returnButtonY = screenPaddingY
        iconScale = 0.5

        # generate
        self.returnButton = IconButton2(returnButtonX, returnButtonY, self.squareButton_img, returnIcon,
                                        buttonScale,
                                        iconScale)

        # level_1=NormalLevelBox(400,400,"1",0.6,0)
        self.levels = []
        self.score = Constants.LEVELS_SCORE
        # append data
        boxScale = 0.9
        spaceX = 250
        spaceY = 250
        originX = 160
        originY = 200
        chocolateOffset = 0  # chocolate box not counted as normal and they don't use number

        for i in range(0, 10):
            if ((i + 1) % 5 == 0):
                # chocolate box
                tempLevel = ChocolateLevelBox(originX + spaceX * (i % 5), originY, boxScale, self.score[i], i + 1)
                self.levels.append(tempLevel)
                chocolateOffset += 1
                # reset
                originX = 160
                originY += spaceY
            else:
                tempLevel = NormalLevelBox(originX + spaceX * (i % 5), originY,
                                           i + 1 - chocolateOffset, boxScale, self.score[i], i + 1)
                self.levels.append(tempLevel)

    def checkInput(self, time_now, next_allowed):
        if time_now > next_allowed:
            if self.returnButton.checkInput():
                return UI_STATES["main"]
            for l in self.levels:
                if l.checkForInput():
                    return len(Constants.UI_STATES) + l.level
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        return UI_STATES["levelSelect"]

    def draw_UI(self):
        self.screen.blit(menuBackground, (0, 0))
        self.returnButton.draw(self.screen)
        for l in self.levels:
            l.draw(self.screen)

    def setStar(self,num):
        self.levels[num].star = self.score[num]

class aboutUI:
    def __init__(self, screen):
        self.screen = screen

        # -------------- Overlay color ----------------
        self.overlay = pygame.Surface((WIDTH, HEIGHT))
        self.overlay.set_alpha(80)
        self.overlay.fill((0, 0, 0))

        # -------------- Overlay Panel ----------------
        aboutPanel_img = pygame.image.load('assets/MilkTeaImages/AboutUs.png').convert_alpha()
        self.aboutPanel = GamePanel(WIDTH / 2, HEIGHT / 2, aboutPanel_img, 1)

        # ------------------------ Cancel Panel ------------------------
        self.cancel_img = cancel_img
        # cancel property
        cancelX = WIDTH / 2 + 500
        cancelY = HEIGHT / 2 - 300
        self.cancelButton = CompleteButton(cancelX, cancelY, self.cancel_img, 0.8)
        # --------------------------- END -------------------------------

        # ------------------------------- AVATARS -------------------------------
        avatarSample1 = pygame.image.load('assets/TeamProfile/Khoa.png').convert_alpha()
        avatarSample2 = pygame.image.load('assets/TeamProfile/Khai.png').convert_alpha()
        avatarSample3 = pygame.image.load('assets/TeamProfile/Thang.png').convert_alpha()
        avatarSample4 = pygame.image.load('assets/TeamProfile/Duc.png').convert_alpha()

        khoaX = WIDTH / 2 - 250
        khoaY = HEIGHT / 2 - 50
        self.khoa_Box = AboutUsCompBox(khoaX, khoaY, avatarSample1, "Tran Nguyen Anh Khoa", "s3863956",
                                       "I love game development", 1)

        khaiX = WIDTH / 2 - 200
        khaiY = HEIGHT / 2 + 100
        self.khai_Box = AboutUsCompBox(khaiX, khaiY, avatarSample2, "Ngo Quang Khai", "s3836387",
                                       "I am very passionate about computer vision technology. ",
                                       1)

        thangX = WIDTH / 2 + 200
        thangY = HEIGHT / 2 -150
        self.thang_Box = AboutUsCompBox(thangX, thangY, avatarSample3, "Nguyen Quoc Thang", "s3796613",
                                        "Through the project, I have learned valuable skills ", 1)

        ducX = WIDTH / 2 -70
        ducY = HEIGHT / 2 +250
        self.duc_Box = AboutUsCompBox(ducX, ducY, avatarSample4, "Nguyen Huu Duc", "s3669698",
                                      "I have experience in computer vision projects and an interest in AI technology. ",
                                      1)

        # ----------------------------------- END ----------------------------------------

    def checkInput(self):
        if self.cancelButton.checkForInput():
            return UI_STATES["main"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        return UI_STATES["about"]

    def draw_UI(self):
        self.screen.blit(self.overlay, (0, 0))
        self.aboutPanel.draw(self.screen)
        self.khoa_Box.draw(self.screen)
        self.khai_Box.draw(self.screen)
        self.thang_Box.draw(self.screen)
        self.duc_Box.draw(self.screen)
        self.cancelButton.draw(self.screen)


class settingUI:
    def __init__(self, screen):
        self.screen = screen
        # -------------- Overlay color ----------------
        self.overlay = pygame.Surface((WIDTH, HEIGHT))
        self.overlay.set_alpha(80)
        self.overlay.fill((0, 0, 0))
        # -------------- Overlay Panel ----------------
        settingPanel_img = pygame.image.load('assets/MilkTeaImages/Setting.png').convert_alpha()
        self.settingPanel = GamePanel(WIDTH / 2, HEIGHT / 2, settingPanel_img, 1)

        # -------------- Cancel symbol ----------------
        self.cancel_img = cancel_img
        # cancel property
        cancelX = WIDTH / 2 + 200
        cancelY = HEIGHT / 2 - 240
        self.cancelButton = CompleteButton(cancelX, cancelY, self.cancel_img, 0.8)
        # -------------- Music icon ----------------
        musicIcon_img = pygame.image.load('assets/MilkTeaImages/MusicIcon.png').convert_alpha()
        musicSettingX = WIDTH / 2
        musicSettingY = HEIGHT / 2 - 50
        self.musicSetting = SettingCompBox(musicSettingX, musicSettingY, musicIcon_img, "Music", 1)

    def draw_UI(self):
        self.screen.blit(self.overlay, (0, 0))
        self.settingPanel.draw(self.screen)
        self.musicSetting.draw(self.screen)
        self.cancelButton.draw(self.screen)
        if self.musicSetting.draw(self.screen):
            MusicController.PlayMusic()
        else:
            MusicController.StopMusic()
        if self.cancelButton.checkForInput():
            return UI_STATES["main"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        return UI_STATES["setting"]


class inGameUI:

    # ====== FIX HERE ==============
    def __init__(self, screen, level=0):
        self.screen = screen
        self.level = level + len(Constants.UI_STATES)
        buttonScale = 0.6
        iconScale = 0.3
        # ------------------------ Restart Button ------------------------
        restartIcon = pygame.image.load('assets/MilkTeaImages/RestartIcon.png').convert_alpha()
        restartPosX = Constants.WIDTH - screenPaddingX - restartIcon.get_width() / 2
        restartPosY = screenPaddingY
        self.restartButton = IconButton2(restartPosX, restartPosY, squareButton_img, restartIcon, buttonScale,
                                         iconScale)

        # ------------------------ Return Button ------------------------
        returnIcon = pygame.image.load('assets/MilkTeaImages/ReturnIcon.png').convert_alpha()
        returnPosX = screenPaddingX
        returnPosY = screenPaddingY
        self.returnButton = IconButton2(returnPosX, returnPosY, squareButton_img, returnIcon, buttonScale, iconScale)

    def checkInput(self, time_now, next_allowed):
        if self.returnButton.checkInput():
            return UI_STATES["levelSelect"]
        if time_now > next_allowed:
            if self.restartButton.checkInput():
                return UI_STATES["restart"]
        return self.level + len(Constants.UI_STATES)

    def draw(self):
        self.returnButton.draw(self.screen)
        self.restartButton.draw(self.screen)


class wonPanelUI:
    def __init__(self, screen):
        self.screen = screen
        # -------------- Overlay color ----------------
        self.overlay = pygame.Surface((WIDTH, HEIGHT))
        self.overlay.set_alpha(80)
        self.overlay.fill((0, 0, 0))
        # -------------- Overlay Panel ----------------
        wonPanel_img = pygame.image.load('assets/MilkTeaImages/YouWon.png').convert_alpha()
        self.aboutPanel = GamePanel(WIDTH / 2, HEIGHT / 2, wonPanel_img, 0.9)
        # -------------- Continue Button ----------------
        conButton_img = pygame.image.load('assets/MilkTeaImages/ContinueButton.png').convert_alpha()
        conButtonX = WIDTH / 2 - conButton_img.get_width() / 2 + 250
        conButtonY = HEIGHT / 2 - conButton_img.get_height() / 2 + 300
        self.conButton = CompleteButton(conButtonX, conButtonY, conButton_img, 1)
        # -------------- Selector Button ----------------
        selector = pygame.image.load('assets/MilkTeaImages/YouWon_Selector.png').convert_alpha()
        selButtonX = WIDTH / 2 - selector.get_width() / 2 + 70
        selButtonY = HEIGHT / 2 - selector.get_height() / 2 + 240
        self.selectorButton = CompleteButton(selButtonX, selButtonY, selector, 1)

    def checkInput(self):
        pygame.event.pump()
        if self.selectorButton.checkForInput():
            return Constants.UI_STATES["levelSelect"]
        if self.conButton.checkForInput():
            return Constants.UI_STATES["next"]
        return Constants.UI_STATES["cleared"]

    def draw(self):
        self.screen.blit(self.overlay, (0, 0))
        self.aboutPanel.draw(self.screen)
        self.conButton.draw(self.screen)
        self.selectorButton.draw(self.screen)


class losePanelUI:
    def __init__(self, screen):
        self.screen = screen
        # -------------- Overlay color ----------------
        self.overlay = pygame.Surface((WIDTH, HEIGHT))
        self.overlay.set_alpha(80)
        self.overlay.fill((0, 0, 0))
        # -------------- Overlay Panel ----------------
        losePanel_img = pygame.image.load('assets/MilkTeaImages/YouLose.png').convert_alpha()
        self.aboutPanel = GamePanel(WIDTH / 2, HEIGHT / 2, losePanel_img, 1)
        # -------------- retry Button ----------------
        retry_img = pygame.image.load('assets/MilkTeaImages/YouLoseButton_Retry.png').convert_alpha()
        conButtonX = WIDTH / 2 - retry_img.get_width() / 2 + 300
        conButtonY = HEIGHT / 2 - retry_img.get_height() / 2 + 250
        self.retryButton = CompleteButton(conButtonX, conButtonY, retry_img, 1)
        # -------------- Selector Button ----------------
        selector = pygame.image.load('assets/MilkTeaImages/YouLoseButton_Menu.png').convert_alpha()
        selButtonX = WIDTH / 2 - selector.get_width() / 2 + 100
        selButtonY = HEIGHT / 2 - selector.get_height() / 2 + 200
        self.selectorButton = CompleteButton(selButtonX, selButtonY, selector, 1)

    def checkInput(self):
        pygame.event.pump()
        if self.retryButton.checkForInput():
            return Constants.UI_STATES["restart"]
        if self.selectorButton.checkForInput():
            return UI_STATES["levelSelect"]
        return Constants.UI_STATES["lose"]

    def draw(self):
        self.screen.blit(self.overlay, (0, 0))
        self.aboutPanel.draw(self.screen)
        self.retryButton.draw(self.screen)
        self.selectorButton.draw(self.screen)
