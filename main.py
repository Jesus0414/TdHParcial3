import speech_recognition as sr
import time 
import webbrowser
import playsound
import os
import random
from time import ctime
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexa_speak('Lo siento, no te entendi')
        except sr.RequestError:
            alexa_speak('Lo siento, error de conexion')
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='es')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'como te llamas' in voice_data:
        alexa_speak('Mi nombre es alexis')
    if 'que hora es' in voice_data:
        alexa_speak(ctime())
    if 'buscar' in voice_data:
        buscar = record_audio('Que necesitas buscar?')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        alexa_speak('Esto fue lo que encontre para: ' + buscar)
    if 'mapa' in voice_data:
        lugar = record_audio("Que lugar quieres buscar?")
        url = 'https://google.nl/maps/place/' + lugar + '/&amp;'
        webbrowser.get().open(url)
        alexa_speak('Es lo que encontre para:' + lugar)
    if 'videos' in voice_data:
        video = record_audio("Que video quieres?")
        url = 'https://www.youtube.com/results?search_query=' + video
        webbrowser.get().open(url)
        alexa_speak('Es lo que encontre para:' + video)
    if 'anime' in voice_data:
        anime = record_audio("Que anime quieres buscar?")
        url = 'https://www3.animeflv.net/browse?q=' + anime
        webbrowser.get().open(url)
        alexa_speak('Es lo que encontre para:' + anime)
    if 'callate' in voice_data:
        exit()
#print('Como te puedo ayudar?')
#voice_data = record_audio()
#respond(voice_data)


time.sleep(1)
alexa_speak('Como te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)