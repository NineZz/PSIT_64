"""BookWorm"""

def main(num1):
    """BookWorm"""
    lst = []
    for _ in range(num1):
        num2, count, lste = float(input()), 0, []
        for _ in range(int(input())):
            lste.append(float(input()))
        for i in sorted(lste):
            if num2 >= i:
                num2 -= i
                count += 1
        lst.append(count)
    print(*lst, sep="\n")
main(int(input()))
