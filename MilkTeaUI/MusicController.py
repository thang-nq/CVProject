from pygame import mixer
mixer.music.load('Music/Background.wav')
mixer.music.play(-1)
isPlaying =True
def StopMusic():
    global isPlaying
    if(not isPlaying):
        return
    mixer.music.stop()
    isPlaying =False
def PlayMusic():
    global isPlaying
    if(isPlaying):
        return
    mixer.music.play(-1)
    isPlaying = True