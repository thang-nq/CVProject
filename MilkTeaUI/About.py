import pygame
from Panel import GamePanel,AboutUsCompBox
from Button import CompleteButton
import SceneManager
# init screen

# create the screen
screenWidth = 1500
screenHeight = 810
#overlay color
s = pygame.Surface((screenWidth,screenHeight))
s.set_alpha(80)
s.fill((0,0,0))
#overlay panel
aboutPanel_img = pygame.image.load('MilkTeaImages/AboutUs.png')
aboutPanel = GamePanel(screenWidth/2,screenHeight/2,aboutPanel_img,1)
#cancel panel
cancel_img =  pygame.image.load('MilkTeaImages/QuitButton.png')
#cancel property
cancelX=screenWidth/2 +500
cancelY=screenHeight/2 - 300
cancelButton = CompleteButton(cancelX,cancelY,cancel_img,0.8)
#icons
avatarSample1 = pygame.image.load('MilkTeaImages/Avatar_Beereel.png')
avatarSample2 = pygame.image.load('MilkTeaImages/Avatar_Princess.png')
avatarSample3 = pygame.image.load('MilkTeaImages/Avatar_Tinia.png')
avatarSample4 = pygame.image.load('MilkTeaImages/Avatar_Scyn.png')
khoaX = screenWidth/2 -250
khoaY = screenHeight/2 - 50
khoa_Box = AboutUsCompBox(khoaX,khoaY,avatarSample1,"Tran Nguyen Anh Khoa","s3863956","I worked on the aesthetic, UX/ UI of the game ",1)
khaiX = screenWidth/2 - 200
khaiY = screenHeight/2 +100
khai_Box = AboutUsCompBox(khaiX,khaiY,avatarSample2,"Khai","s3863956","I worked on the physics simulation",1)
thangX = screenWidth/2 - 70
thangY = screenHeight/2 + 250
thang_Box = AboutUsCompBox(thangX,thangY,avatarSample3,"Thang","s3863956","I worked in the computer vision system",1)
ducX = screenWidth/2 +250
ducY = screenHeight/2 -150
duc_Box = AboutUsCompBox(ducX,ducY,avatarSample4,"Duc","s3863956","I worked in the computer vision system",1)
def run(surface):
    surface.blit(s,(0,0))
    aboutPanel.draw(surface)
    khoa_Box.draw(surface)
    khai_Box.draw(surface)
    thang_Box.draw(surface)
    duc_Box.draw(surface)
    if(cancelButton.draw(surface)):
        SceneManager.SetState(SceneManager.mainState)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
