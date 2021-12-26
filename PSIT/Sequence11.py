"""Sequence XI"""
def main():
    """sequence"""
    line_n = int(input())
    this_row = 1
    step_row = 1
    while this_row > 0:
        line = ""

        this_col = 1
        step_col = 1
        while this_col > 0:
            line += "%02d "%(min(this_row, this_col))

            if this_col == line_n:
                step_col = -1
            this_col += step_col
        print(line)
        if this_row == line_n:
            step_row = -1
        this_row += step_row

main()
