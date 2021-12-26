"""Ink"""
def main(val=input().split()):
    """Ink"""
    import math
    for _ in range(int(val[1])):
        home = input().split()
        dis = ((int(home[0])**2+int(home[1])**2)**0.5)**2
        print(math.ceil(3.1416*dis/int(val[0])))
main()
