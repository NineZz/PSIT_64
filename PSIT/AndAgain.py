"""AndAgain"""
def main(val, lst):
    """AndAgain"""
    for i in val:
        i = i.lower()
        if i.count('a')+i.count('e')+i.count('i')+i.count('o')+i.count('u') >= 2:
            lst.append(i)
    lst.sort()
    if lst == []:
        print('Nope')
    else:
        for i in lst:
            print(i)
main((input().replace('.', '')).split(), [])
