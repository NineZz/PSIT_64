"""CoPrimeV1"""
def main():
    """CoPrimeV1"""
    num_1 = int(input())
    num_2 = int(input())
    num_list = []
    for i in range(1, 10001):
        if num_1%i == 0 and num_2%i == 0:
            num_list.append(i)
    ans = max(num_list)
    if ans == 1:
        print("YES")
        print(ans)
    else:
        print("NO")
        print(ans)
main()
