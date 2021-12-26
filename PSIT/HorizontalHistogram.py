"""HorizontalHistogram"""
def main(val, low, upp):
    """HorizontalHistogram"""
    for i in val:
        if i.islower():
            low.add(i)
        elif i.isupper():
            upp.add(i)
    ans = sorted(list(low))
    ans.extend(sorted(list(upp)))
    for i in ans:
        k = ''
        for j in range(val.count(i)):
            if j%5 == 4 and j+1 != val.count(i):
                k += '-|'
            else:
                k += '-'
        print(i, ':', k)
main(input(), set(), set())
