"""BrickBridge"""
def main():
    """function bridge"""
    num_1 = int(input())
    num_5 = int(input())
    num_max = int(input())

    num_5_need = num_max//5
    remain = num_max%5

    if num_5 >= num_5_need:
        if remain == 0:
            return 0
        if num_1 >= remain:
            return remain
        return -1
    remain = num_max-num_5*5

    if num_1 >= remain:
        return remain
    return -1

print(main())
