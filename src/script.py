# import the modules
import pyttsx3
import speech_recognition as sR
import datetime
from googlesearch import search
from bs4 import BeautifulSoup
import requests

# Initialise pyttsx3 engine
def initialise():
    return pyttsx3.init()

# Configure pyttsx3 engine
def configure(engine):
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    engine.setProperty('rate', rate - 5)
    engine.setProperty('volume', volume + 5)
    engine.setProperty('voice', "com.apple.speech.synthesis.voice.Daniel")
    return engine

# Speak Function
def speak(engine, textToSpeak):
    engine.say(textToSpeak)
    engine.runAndWait()

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

# Listen to user input
def listen(engine):
    record = sR.Recognizer()
    with sR.Microphone() as source:
        record.pause_threshold = 1
        record.adjust_for_ambient_noise(source, duration = 1)
        audio = record.listen(source)
    try:
        print("Recognising input...")
        greet(engine)
        query = record.recognize_google(audio, language='en_GB')
        print("User said: {}".format(query))
        return query
    except sR.UnknownValueError:
        print("I cannot hear/ understand you")
        speak(engine, "I cannot hear/ understand you")
        return "None"
    except sR.RequestError:
        print("Say that again please")
        speak(engine, "Say that again please?")
        return "None"

# Make Google search query
def googleSearch(query):
    return search(query, lang = "en", num_results = 3)

# Check Price of stock
def checkStockPrice():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
        }
        for url in googleSearch("Tesla stock price yahoo finance"):
            print(url)
            page = requests.get(url, headers = headers)
            soup = BeautifulSoup(page.content, "html.parser")
            price = soup.find(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").get_text()
            title = soup.find(class_='D(ib) Fz(18px)').get_text()
            currency = soup.find(class_='C($tertiaryColor) Fz(12px)').get_text()
            currency = currency[-3:]
            print("{} - {} - {}".format(currency, title, price))
    except AttributeError as e:
        print("Attribute Error: {}".format(e))

# Shutdown pyttsx3 engine
def shutdown(engine):
    engine.stop()

# Controller
engineInit = initialise()
engine = configure(engineInit)
#speak(engine, "Hello Abhinav")
listen(engine)
checkStockPrice()
shutdown(engine)

# Appendix
# list voices
"""
voices = engine.getProperty('voices')
for voice in voices:
   print("{} : {}".format(voice.id, voice.languages))
com.apple.speech.synthesis.voice.fiona : ['en-scotland']
com.apple.speech.synthesis.voice.Fred : ['en_US']
com.apple.speech.synthesis.voice.karen : ['en_AU']
com.apple.speech.synthesis.voice.moira : ['en_IE']
com.apple.speech.synthesis.voice.rishi : ['en_IN']
com.apple.speech.synthesis.voice.samantha : ['en_US']
com.apple.speech.synthesis.voice.tessa : ['en_ZA']
com.apple.speech.synthesis.voice.veena : ['en_IN']
com.apple.speech.synthesis.voice.Victoria : ['en_US']
"""
