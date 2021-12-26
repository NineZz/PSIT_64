"""[Midterm] Key"""
def main():
    """function key"""
    number = int(input())
    sum_num1 = 0
    while True:
        for i in str(number):
            sum_num1 += int(i)
        break
    numx10 = (number%10**3)*10
    sum_num2 = sum_num1+numx10
    if sum_num2 >= 1000:
        print("%04d"%(sum_num2%10**4))
    elif sum_num2 < 1000:
        print(1000+sum_num2)
main()
