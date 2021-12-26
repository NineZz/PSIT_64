"""SumOfNumber"""
def main():
    """function sum"""
    sum_number = 0
    target = int(input())
    while True:
        number = int(input())
        if number == -1:
            break
        sum_number += number
        if sum_number == target:
            break
    print(sum_number)
main()
