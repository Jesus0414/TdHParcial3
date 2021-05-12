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
            alexa_speak('Lo siento, ese buscador no existe, prueba otra vez')
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
    if 'Google' in voice_data:
        google = record_audio('Que imagen quieres buscar en google?')
        url = 'https://www.google.com/search?q=' + google + '&tbm=isch&ved=2ahUKEwi874ORosHwAhUErZ4KHfUuAnsQ2-cCegQIABAA&oq=pelicano&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BAgjECc6BAgAEEM6BggAEAoQGDoECAAQGFDPNVilQmDFRGgBcAB4AIABcIgBrAeSAQMyLjeYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=zUeaYPzUJITa-gT13YjYBw&bih=831&biw=1707&safe=active'
        webbrowser.get().open(url)
        alexa_speak('Esto fue lo que encontre para: ' + google + ' en google')
    if 'Yahoo' in voice_data:
        yahoo = record_audio("Que imagen quieres buscar en yahoo?")
        url = 'https://espanol.images.search.yahoo.com/search/images;_ylt=Awr9J.pCSJpga1EA1iADEQx.;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=' + yahoo + '&fr2=piv-web&fr=yfp-t'
        webbrowser.get().open(url)
        alexa_speak('Es lo que encontre para: ' + yahoo + ' en yahoo')
    if 'bingo' in voice_data:
        bing = record_audio("Que imagen quieres buscar en bing?")
        url = 'https://www.bing.com/images/search?q=' + bing 
        webbrowser.get().open(url)
        alexa_speak('Es lo que encontre para: ' + bing + ' en bing')
    if 'ecosia' in voice_data:
        ecosia = record_audio("Que imagen quieres buscar en ecosia?")
        url = 'https://www.ecosia.org/images?q=' + ecosia 
        webbrowser.get().open(url)
        alexa_speak('Es lo que encontre para: ' + ecosia + ' en ecosia')
    if 'silencio' in voice_data:
        exit()

print('Buscadores disponibles:')
print('-Google')
print('-Yahoo')
print('-Bingo = Bing')
print('-Ecosia')
time.sleep(1) 
alexa_speak('Bienvenido al buscador de imagenes, por favor mencione el buscador que quieras usar.')
while 1:
    voice_data = record_audio()
    respond(voice_data)