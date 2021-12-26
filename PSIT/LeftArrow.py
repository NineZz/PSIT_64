"""LeftArrow"""
def main():
    """function arrow"""
    num_1 = int(input())
    num_2 = int(input())
    for i in range(num_2):
        num_3 = abs((num_2//2)-i)
        print((" "*num_3)+("*"*num_1))
main()
