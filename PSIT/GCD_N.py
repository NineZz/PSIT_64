"""GCD_N"""
def main():
    """GCD_N"""
    num_n = int(input())
    num_list = []
    for _ in range(num_n):
        num_list.append(int(input()))
    for i in range(1, 10001):
        for number in num_list:
            if number%i == 0:
                num_list.append(i)
    ans = max(num_list)
    print(ans)
main()
