"""AscendingSort"""
def main():
    """AscendingSort"""
    num_list = []
    count = 0
    while count < 5:
        number = int(input())
        num_list.append(number)
        count += 1
    num_list.sort()
    for char in num_list:
        print(char)
main()
