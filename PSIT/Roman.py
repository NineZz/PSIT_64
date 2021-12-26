"""Roman"""
def add(alp):
    '''add'''
    if alp == 'M':
        return 1000
    elif alp == 'D':
        return 500
    elif alp == 'C':
        return 100
    elif alp == 'L':
        return 50
    elif alp == 'X':
        return 10
    elif alp == 'V':
        return 5
    elif alp == 'I':
        return 1
def main(val=input(), ans=0, check=90000000):
    """Roman"""
    for i in val:
        num = add(i)
        if num <= check:
            ans += num
        else:
            ans += -check*2+num
        check = num
    print(ans)
main()
