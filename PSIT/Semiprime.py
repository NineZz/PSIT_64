"""Semi Prime"""
import math
def isSemiPrime(number):
    """Semi Prime"""
    result = False
    primes = []
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            number = int(number / i)
            primes.append(i)
            if len(primes) >= 2:
                break
    if number > 1:
        primes.append(number)
    if len(primes) == 2:
        result = True
        n = primes[0] * primes[1]
        print(f"{primes[0]} * {primes[1]} = {n}")
    return result
number = 33

print(isSemiPrime(int(input())))