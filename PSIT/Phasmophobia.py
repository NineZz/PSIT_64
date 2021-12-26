"""Phasmophobia"""
def add(val):
    '''add'''
    if val == 'No evidence':
        return {'Banshee', 'Demon', 'Jinn', 'Mare', 'Oni', 'Phantom', \
            'Poltergeist', 'Revenant', 'Shade', 'Spirit', 'Wraith', 'Yurei'}
    elif val == 'Ghost Orb':
        return {'Jinn', 'Mare', 'Phantom', 'Poltergeist', 'Shade', 'Yurei'}
    elif val == 'Spirit Box':
        return {'Demon', 'Jinn', 'Mare', 'Oni', 'Poltergeist', 'Spirit', 'Wraith'}
    elif val == 'Fingerprints':
        return {'Banshee', 'Poltergeist', 'Revenant', 'Spirit', 'Wraith'}
    elif val == 'EMF Level 5':
        return {'Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade'}
    elif val == 'Freezing Temperatures':
        return {'Banshee', 'Demon', 'Mare', 'Phantom', 'Wraith', 'Yurei'}
    elif val == 'Ghost Writing':
        return {'Demon', 'Oni', 'Revenant', 'Shade', 'Spirit', 'Yurei'}
def main(val1, val2, val3):
    """Phasmophobia"""
    clue1 = add(val1)
    clue2 = add(val2)
    clue3 = add(val3)
    ans = sorted(clue1&clue2&clue3)
    if len(ans) == 0:
        print('Not yet discovered')
    else:
        print(*ans, sep='\n')
main(input(), input(), input())
