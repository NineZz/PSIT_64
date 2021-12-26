"""isprime_large"""
def main(num):
    """isprime_large"""
    if num == 1:
        return 'NO'
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return 'NO'
    return 'YES'
print(main(int(input())))
