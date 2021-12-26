"""SMS"""
def main(txt=''):
    """SMS"""
    button = {2:'ABC', 3:'DEF', 4:'GHI', 5:'JKL', 6:'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ'}
    for _ in range(int(input())):
        press = int(input())
        many = int(input())
        if press == 1:
            if len(txt)-many <= 0:
                txt = ''
            else:
                txt = txt[:(len(txt)-many)]
        elif press == 7 or press == 9:
            if many%4 == 0:
                txt += button[press][3]
            elif many%4 == 1:
                txt += button[press][0]
            elif many%4 == 2:
                txt += button[press][1]
            elif many%4 == 3:
                txt += button[press][2]
        else:
            if many%3 == 0:
                txt += button[press][2]
            elif many%3 == 1:
                txt += button[press][0]
            elif many%3 == 2:
                txt += button[press][1]
    print('null' if len(txt) == 0 else txt)
main()
