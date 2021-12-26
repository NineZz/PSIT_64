"""Binary"""
def main():
    """bbbb"""
    num = int(input())
    ans = 0
    counter = 0
    mod = num
    while mod > 0:
        ans = ((mod%2)*(10**counter)) + ans
        mod = int(mod/2)
        counter += 1
    print(ans)
main()
