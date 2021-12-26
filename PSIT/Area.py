"""Area"""
def area():
    """function area"""
    number = int(input())
    ans = 0
    while number > 0:
        word = input().replace(" ", "")
        ans += len(word)
        number -= 1
    print(ans)
area()
