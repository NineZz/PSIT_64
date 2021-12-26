"""[Midterm] Sequence N"""
def main():
    """function loop"""
    number = int(input())
    for i in range(number):
        for j in range(number):
            if j == 0 or j == number-1 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
