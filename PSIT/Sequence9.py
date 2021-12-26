"""Sequence IX"""
def main():
    """function sequence"""
    line_n = int(input())
    this_row = 1
    while this_row <= line_n:
        line = "   "*(line_n-this_row)
        this_col = 1
        step = 1
        while this_col > 0:
            line += "%02d "%this_col
            if this_col == this_row:
                step = -1
            this_col += step
        print(line)
        this_row += 1
main()
