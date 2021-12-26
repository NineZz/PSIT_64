"""HowLong"""
def digits(num_x):
    """function digit"""
    num_x = abs(num_x)
    if num_x < 10:
        return 1
    return 1 + digits(num_x / 10)

def main():
    """function long"""
    print(digits(int(input())))
main()
