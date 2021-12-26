"""FibonacciRecursionV2"""
def func(val):
    """func"""
    if val == 1 or val == 0:
        return val
    else:
        return func(val-1)+func(val-2)
def main(num=int(input())):
    """FibonacciRecursionV12"""
    print(func(num))
main()
