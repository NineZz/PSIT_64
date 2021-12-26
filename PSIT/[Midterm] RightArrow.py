"""[Midterm] RightArrow"""

def main():
    """[Midterm] RightArrow"""
    number_n = int(input()) #กว้าง
    number_m = int(input()) #สูง
    cut_number = number_m // 2
    for i in range(-cut_number, cut_number+1):
        count = abs(abs(i) - cut_number)
        print(' '*count, end='')
        for _ in range(number_n):
            txt = '*'
            print(txt, end='')
        print()
main()
