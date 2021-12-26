"""ChristmasTree"""
def main():
    """Tree"""
    line_n = int(input())
    line_k = int(input())
    wood = (" "*(line_n-2)+"---"+"\n")*line_k
    this_row = 1
    while this_row <= line_n:
        line = " "*(line_n-this_row)
        this_col = 1
        step = 1
        while this_col > 0:
            line += "*"
            if this_col == this_row:
                step = -1
            this_col += step
        print(line)
        this_row += 1
    print(wood)
main()
