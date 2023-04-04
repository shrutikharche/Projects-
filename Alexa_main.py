import speech_recognition as sr
import pyttsx3
import time
from time import ctime
import webbrowser
import playsound
from gtts import gTTS
import os
import random
from tkinter import *
from PIL import ImageTk,Image

print('Listening...')
r = sr.Recognizer()
speaker = pyttsx3.init()
def record_audio(ask = False):

    #user voice record
    with sr.Microphone() as source:
        if ask:
            alexa_voice(ask)
            audio = r.listen(source)
            voice_data = " "
        try:
            voice_data = r.recognize_google(audio)
            print('Recognizer voice :'+ voice_data)
        except Exception:
            print('Oops something went Wrong')
            #alexa_voice('Oops something went Wrong')
        return voice_data
def alexa_voice(audio_string):
    #Play audio text to voice
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

class Widget: #GUI OF VIRTUAL ASSISTAND AND COMMANDSGIVEN
    def __init__(self):
        root = Tk()
        root.title('ALEXA')
        root.geometry('520x320')

        img = ImageTk.PhotoImage(Image.open('img2.jpg'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')
        compText = StringVar()
        userText = StringVar()
        userText.set('Your Virtual Assistant')
        userFrame = LabelFrame(root, text='Lena', font=('Railways', 24,'bold'))
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame, textvariable=userText, bg='black',fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        # compFrame = LabelFrame(root, text="Lena", font=('Railways',10, 'bold'))
        # compFrame.pack(fill="both", expand='yes')
        Button(root, text='Speak', font=('railways', 10, 'bold'),bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        Button(root, text='Close', font=('railways', 10,'bold'), bg='yellow', fg='black', command=root.destroy).pack(fill='x', expand='no')
        alex_voice('How can i help you ?')
        root.mainloop()
    def clicked(self):
    #BUTTON CALLING
        print("working...")
        voice_data = record_audio()
        voice_data = voice_data.lower()
        if 'who are you' in voice_data:
            alexa_voice('My name is alexa ')
        if 'search' in voice_data:
            search = record_audio('What do you want to search for ?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            alexa_voice('Here is what i found' + search)
        if 'find location' in voice_data:
            location = record_audio('What is your location?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            alexa_voice('Here is location' + location)
        if 'what is the time' in voice_data:
            alexa_voice("Sir the time is :" + ctime())
        if 'exit' in voice_data:
            alexa_voice('Thanks have a good day ')
            exit()

if __name__== '__main__':
    widget = Widget()
time.sleep(1)
while 1:
    voice_data = record_audio()
    respond(voice_data)

speaker.runAndWait()