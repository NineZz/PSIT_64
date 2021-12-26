"""Dart"""
def main(score=0):
    """Dart"""
    for _ in range(int(input())):
        point = input().split()
        dis = ((int(point[0]))**2+(int(point[1]))**2)**0.5
        score = score+5 if dis <= 2 else score+4 if dis <= 4 else score+3 if dis <= 6 else \
            score+2 if dis <= 8 else score+1 if dis <= 10 else score+0
    print(score)
main()
