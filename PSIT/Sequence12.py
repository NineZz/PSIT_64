"""Sequence XII"""

def main():
    """Sequence XII"""
    line_n = int(input())

    this_row = 0
    step_row = 1
    while this_row >= 0:
        line = ""

        runner = line_n-this_row
        step_runner = 1

        this_col = 0
        step_col = 1
        while this_col >= 0:
            line += "%02d "%(runner)
            if runner == line_n:
                step_runner = -1
            elif this_col == line_n-1:
                step_runner = 1
            runner += step_runner

            if this_col == line_n-1:
                step_col = -1
            this_col += step_col
        print(line)
        if this_row == line_n-1:
            step_row = -1
        this_row += step_row

main()
