import  pygame
#init screen
pygame.init()

#create the screen
screenWidth=1500
screenHeight=810
screen =pygame.display.set_mode((screenWidth,screenHeight))

#caption
pygame.display.set_caption("MilkTea")

#background
menuBackground = pygame.image.load('MilkTeaImages/Background.png')
screenPaddingX=50
screenPaddingY=50
#play button
playButton_img = pygame.image.load('MilkTeaImages/PlayButton.png')
#compute play button property
playButtonScale=0.6
playButtonX=screenWidth/2-int(playButton_img.get_width()/2*playButtonScale)
playButtonY=screenHeight/2-int(playButton_img.get_height()/2*playButtonScale)
#button
squareButton_img=pygame.image.load('MilkTeaImages/Button_Square.png')
squareWidth=squareButton_img.get_width()
squareHeight=squareButton_img.get_height()
buttonScale=0.5
#setting
settingIcon_img=pygame.image.load('MilkTeaImages/SettingIcon.png')
#compute setting button property
settingButtonX=screenPaddingX
settingButtonY=screenHeight - screenPaddingY - int(squareWidth*buttonScale)
#about button
aboutIcon_img=pygame.image.load('MilkTeaImages/AboutIcon.png')
#compute setting button property
aboutButtonX=settingButtonX+120
aboutButtonY=settingButtonY
#about property
exitIcon_img=pygame.image.load("MilkTeaImages/ExitIcon.png")
#exit property
exitButtonX=screenWidth-screenPaddingX-exitIcon_img.get_width()/2
exitButtonY=settingButtonY
#Class button
class CompleteButton():
    def __init__(self,x,y,image,scale):
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        #draw button on the screen
        screen.blit(self.image,( self.rect.x,self.rect.y))
class IconButton():
    def __init__(self,x,y,image,icon,scale):
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        iconWidth=icon.get_width()
        iconHeight=icon.get_height()
        self.icon = pygame.transform.scale(icon,(int(iconWidth*scale),int(iconHeight*scale)))
    def draw(self):
        #draw button on the screen
        screen.blit(self.image,(self.rect.x,self.rect.y))
        #draw icon on the screen
        width=self.image.get_width()
        height=self.image.get_height()
        iconWidth = self.icon.get_width()
        iconHeight = self.icon.get_height()
        screen.blit(self.icon,(self.rect.x+int(width/2)-int(iconWidth/2),self.rect.y+int(height/2)-int(iconHeight/2)))

#Generate button
play_Button = CompleteButton(playButtonX,playButtonY,playButton_img,playButtonScale)
settingButton=IconButton(settingButtonX,settingButtonY,squareButton_img,settingIcon_img,buttonScale)
aboutButton=IconButton(aboutButtonX,aboutButtonY,squareButton_img,aboutIcon_img,buttonScale)
exitButton=IconButton(exitButtonX,exitButtonY,squareButton_img,exitIcon_img,buttonScale)
#Game loop
running = True

while running:
    screen.blit(menuBackground,(0,0))
    play_Button.draw()
    settingButton.draw()
    aboutButton.draw()
    exitButton.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()