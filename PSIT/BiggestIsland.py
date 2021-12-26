"""BiggestIsland"""


def chang(lst, lstresult):
    """BiggestIsland"""
    lff, counttest = [], []
    lstresult[len(lstresult) - 1] = []
    countfirst = lstresult[len(lstresult) - 1]
    lstresult[len(lstresult) - 1] = []
    if lstresult[int(lst[0]) - 1][int(lst[1]) + 1] == '1':
        lff.append([int(lst[0]) - 1, int(lst[1]) + 1])
    if lstresult[int(lst[0]) - 1][int(lst[1]) + 0] == '1':
        lff.append([int(lst[0]) - 1, int(lst[1]) + 0])
    if lstresult[int(lst[0]) - 1][int(lst[1]) - 1] == '1':
        lff.append([int(lst[0]) - 1, int(lst[1]) - 1])
    if lstresult[int(lst[0])][int(lst[1]) + 1] == '1':
        lff.append([int(lst[0]), int(lst[1]) + 1])
    if lstresult[int(lst[0])][int(lst[1]) - 1] == '1':
        lff.append([int(lst[0]), int(lst[1]) - 1])
    if lstresult[int(lst[0]) + 1][int(lst[1]) + 1] == '1':
        lff.append([int(lst[0]) + 1, int(lst[1]) + 1])
    if lstresult[int(lst[0]) + 1][int(lst[1]) + 0] == '1':
        lff.append([int(lst[0]) + 1, int(lst[1]) + 0])
    if lstresult[int(lst[0]) + 1][int(lst[1]) - 1] == '1':
        lff.append([int(lst[0]) + 1, int(lst[1]) - 1])
    for iff in lff:
        lstresult[iff[0]][iff[1]] = '0'
        counttest.append([iff[0], iff[1]])
        lstresult = chang(iff, lstresult)
        counttest.extend(lstresult[len(lstresult) - 1])
    lstresult[len(lstresult) - 1] = countfirst + counttest
    return lstresult

def main():
    """BiggestIsland"""
    st1, lst2, lsttest, countf = input().split(), [], [], []
    for _ in range(int(st1[0])):
        st2 = input().split()
        st2.insert(0, 0)
        st2.append(int(0))
        lst2.append(st2)
    for _ in range(int(st1[1]) + 2):
        lsttest.append(str('0'))
    lst2.insert(0, lsttest)
    lst2.append(lsttest)
    lsttest = []
    lst2.append(1150)
    lst2.append(0)
    for j in range(1, int(st1[1]) + 1):
        for i in range(1, int(st1[0]) + 1):
            if int(lst2[i][j]) == 1:
                lst2 = chang([i, j], lst2)
                lstff = []
                lst2[len(lst2) - 1].append([i, j])
                for iff in lst2[len(lst2) - 1]:
                    if iff not in lstff:
                        lstff.append(iff)
                countf.append(int(len(lstff)))
                lst2[len(lst2) - 1] = 0
    print(max(countf))
main()
