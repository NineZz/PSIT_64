"""WPM"""
def kids(speed):
    """check"""
    if speed < 11:
        return 'Very Slow'
    elif 11 <= speed <= 20:
        return 'Slow'
    elif 21 <= speed <= 30:
        return 'Average'
    elif 31 <= speed <= 40:
        return 'Fast'
    else:
        return 'Very Fast'

def adult(speed):
    """check"""
    if speed < 26:
        return 'Very Slow'
    elif 26 <= speed <= 35:
        return 'Slow/Beginner'
    elif 36 <= speed <= 45:
        return 'Intermediate/Average'
    elif 46 <= speed <= 65:
        return 'Fast/Advanced'
    elif 66 <= speed <= 80:
        return 'Very Fast'
    else:
        return 'Insane'

def wpm():
    """WPM"""
    age = input()
    speed = int(input())
    if age == 'Kids':
        print(kids(speed))
    elif age == 'Adults':
        print(adult(speed))
wpm()
