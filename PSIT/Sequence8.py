"""Sequence VIII"""
def main():
    """function sequence"""
    line_n = int(input())
    this_row = 1
    while this_row <= line_n:
        line = "   "*(line_n-this_row)
        this_col = 1
        while this_col <= this_row:
            line += "%02d "%this_col
            this_col += 1
        print(line)
        this_row += 1
main()
