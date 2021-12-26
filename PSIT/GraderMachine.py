"""GraderMachine"""
def main():
    """function sum"""
    start = int(input())
    stop = int(input())
    summary = 0
    pass_line = ""

    if start < stop:
        step = 1
    else:
        step = -1

    while True:
        if start%2 == 0:
            pass_line += "%d "%start
            summary += start
        if start == stop:
            break
        start += step

    print("pass : %s"%pass_line.strip())
    print("Sum : %d"%summary)
main()
