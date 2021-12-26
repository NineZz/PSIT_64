"""Scout"""
def main():
    """Scout"""
    for i in range(int(input())):
        num1 = input().split()
        num2 = input().split()
        ans = 0
        check = 0
        for i in sorted(num2):
            if ans < int(num1[1]) and check + int(i) <= int(num1[2]) and ans < int(num1[0]):
                ans += 1
                check += int(i)
        print(ans)
        ans, check = 0, 0
main()
