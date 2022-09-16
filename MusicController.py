from pygame import mixer
mixer.music.load('assets/Music/Background.wav')
mixer.music.play(-1)
mixer.music.set_volume(0)
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