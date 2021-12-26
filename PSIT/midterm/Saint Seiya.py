"""Saint Seiya"""

def main():
    """Saint Seiya"""
    time = int(input())
    punch = int(input())
    damage = 0
    count = 1
    if ((time//2)-(time//6))*165+(time//6) <= punch:
        print(((time//2)-(time//6))*165+(time//6))
    else:
        while damage < punch and count <= time:
            if count%6 == 0:
                damage += 1
            elif count%2 == 0:
                damage += 165
            count += 1
        if time-count >= 0:
            damage += 12*(time-count)
        print(damage)
main()
