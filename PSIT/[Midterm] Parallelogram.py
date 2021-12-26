"""[Midterm] Parallelogram"""
def main():
    """[Midterm] Parallelogram"""
    lines = input()
    lenght = len(lines)
    for i in range(1, lenght*2):
        print(" "*(lenght-i)+lines[max(0, i-lenght):i])
main()
