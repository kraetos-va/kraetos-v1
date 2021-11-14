from core.engine import shutdown
from core.osmosis import listen, speak, understand
from core.playbook import directive, isActivate

def listener(engine):
    print("Listening..")
    input = listen()
    inputText = understand(input[0], input[1])
    print("input: {}".format(inputText))
    if isActivate(inputText):
        return follow(engine)
    else:
        return 'Null'

def follow(engine):
    print("Hi! I'm here..")
    speak(engine, "Hi, I'm listening")
    input = listen()
    inputText = understand(input[0], input[1])
    return directive(inputText)

def trigger(engine, action):
    if action == 'None':
        return False
    elif action == 'SHUTDOWN':
        shutdown(engine)
        return 'None'
    elif action == 'INVALID':
        speak(engine, "Sorry! that is an invalid request")
        return False
    else:
        return True