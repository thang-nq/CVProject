import threading
import GameUI
import time
import Constants
import gameV2
import pygame.event

UI_STATES = Constants.UI_STATES

buttonDelay = 1


class manager:
    def __init__(self,screen):
        self.gameState = UI_STATES['main']
        self.time_now = 0
        self.next_allowed = 0
        self.DELAY = Constants.DELAY


        self.buttonPressed = False
        self.screen = screen


        #------------------- UIs ---------------------
        self.mainUI = GameUI.mainUI(self.screen)
        self.levelsUI = GameUI.selectorUI(self.screen)
        self.aboutUI = GameUI.aboutUI(self.screen)
        self.settingUI = GameUI.settingUI(self.screen)
        self.inGameUI = GameUI.inGameUI(self.screen)
        self.game = gameV2.Bubble_tea(self.screen)

    def SetOffButton(self):
        self.buttonPressed = False

    def SetOnButton(self):
        setOff = threading.Timer(buttonDelay, self.SetOffButton)
        setOff.start()
        # buttonPressed = False


    def SetState(self, state):
        self.gameState = state

        print("set state: "+self.subSetting)

    def getMainUI(self):
        self.gameState = self.mainUI.draw_UI()
        if self.gameState == UI_STATES['levelSelect']:
            self.next_allowed = self.time_now + self.DELAY
            self.SetOnButton()

    def getLevelSelect(self):
        self.gameState = self.levelsUI.draw_UI(self.time_now,self.next_allowed)


    def getAbout(self):
        self.gameState = self.aboutUI.draw_UI()

    def getSetting(self):
        self.gameState = self.settingUI.draw_UI()

    def getLevel(self, gameState = len(Constants.UI_STATES)):
        level = gameState - len(Constants.UI_STATES)

    def loadLevel(self):
        self.game.main_loop()

    def getGame(self):

        self.game.event_hanlder()
        self.game.draw()
        self.gameState = self.inGameUI.draw()
        self.game.update()
