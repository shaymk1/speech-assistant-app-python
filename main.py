
import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()


def record_audio():  # using microphone
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print('sorry, i did not get that! Please try again!')
        except sr.RequestError:
            print('sorry, my speech service is down right now!')
        return voice_data


print('hi, how can i help you today?')
