"""MultiplyMatrixPQR"""
def addlist(num_1, num_2, lst_0):
    """MultiplyMatrixPQR"""
    for _ in range(num_1):
        lst_1 = []
        for _ in range(num_2):
            num = int(input())
            lst_1.append(num)
        lst_0.append(lst_1)
    return lst_0

def main():
    """main"""
    num_1, num_2, num3 = int(input()), int(input()), int(input())
    a_lst = addlist(num_1, num_2, [])
    b_lst = addlist(num_2, num3, [])
    for i in a_lst:
        for j in range(len(b_lst[0])):
            sum_num, count = 0, 0
            for k in i:
                sum_num += k * int(b_lst[count][j])
                count += 1
            print(sum_num, end=" ")
        print()
main()
