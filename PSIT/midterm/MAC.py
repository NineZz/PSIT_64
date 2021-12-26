"""MAC"""
def add(val):
    '''add'''
    chck = len(val)
    for i in val.lower():
        if i == 'a' or i == 'b' or i == 'c' or i == 'd' or i == 'e' or i == 'f' or i.isnumeric():
            chck -= 1
    return 1 if chck == 0 else 0
def main(data):
    """MAC"""
    if (data[2::3] == '-----') and (len(data)-5 == 12):
        check = add(data.replace('-', ''))
        print('VALID 1' if check == 1 else 'ERROR')
    elif (data[2::3] == ':::::') and (len(data)-5 == 12):
        check = add(data.replace(':', ''))
        print('VALID 2' if check == 1 else 'ERROR')
    elif (data[4::5] == '..') and (len(data)-2 == 12):
        check = add(data.replace('.', ''))
        print('VALID 3' if check == 1 else 'ERROR')
    else:
        print('ERROR')
main(input())
