mainState="main"
settingState = "setting"
aboutState = "about"
subSetting= mainState
def CheckState(state):
    #print("what is state:"+subSetting+" - "+ state)
    return subSetting == state
def CheckSetting():
    return subSetting == settingState
def CheckAbout():
    return subSetting == aboutState
def SetState(state):
    global  subSetting
    subSetting = state
    #print("set state: "+subSetting)