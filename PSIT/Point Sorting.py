"""Point Sorting"""
def main():
    """main"""

    list_x = []
    duo = []

    for i in range(int(input())):
        for _ in range(int(input())):
            ans = (input().split())
            for i in ans:
                duo.append(int(i))
            list_x.append(duo)
            duo = []
        list_x = sorted(list_x, key=lambda x: x[1], reverse=True)
        list_x = sorted(list_x, key=sum)
        for i in list_x:
            for j in i:
                print(j, end=" ")
            print()
        list_x = []

main()
