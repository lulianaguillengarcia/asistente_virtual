import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia
import random 

name = 'asistente'
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

bromas = [
    "¿Por qué la computadora fue al doctor? ¡Tenía un virus!",
    "¿Por qué el astronauta se divorció? ¡Porque necesitaba espacio!",
    "¿Qué le dice un semáforo a otro semáforo? ¡No me mires, que me estoy cambiando!",
    "¿Por qué la bicicleta se cayó? ¡Porque estaba dos-tired!",
    "¿Qué hace un pez en el espacio? ¡Nada, porque no hay agua!"
] 

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            #talk(rec)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
            return rec 
    except sr.UnknownValueError:
        talk("No se entendió el audio")
    except sr.RequestError as e:
        print("Error al solicitar resultados; {0}".format(e))
    except Exception as e:
        print(f"Error inesperado: {e}")

def run():
    rec = listen() 
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music) 
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, 1)
        talk(info)
    elif 'broma' in rec:
        talk(random.choice(bromas)) 
    elif 'cuenta un chiste' in rec:
        talk(random.choice(bromas)) 
run() 