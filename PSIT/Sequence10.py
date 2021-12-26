"""Sequence X"""
def main():
    """function sequence"""
    line_n = int(input())
    this_row = 1
    step_row = 1
    while this_row > 0:
        line = "   "*(line_n-this_row)
        this_col = 1
        step_col = 1
        while this_col > 0:
            line += "%02d "%this_col
            if this_col == this_row:
                step_col = -1
            this_col += step_col
        print(line)
        if this_row == line_n:
            step_row = -1
        this_row += step_row
main()
