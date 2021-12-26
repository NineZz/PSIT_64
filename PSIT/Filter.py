"""Filter"""
import json
def main():
    """main"""
    dictfew, money, fewresult = json.loads(str(input())), float(input()), {}
    for i in sorted(dictfew):
        if float(dictfew[str(i)]) >= float(money):
            fewresult[str(i)] = float(dictfew[str(i)])
    if len(fewresult) == 0:
        print("Nope")
    else:
        for key, value in fewresult.items():
            print("%s	%.2f" % (key, float(value)))
main()
