"""Sequence I"""
def main():
    """function mxn"""
    num_m = int(input())
    num_n = int(input())
    for i in range(num_m):
        for j in range(num_n):
            print((i*num_n)+j+1, end=" ")
        print()
main()
