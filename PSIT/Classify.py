"""Classify"""
def add(data):
    '''add'''
    check = ''
    for i in range(len(data)):
        if i == 0 or data[i][:2] != check:
            print(data[i])
            check = data[i][:2]
        else:
            print('--'+data[i][2:])
def main(val, j, almost):
    """Classify"""
    while True:
        code = input()
        if code == 'END':
            break
        val.append(int(code))
        val.sort()
    for i in range(len(val)):
        ans = str(val[i]//1000000)+' '+str(int(str(val[i]//10000)[2:]))
        if i == 0:
            num = ans
        else:
            if ans == num:
                j += 1
            else:
                almost.append(num+' '+str(j))
                num = ans
                j = 1
    almost.append(ans+' '+str(j))
    add(almost)
main([], 1, [])
