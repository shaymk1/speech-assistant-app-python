
from re import search
import speech_recognition as sr
from time import ctime
import webbrowser
import time
import os
import playsound
import random
from gtts import gTTS


# initialize the recognizer
r = sr.Recognizer()


def record_audio(ask=False):  # using microphone
    with sr.Microphone() as source:
        if ask:
            alexas_speak(ask)

        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexas_speak('sorry, i did not get that! Please try again!')
        except sr.RequestError:
            alexas_speak('sorry, my speech service is down right now!')
        return voice_data


def alexas_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')  # tts=text-to-string
    random_number = random.randint(1, 1000000)
    audio_file = 'audio-' + str(random_number) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)  # play the audio file
    print(audio_string)
    os.remove(audio_file)


def response(voice_data):  # coming from alexa
    if 'what is your name' in voice_data:
        alexas_speak('my name is Shay')
    if 'what time is it' in voice_data:
        alexas_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexas_speak('here are the results of your ' + search)
    if 'find location' in voice_data:
        location = record_audio('find location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexas_speak('Please tell me what location is that?  ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
alexas_speak('hi, how can i help you today?')
while (1):
    voice_data = record_audio()  # get the voice input
    response(voice_data)
