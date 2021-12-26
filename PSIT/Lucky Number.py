"""Lucky Number"""
def number():
    """Lucky Number"""
    num_1 = int(input())
    num_lst = []
    for num in range(1, num_1+1):
        num_lst.append(num)
    for i in range(num_1//2):
        num_lst.pop(i+1)
    for j in range(2, ((num_1//2)-2), 2):
        num_lst.pop(j)
    for k in range(6, ((num_1//2)-4), 2):
        num_lst.pop(k)
    print(*num_lst)
number()
