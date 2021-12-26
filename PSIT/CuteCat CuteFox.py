
"""CuteCat CuteFox"""
def fewthepza(dictfew, fewza):
    """CuteCat CuteFox"""
    return len([few for few in dictfew.values() if fewza in few])

def main():
    """CuteCat CuteFox"""
    num1, dictfew, fewresult = int(input()), {}, {}
    for _ in range(num1):
        fewza = str(input())
        if len(fewza.split('"')) > len(fewza.split("'")):
            dictfew[fewza.split('"')[1]] = fewza.split('"')[3]
        else:
            dictfew[fewza.split("'")[1]] = fewza.split("'")[3]
    countcat, countfox = fewthepza(dictfew, "Cat"), fewthepza(dictfew, "Fox")
    checkcat, checkfox, countfew = "Cat01" in dictfew.values(), "Fox01" in dictfew.values(), 0
    if countcat == 0 or checkcat == 0:
        fewresult["Garfield"] = "Cat01"
    if countfox == 0 or checkfox == 0:
        fewresult["Fubuki"] = "Fox01"
    for key, value in sorted(dictfew.items(), key=lambda x: x[1]):
        if checkfox == 0 and value.count("Fox") >= 1 and countfew == 0:
            countfew += 1
            fewresult["Fubuki"] = "Fox01"
        fewresult[key] = value
    countcat, countfox = fewthepza(
        fewresult, "Cat"), fewthepza(fewresult, "Fox")
    cat, fox = {}, {}
    for key, value in fewresult.items():
        if value.count("Cat") >= 1:
            cat.update({int(value.split("Cat")[1]): [key, value]})
        elif value.count("Fox") >= 1:
            fox.update({int(value.split("Fox")[1]): [key, value]})
    print("Cat : %d\nFox : %d" % (countcat, countfox))
    for cry in sorted(cat):
        print(cat[cry][0] + " : " + cat[cry][1])
    for cry in sorted(fox):
        print(fox[cry][0] + " : " + fox[cry][1])
main()
