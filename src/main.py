# import the modules
from core.engine import initialise, configure, shutdown
from core.osmosis import listen, speak, understand
from core.playbook import directive
from helpers.stocks import checkStockPrice

# Controller
engineInit = initialise()
engine = configure(engineInit)
speak(engine, "Hello Abhinav")
input = listen()
inputText = understand(engine, input[0], input[1])
print("input: {}".format(inputText))
instruction = directive(inputText)
print(instruction)
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
