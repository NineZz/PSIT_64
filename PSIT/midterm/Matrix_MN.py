"""Matrix_MN"""
def matrix():
    """Matrix_MN"""
    row = int(input())
    col = int(input())

    num_list = []
    for _ in range(row*col):
        text = input()
        num_list.append(text)

    count = 0
    for start in range(row*col):
        print(num_list[start], end=" ")
        count += 1
        if count % col == 0:
            print()


matrix()
