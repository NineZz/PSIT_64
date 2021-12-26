"""RunGame"""
def main():
    """RunGame"""
    line = input().split()
    ans = 0
    keep = 0
    for i in line:
        ans = abs(int(i) - ans)
        keep += ans
        ans = int(i)
    print(keep)
main()
