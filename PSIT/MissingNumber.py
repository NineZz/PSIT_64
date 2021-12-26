"""MissingNumber"""
def main():
    """MissingNumber"""
    max_input = int(input())
    num_list = []
    while max_input > 0:
        number = int(input())
        num_list.append(number)
        if number == 0:
            break
    sort_list = sorted(num_list)
    min_num = min(num_list)
    for i in range(min_num, max_input+1):
        if i not in sort_list:
            print(i)
main()
