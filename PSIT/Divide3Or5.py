"""Divide3Or5"""
def main():
    """Divide3Or5"""
    num = int(input())
    ans = 0
    for i in range(num+1):
        if i%3 == 0 or i%5 == 0:
            ans += i
    print(ans)
main()
