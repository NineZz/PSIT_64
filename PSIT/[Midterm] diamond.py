"""[Midterm] diamond"""
def main():
    """diamond"""
    size = int(input())
    half = size//2
    for row in range(size):
        for col in range(size):
            if half == col+row or half == col-row or half == row or \
                half == row-col or col == size-row+half-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
