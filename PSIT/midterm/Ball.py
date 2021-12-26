"""Ball"""

def ball():
    """Ball"""
    height = float(input())
    count = 0
    while True:
        if height < 0.01:
            count -= 1
            break
        height = height * 0.6
        count += 1
    print(count)

ball()

