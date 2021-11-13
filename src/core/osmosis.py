import datetime
import speech_recognition as sR

# Speak Function
def speak(engine, textToSpeak):
    engine.say(textToSpeak)
    engine.runAndWait()

# Listen to user input
def listen():
    record = sR.Recognizer()
    with sR.Microphone() as source:
        record.pause_threshold = 1
        record.adjust_for_ambient_noise(source, duration = 1)
        audio = record.listen(source)
        return record, audio

# Process input with understand function
def understand(engine, record, audio):
    try:
        print("Recognising input...")
        greet(engine)
        query = record.recognize_google(audio, language='en_GB')
        return str(query).lower()
    except sR.UnknownValueError:
        print("I cannot hear/ understand you")
        speak(engine, "I cannot hear/ understand you")
        return "None"
    except sR.RequestError:
        print("Say that again please")
        speak(engine, "Say that again please?")
        return "None"

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