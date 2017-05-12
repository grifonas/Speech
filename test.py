#!/usr/bin/env python
import speech_recognition as sr
from moviepy.editor import VideoFileClip
#from moviepy.video.io.VideoFileClip import VideoFileClip
import pygame


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("I'm listenning...")
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

userInput = r.recognize_google(audio)
userInput = userInput.lower()
print userInput

if "play" in userInput and "video" in userInput and "mi" in userInput:
    
    filename = 'video1.mp4'
else:
	filename = 'play.mov'

print (filename)

pygame.display.set_caption('My video!')

clip = VideoFileClip(filename)
clip.preview(fps=25)
pygame.quit()