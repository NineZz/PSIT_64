"""Sequence II"""
def main():
    """function sequence"""
    number = int(input())
    for i in range(number):
        for j in range(number):
            print(i+(number*j), end=" ")
        print()
main()
