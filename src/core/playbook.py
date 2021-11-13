import re

def directive(input):
    if re.match('.*spotify.*', input):
        return 'SPOTIFY'
    elif re.match('.*weather.*', input):
        return 'WEATHER'
    elif re.match('.*time.*', input):
        return 'TIME'
    else:
        return "None"