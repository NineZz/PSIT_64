"""Olympic"""
def main(num, check, i=0, j=0):
    """Olympic"""
    oldg, olds, oldb, = 0, 0, 0
    for _ in range(num):
        country, gold, sil, bronze = input().split()
        check.append([-int(gold), -int(sil), -int(bronze), country])
    check.sort()
    for gold, sil, bronze, country in check:
        i += 1
        if oldg == abs(gold) and olds == abs(sil) and oldb == abs(bronze):
            print(j, country, abs(gold), abs(sil), abs(bronze), abs(gold+sil+bronze))
        else:
            print(i, country, abs(gold), abs(sil), abs(bronze), abs(gold+sil+bronze))
            j = i
        oldg, olds, oldb, = abs(gold), abs(sil), abs(bronze)
main(int(input()), [])
