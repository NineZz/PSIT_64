"""Century"""
import math
def main():
    """Century"""
    max_input = int(input())
    for _ in range(max_input):
        years = input()
        if years[:4] == "B.E.":
            years = int(years[5:]) - 543
        else:
            years = int(years[5:])

        if years <= 0:
            years = "ERROR"
        elif 1 <= years <= 100:
            years = 1
        else:
            years = math.ceil(years/100)
        print(years)
main()
