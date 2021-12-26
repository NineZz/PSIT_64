"""Duplicate I"""
def main():
    """Duplicate I"""
    max_a = int(input())
    max_b = int(input())
    list_a = []
    list_b = []
    list_n = []
    for _ in range(max_a):
        list_a.append(input())
    for _ in range(max_b):
        list_b.append(input())
    for char in list_a:
        if char in list_b:
            list_n.append(char)
    if len(list_n) == 0:
        print("Nope")
    else:
        list_n.sort(reverse=True)
        print(*list_n, sep="\n")
main()
