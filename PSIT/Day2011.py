"""Day2011"""
def main(day, month, manyday=0):
    """Day2011"""
    for i in range(1, month):
        if i == 2:
            manyday += 28
        elif i == 4 or i == 6 or i == 9 or i == 11:
            manyday += 30
        else:
            manyday += 31
    manyday += day
    print('Saturday' if manyday%7 == 1 else 'Sunday' if manyday%7 == 2 else 'Monday' if \
        manyday%7 == 3 else 'Tuesday' if manyday%7 == 4 else 'Wednesday' if manyday%7 == 5 \
            else 'Thursday' if manyday%7 == 6 else 'Friday')
main(int(input()), int(input()))
