import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import smtplib

import sys
import random
import numpy
import requests
import bs4
import pyaudio
import cv2

engine = pyttsx3.init("sapi5")
# engine = pyttsx3.init()


def speak(message):
     engine.say('{}' .format(message))
     engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon ")

    else:
        speak("Good evening")
    speak("i am computer voice E assistance ,   tell me how can i help you ")


def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak(" listening")
        print("listening..............")

        r.pause_threshhold = 1
        r.energy_threshold = 7000
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        speak('recognizing')
        print("recognizing .......")
        query = r.recognize_google(audio, language='en-in')
        print(F"USER SAID: {query} \n")
    except Exception as e:
        print(e)

        print("say that again please...")
        return "none"
    return query


wish();



while True:
    query = take().lower()
# logic for exicuting tasks based on on query

    if 'wikipedia' in query:
        speak('searching wikipedia ...')
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=3)
        speak("according to wikipedia")
        print(result)
        speak(result)

    elif'search' in query:
        speak("what you want search")
        p = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening..............")
            audio = p.listen(source)
            text = p.recognize_google(audio)
            p.pause_threshold = 1
            p.energy_threshold = 5000
            speak('searching......')
            url = 'https://google.com/search?q='
            search_url = url+text
            webbrowser.open(search_url)


    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif ' can you do' in query:
        speak('i can do variety of things for you')
        print(" such as :"
              "opening google,  wikepedia of something, blog, twitter,  facebook"
              "  can ask about h o d of c s e department,  about my name , play music and more  ")

        speak(" such as :"
              "opening google, wikepedia of something, blog, twitter, facebook"
              "can ask about h o d of c s e department, about my name, play music and more  ")

    elif 'open facebook' in query:
        webbrowser.open("facebook.com")

    elif 'your name' in query:
        speak('my name is COMPUTER VOICE E ASSISTANT')

    elif 'hi assistant' in query:
        speak('hello, how are you sir')
          
    elif 'explain' in query:
        print(" hi every one, let me first introduce my self, i am a program code over the phython "
              "3.7 version on the pyCharm")
        print("by Vaibhav Arora, B tech, 1st semester")
        print("This program reflects small reflention of upgrowing technology that is Artificial intelligence")
        print("it could do variety of tasks over voice command ")
        print("you still be wondering of what can i exactly do ")
        print("so the answer is ,     ")
        print('i can do variety of things for you')
        print("such as :"
              "sending Gmail, opening google, wikepedia of something, blog, twitter, facebook"
              "about my name, play music and much more  ")

        speak(" hi every one, let me first introduce my self, i am a program code over the phython 3.7 version "
              "on the pyCharm")
        speak("by Vaibhav Arora, B tech, 1st semester")
        speak("This program reflects small reflention of upgrowing technology that is Artificial intelligence")
        speak("it could do variety of tasks over voice command ")
        speak("you still be wondering of what can i exactly do ")
        speak("so the answer is ,     ")
        speak('i can do variety of things for you')
        speak(" such as :"
              " sending Gmail, opening google, wikepedia of something, blog, twitter, facebook"
              "about my name, play music and much more  ")

        speak("many upgradation are still in progress ")

    elif 'hod of cse' in query:
        speak('engineer sandeep sharma is H O D OF  C S E DEPARTMENT')

    elif "joke" in query:
        speak("where is timbuktu, asked teacher")
        speak("chintu raised his hands ")
        speak("replied    between timbuk 1 and timbuk 3")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'open blog' in query:
        webbrowser.open("computergenetics102.blogspot.com")

    elif 'open twitter' in query:
        webbrowser.open("twitter.com")

   

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")

    elif 'play song' or'play music' in query:
        music_dir = 'C:\\Users\\Sujit\\Desktop\\songs'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'open paint' in query:
        path = "%windir%\\system32\\mspaint.exe"
        os.startfile(path)

  

    elif ' tell location ' or 'map' in query:
        location = input('pls type the location     ')
        speak("pls type the location")
        webbrowser.open("www.google.co.in/maps/search/" + location)

  
    else:
        speak('try again with different keyword or definite pattern')
