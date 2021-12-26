"""Diamond I"""
def main(deep, wide, diamond, val):
    """Diamond I"""
    for _ in range(deep):
        diamond.append(input().split())
    for j in range(wide):
        money = 0
        for i in range(deep):
            money += int(diamond[i][j])
        val.append(money)
        val.sort(reverse=True)
    print(val[0])
main(int(input()), int(input()), [], [])
