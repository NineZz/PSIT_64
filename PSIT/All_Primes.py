"""All_Primes"""
def main(num=int(input())):
    """All_Primes"""
    ans = num-1
    if num == 1:
        print(0)
    else:
        for i in range(2, num+1):
            k = 0
            for j in range(2, i):
                if i%j == 0:
                    k = 1
            ans -= k
        print(ans)
main()
