import pyttsx3

# Initialise pyttsx3 engine
def initialise():
    return pyttsx3.init()

# Configure pyttsx3 engine
def configure(engine):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 1)
    engine.setProperty('voice', "com.apple.speech.synthesis.voice.Daniel")
    return engine

# Shutdown pyttsx3 engine
def shutdown(engine):
    engine.stop()