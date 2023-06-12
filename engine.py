import pyttsx3
from decouple import config
import speech_recognition as sr
import commands

USERNAME = config("USER")
BOTNAME = config("BOTNAME")

engine = pyttsx3.init("sapi5")

#Set Default Voice
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[2].id)

#Get Rate
def getRate():
    return engine.getProperty("rate")
#Set Rate
def setRate(num):
    engine.setProperty("rate",190)

#Get Volume
def getVolume():
    return engine.getProperty("volume")
#Set Volume
def setVolume(num):
    engine.setProperty("volume",num)

#Get Pitch 
def getPitch():
    return engine.getProperty("pitch")
# Set Pitch (0.0 to 1.0)
def setPitch(num):
    #Set Pitch
    engine.setProperty("pitch", num)
# Check Pitch Support with specific voice ID
def canPitch(id):
    if "pitch" in voices[id].__dict__:
        return True
    else:
        return False

#Get Voices
def getVoices():
    return voices
# Set Voice
def setVoice(index):
    #Set Voice
    engine.setProperty("voice",voices[index].id)

#Initialize Voice Settings
setRate(190)
setVolume(1.0)
setVolume(2)

# Speaking Function
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Listening Function
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print("Query: " + query)
    except sr.UnknownValueError:
        print("Google Recognition could not understand what you said")
    except sr.RequestError as e:
        print("Could not request Google Recognition. {0}".format(e))

#Wake Listen Function
def wakeListen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        query = query.lower()
        if "jarvis" in query:
            print("Query: " + query)
            #Process query meaning and do commands
    except sr.UnknownValueError:
        print("Google Recognition could not understand what you said")
    except sr.RequestError as e:
        print("Could not request Google Recognition. {0}".format(e))

    
def startup():
    print(f"Starting up {BOTNAME} A.I")
    commands.greetings()
        