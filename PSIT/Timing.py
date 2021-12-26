"""Timing"""
def main():
    """time"""
    second = int(input())
    minute = second//60
    hour = minute//60
    day = hour//24
    print("%d %d %d %d"%(day, hour%24, minute%60, second%60))
main()
