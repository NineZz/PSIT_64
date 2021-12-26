"""Align"""
def main():
    """function size"""
    number = int(input())
    side = input()
    word = input()
    num_word = len(word)
    num_1 = number-num_word
    num_2 = num_1//2
    if side == "left":
        print(word+" "*num_1)
    elif side == "right":
        print(" "*num_1+word)
    elif side == "center":
        if num_1%2 != 0:
            print(" "*(num_2+1)+word+" "*num_2)
        elif num_1%2 == 0:
            print(" "*num_2+word+" "*num_2)
main()
