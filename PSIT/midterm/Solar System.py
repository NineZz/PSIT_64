"""Solar System"""
def add(spp, index):
    """Solar System"""
    for i in range(spp.count(" ")):
        tss = spp.find(" ")
        ffdsa = spp[0:tss]
        if index == i:
            return ffdsa
        spp = spp[tss+1:]
def add2(st1, checki, suncheck):
    """Solar System"""
    hot, cool = '', ''
    hot = str(add(st1, suncheck - 1))
    if checki >= 3:
        cool = str(add(st1, 0))
    elif checki == 2:
        cool = str(add(st1, suncheck - 1))
    return hot, cool
def main():
    """Solar System"""
    st1, suncheck, hot, cool = str(input()) + " .", -1, '', ''
    spp, checki = st1, st1.count(" ")
    for i in range(st1.count(" ")):
        tss = spp.find(" ")
        ffdsa = spp[0:tss]
        if ffdsa.lower() == "sun":
            suncheck = i
        spp = spp[tss+1:]
    if suncheck == -1:
        pass
    elif suncheck == 0:
        hot = str(add(st1, suncheck + 1))
        if checki >= 3:
            cool = str(add(st1, checki - 1))
        elif checki == 2:
            cool = str(add(st1, suncheck + 1))
    elif suncheck == checki or suncheck == checki - 1:
        hot, cool = add2(st1, checki, suncheck)
    else:
        if checki > 3:
            hot = str(add(st1, suncheck - 1)) + " " + \
                str(add(st1, suncheck + 1))
            if checki >= 5 and int(checki / 2) == suncheck:
                cool = str(add(st1, 0)) + " " + str(add(st1, checki - 1))
            else:
                if suncheck == 1 or int(checki / 2) > suncheck:
                    cool = str(add(st1, checki - 1))
                elif suncheck == checki - 2 or int(checki / 2) < suncheck:
                    cool = str(add(st1, 0))
        else:
            hot = str(add(st1, suncheck - 1)) + " " + \
                str(add(st1, suncheck + 1))
            cool = str(add(st1, suncheck - 1)) + " " + \
                str(add(st1, suncheck + 1))
    print('Hot: ' + hot, 'Cool: ' + cool, sep="\n")
main()
