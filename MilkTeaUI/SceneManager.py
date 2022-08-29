import threading
import GameUI
import time
import Constants
import config
mainState = "main"
settingState = "setting"
aboutState = "about"
subSetting = mainState
UI_STATES = Constants.UI_STATES

buttonDelay = 1


class manager:
    def __init__(self,screen):
        self.gameState = UI_STATES['main']
        self.time_now = 0
        self.next_allowed = 0
        self.DELAY = Constants.DELAY


        self.subSetting = mainState
        self.buttonPressed = False
        self.screen = screen
        self.mainState = "main"
        self.settingState = "setting"
        self.aboutState = "about"

        #TRACKING
        self.handstate = 'None'
        self.currentpos = (0, 0)

        #------------------- UIs ---------------------
        self.mainUI = GameUI.mainUI(self.screen, self.currentpos)
        self.levelsUI = GameUI.selectorUI(self.screen)
        self.aboutUI = GameUI.aboutUI(self.screen)
        self.settingUI = GameUI.settingUI(self.screen)

    def SetOffButton(self):
        self.buttonPressed = False

    def SetOnButton(self):
        self.buttonPressed = True
        setOff = threading.Timer(buttonDelay, self.SetOffButton)
        setOff.start()
        # buttonPressed = False

    def MainButtonPressed(self):
        return self.buttonPressed

    def CheckState(self, state):
        # print("what is state:"+subSetting+" - "+ state)
        return self.subSetting == state

    def CheckSetting(self):
        return self.subSetting == settingState

    def CheckAbout(self):
        return self.subSetting == aboutState

    def CheckMain(self):
        return self.subSetting == mainState

    def SetState(self, state):
        self.gameState = state
        self.subSetting = state

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
