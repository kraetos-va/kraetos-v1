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
        record.adjust_for_ambient_noise(source, duration = 0.5)
        audio = record.listen(source)
        return record, audio

# Process input with understand function
def understand(record, audio):
    try:
        print("Recognising input...")
        query = record.recognize_google(audio, language='en_GB')
        return str(query).lower()
    except sR.UnknownValueError:
        return 'None'
    except sR.RequestErrsor:
        return 'Null'

# Greeting Function
def greet(engine):
    hour = int(datetime.datetime.now().hour)
    owner = 'Abhinav'
    if hour >= 0 and hour <= 12:
        speak(engine, "Good Morning! {}".format(owner))
    elif hour > 12 and hour < 16:
        speak(engine, "Good Afternoon! {}".format(owner))
    elif hour > 16:
        speak(engine, "Good Evening! {}".format(owner))
    speak(engine, "I am kraetos, your virtual assistant")