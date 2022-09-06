import threading
import GameUI
import time
import Constants
import gameV2
import pymunk

UI_STATES = Constants.UI_STATES

buttonDelay = 1


class manager:
    def __init__(self, screen):
        self.gameState = UI_STATES['main']
        self.time_now = 0
        self.next_allowed = 0
        self.DELAY = Constants.DELAY
        self.count = 0
        self.buttonPressed = False
        self.screen = screen
        # self.space = space

        # ------------------- UIs ---------------------
        self.mainUI = GameUI.mainUI(self.screen)
        self.levelsUI = GameUI.selectorUI(self.screen)
        self.aboutUI = GameUI.aboutUI(self.screen)
        self.settingUI = GameUI.settingUI(self.screen)
        self.inGameUI = GameUI.inGameUI(self.screen)
        self.game = gameV2.Bubble_tea(self.screen)
        self.wonPanelUI = GameUI.wonPanelUI(self.screen)
        self.losePanelUI = GameUI.losePanelUI(self.screen)


    def SetOffButton(self):
        self.buttonPressed = False

    def SetOnButton(self):
        setOff = threading.Timer(buttonDelay, self.SetOffButton)
        setOff.start()
        # buttonPressed = False

    def getMainUI(self):
        self.mainUI.draw_UI()

    def checkMainUI(self):
        self.gameState = self.mainUI.checkInput()
        if self.gameState == UI_STATES['levelSelect']:
            self.next_allowed = self.time_now + self.DELAY
            self.SetOnButton()

    def getLevelSelect(self):
        self.levelsUI.draw_UI()

        self.gameState = self.levelsUI.checkInput(self.time_now, self.next_allowed)
        # print(self.gameState)

    def getAbout(self):
        self.aboutUI.draw_UI()
        self.gameState = self.aboutUI.checkInput()

    def getSetting(self):
        self.gameState = self.settingUI.draw_UI()

    def getLevel(self, gameState=len(Constants.UI_STATES)):
        level = gameState - len(Constants.UI_STATES)

    def loadLevel(self):
        self.game.main_loop()

    def getGame(self):
        self.game.event_hanlder()
        self.game.draw()
        self.inGameUI.draw()
        if self.game.ended != 0:
            self.gameState = Constants.UI_STATES["cleared"]
        temp = self.inGameUI.checkInput(self.time_now, self.next_allowed)
        if temp != self.gameState:
            self.gameState = temp
            self.next_allowed = self.time_now + self.DELAY + 1000

        self.game.update()

    def restartGame(self):
        self.game.restart()

    def getWinPanel(self):
        temp = self.wonPanelUI.checkInput()
        if temp != self.gameState and self.count <=0:
            self.count += 1
            self.gameState = temp
            self.wonPanelUI.draw()
            self.game.restart()
        elif self.count >=0:
            self.gameState = self.wonPanelUI.checkInput()


    def getLosePanel(self):
        self.losePanelUI.draw()
        self.gameState = self.losePanelUI.checkInput()