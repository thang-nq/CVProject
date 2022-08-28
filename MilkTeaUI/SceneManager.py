import threading
import GameUI
import time

mainState = "main"
settingState = "setting"
aboutState = "about"
subSetting = mainState
UI_STATES = {"main": 0, "levelSelect": 1, "setting": 2, "about": 3, "game": 4}

buttonDelay = 1


class manager:
    def __init__(self,screen):
        self.gameState = UI_STATES['main']
        self.subSetting = mainState
        self.buttonPressed = False
        self.screen = screen
        self.mainState = "main"
        self.settingState = "setting"
        self.aboutState = "about"

        self.mainUI = GameUI.mainUI(self.screen)

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
        print(self.subSetting == aboutState)
        return self.subSetting == aboutState

    def CheckMain(self):
        return self.subSetting == mainState

    def SetState(self, state):
        self.gameState = UI_STATES[state]
        self.subSetting = state

        print("set state: "+self.subSetting)

    def getMainUI(self):
        self.mainUI
        self.gameState = UI_STATES[self.mainUI.draw_UI()]
