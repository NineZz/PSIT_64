"""LineSorting"""
def main():
    """LineSorting"""
    my_list = []
    line = int(input())
    for _ in range(line):
        word = input()
        my_list.append(word)
        sort_list = sorted(my_list, key=len)
        if line == len(my_list):
            break
    for i in sort_list:
        print(i)
main()
