"""BreachTheDoor"""
def main(val, ans):
    """BreachTheDoor"""
    for i in range(len(val)):
        key = ''
        for j in val[i]:
            if j.isalpha():
                key += j
        if len(key) > 6:
            ans.append(key)
    print(*ans)
main(input().split(), [])
