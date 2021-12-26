"""Sequence V"""
def main():
    """function sequence"""
    number = int(input())
    counter = 0
    line = ""
    runner = number
    while runner > 0:
        counter += 1
        line += "%s "%runner
        if counter == 7:
            line += "\n"
            counter = 0
        runner -= 1
    print(line.strip())
main()
