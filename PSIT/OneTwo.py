"""OneTwo"""
def main(num, ans='', ans1='1', ans2='2'):
    """OneTwo"""
    if num == 1 or num == 2:
        print(num)
    elif num >= 3:
        for _ in range(3, num+1):
            ans = ans2+ans1
            ans1, ans2 = ans2, ans
        print(ans)
main(int(input()))
