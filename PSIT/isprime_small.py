"""isprime_small"""
def main():
    """prime"""
    num = int(input())
    prime = 0
    if num > 1:
        for i in range(2, int(num*0.5) + 1):
            if num % i == 0:
                prime = 1
                break
        if prime == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main()
