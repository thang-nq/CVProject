import pygame
from Panel import GamePanel,SettingCompBox
from Button import CompleteButton
import SceneManager
import MusicController
# init screen

# create the screen
screenWidth = 1500
screenHeight = 810
#overlay color
s = pygame.Surface((screenWidth,screenHeight))
s.set_alpha(80)
s.fill((0,0,0))
#overlay panel
settingPanel_img = pygame.image.load('MilkTeaImages/Setting.png')
settingPanel = GamePanel(screenWidth/2,screenHeight/2,settingPanel_img,1)
#cancel panel
cancel_img =  pygame.image.load('MilkTeaImages/QuitButton.png')
#cancel property
cancelX=screenWidth/2 +200
cancelY=screenHeight/2 - 240
cancelButton = CompleteButton(cancelX,cancelY,cancel_img,0.8)
#icons
musicIcon_img=pygame.image.load('MilkTeaImages/MusicIcon.png')
musicSettingX=screenWidth/2
musicSettingY = screenHeight/2 -50
musicSetting = SettingCompBox(musicSettingX,musicSettingY,musicIcon_img,"Music",1)
def run(surface):
    surface.blit(s,(0,0))
    settingPanel.draw(surface)
    if musicSetting.draw(surface):
        MusicController.PlayMusic()
    else:
        MusicController.StopMusic()
    if(cancelButton.draw(surface)):
        SceneManager.SetState(SceneManager.mainState)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
