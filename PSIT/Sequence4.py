"""Sequence IV"""
def main():
    """function sequence"""
    number = int(input())

    runner = 1
    this_row = 1
    while this_row <= number:
        line = ""
        this_col = 1
        while this_col <= number:
            line += "%d "%runner
            runner += 1
            this_col += 1
        print(line.strip())
        this_row += 1
main()
