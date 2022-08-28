import threading
import time

mainState = "main"
settingState = "setting"
aboutState = "about"
subSetting = mainState

buttonPressed = False
buttonDelay = 1


def SetOffButton():
    global buttonPressed
    buttonPressed = False


def SetOnButton():
    global buttonPressed
    buttonPressed = True
    setOff = threading.Timer(buttonDelay, SetOffButton)

    setOff.start()
    # buttonPressed = False


def MainButtonPressed():
    return buttonPressed


def CheckState(state):
    print("what is state:"+subSetting+" - "+ state)
    return subSetting == state


def CheckSetting():
    return subSetting == settingState


def CheckAbout():
    return subSetting == aboutState


def CheckMain():
    return subSetting == mainState


def SetState(state):
    global subSetting
    subSetting = state
    # print("set state: "+subSetting)
