"""GCD_v1"""
def main():
    """GCD_v1"""
    num_1 = int(input())
    num_2 = int(input())
    num_list = []
    for i in range(1, 1001):
        if num_1%i == 0 and num_2%i == 0:
            num_list.append(i)
    ans = max(num_list)
    print(ans)
main()
