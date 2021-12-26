"""Sequence VII"""
def main():
    """function sequence"""
    line_n = int(input())
    this_row = 1
    step = 1
    while this_row > 0:
        line = ""
        this_col = 1
        while this_col <= this_row:
            line += "%d "%this_col
            this_col += 1
        print(line)

        if this_row == line_n:
            step = -1
        this_row += step
main()
