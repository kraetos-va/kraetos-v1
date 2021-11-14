# import the modules
from core.engine import initialise, configure
from core.osmosis import greet
from helpers.listener import listener, trigger
from helpers.stocks import checkStockPrice

# boot up engine
def init():
    engineInit = initialise()
    return configure(engineInit)

# start function to initialise AI engine
def start():
    engine = init()
    greet(engine)
    chore(engine)

# chore function to perform action if found valid speech instructions
def chore(engine):
    action = listener(engine)
    if isinstance(trigger(engine, action), str) and trigger(engine, action) == 'None':
        print("Shutting down")
    elif isinstance(trigger(engine, action), bool) and trigger(engine, action):
        checkStockPrice()
        chore(engine)
    else:
        chore(engine)

# main controller
start()
