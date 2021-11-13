from core.osmosis import speak
import datetime

# Greeting Function
def greet(engine):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak(engine, "Good Morning!")
    elif hour > 12 and hour < 16:
        speak(engine, "Good Afternoon!")
    elif hour > 16:
        speak(engine, "Good Evening!")
    speak(engine, "I am kraetos, your virtual assistant.")