""""VerticalHistogram"""

def main():
    """VerticalHistogram"""
    txt = list(input())
    txt.sort(key=str.swapcase)

    alpha, num = [], []
    for i in txt:
        alpha += [i]
        num += [txt.count(i)]
        while txt.count(i) > 1:
            txt.remove(i)

    high = max(num)

    for i in range(high, 0, -1): #3
        print('%.03d' %i, end=' ')
        for j in num:
            if i == j or i < j:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    print('    ', end='')
    print(*alpha, sep=' ')
main()
