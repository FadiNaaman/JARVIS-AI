import engine
from datetime import datetime

def greetings():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        engine.speak(f"Good Morning {engine.USERNAME}")
    elif (hour >= 12) and (hour < 18):
        engine.speak(f"Good Afternoon {engine.USERNAME}")
    else:
        engine.speak(f"Good Evening {engine.USERNAME}")

# Settings
def changeRate(num):
    rate = engine.getRate()
    rate += num
    if rate < 0:
        rate = 0
    engine.setRate(rate)

def changeVolume(num):
    volume = engine.getVolume()
    volume += num
    if volume > 1.0:
        volume = 1.0
    if volume < 0.0:
        volume = 0.0
    engine.setVolume(volume)

def changePitch(num):
    pitch = engine.getPitch()
    pitch += num
    if pitch > 1.0:
        pitch = 1.0
    if pitch < 0.0:
        pitch = 0.0
    engine.setPitch(pitch)

def changeVoice(id):
    engine.setVoice(id)