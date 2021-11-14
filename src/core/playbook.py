import re

def isActivate(input):
    if re.match('.*(hey|hi|hello|morning|afternoon|evening).*kratos.*', input):
        return True
    elif re.match('.*kratos.*you\sthere.*', input):
        return True
    else:
        return False

def directive(input):
    if re.match('.*spotify.*', input):
        return spotifyDirective(input)
    elif re.match('.*weather.*', input):
        return weatherDirective(input)
    elif re.match('.*time.*', input):
        return timeDirective(input)
    elif re.match('.*shut\s*down.*', input):
        return 'SHUTDOWN'    
    else:
        return 'None'

def spotifyDirective(input):
    if re.match('.*open.*spotify.*', input):
        return 'OPEN_SPOTIFY'
    elif re.match('.*play.*spotify.*', input):
        return 'PLAY_SPOTIFY'
    elif re.match('.*pause.*spotify.*', input):
        return 'PAUSE_SPOTIFY'  
    else:
        return 'INVALID'

def timeDirective(input):
    if re.match('.*time.*(in|at|on|of).*', input):
        return 'PLACE_TIME'
    elif re.match('.*time.*', input):
        return 'CURRENT_LOCATION_TIME'
    else:
        return 'INVALID'

def weatherDirective(input):
    if re.match('.*weather.*(in|at|on|of).*', input):
        return 'PLACE_WEATHER'
    elif re.match('.*weather.*', input):
        return 'CURRENT_LOCATION_WEATHER'
    else:
        return 'INVALID'