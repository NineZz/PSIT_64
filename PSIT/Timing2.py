"""Timing II"""
def time():
    """function time"""
    second = int(input())
    minute = second//60
    hour = minute//60
    day = hour//24
    if day < 10000:
        print("%04d:%02d:%02d:%02d"%(day, hour%24, minute%60, second%60))
    elif day >= 10000:
        print("ERR_:__:__:__")
time()
