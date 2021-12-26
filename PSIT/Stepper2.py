"""Stepper II"""
def main():
    """Stepper II"""
    num_1 = int(input())
    num_2 = int(input())
    if num_1-num_2 < 0:
        step = 1
    else:
        step = -1
    for i in range(num_1, num_2+step, step):
        print(i)
main()
