"""Sequence III"""
def main():
    """function sequence"""
    number = int(input())
    for i in range(2, number+2):
        for j in range(number):
            print(i+j, end=" ")
        print()
main()
