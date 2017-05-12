#!/usr/bin/env python
import speech_recognition as sr
from moviepy.editor import VideoFileClip
#from moviepy.video.io.VideoFileClip import VideoFileClip
import pygame
import subprocess

def getAudioInput():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        audio = r.listen(source)


    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        #print("Google Speech Recognition thinks you said: " + r.recognize_google(audio))
        print("")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    #   
    global audioInput
    audioInput = r.recognize_google(audio).lower()
    print("This is the output of getAudioInput: " + audioInput)
    return audioInput    

def playVideo(filename):
    pygame.display.set_caption('My video!')
    clip = VideoFileClip(filename)
    clip.preview(fps=25)
    pygame.quit()

def repeatUserInput(toRepeat): 
    print("You said " + toRepeat)

def determineAction(userInput):
    global action
    if "play" in userInput and "video" in userInput:
        action = "playVideo"
    else:
        action = 'repeatUserInput'
    print("This is the output of determineAction. The action: " + action)
    return action
    
def determineVideoFilename(userInput):
    if "about" in audioInput:
        videoFilename = "video1.mp4"
    else:
        videoFilename = "play.mov"
        print("This is the output of determineVideoFilename. Filename: " + videoFilename)
    return videoFilename

####TESTING:
vid1 = ("./play.mov")
subprocess.call('open ' + vid1, shell=True)
#playVideo("./play.mov")
####End of TESTING
###toDo = determineAction(getAudioInput()) 

###if  toDo == "repeatUserInput":
###    repeatUserInput(audioInput)

###elif toDo == "playVideo":
###    print("I will play a video called " + determineVideoFilename(audioInput))