"""3nPlus1"""
def main():
    """3nPlus1"""
    while True:
        num = int(input())
        if num == 0:
            break
        count = 1
        while num != 1:
            if num%2 == 0:
                num = num/2
            else:
                num = num*3+1
            count += 1
        print(count)
main()
