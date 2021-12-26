"""B - Fully pair?"""
def check(lines, char):
    """check"""
    count_1 = lines.count(char)
    if count_1%2 == 0:
        return ""
    return char

def main():
    """B - Fully pair?"""
    lines = input()
    alone = ""
    while len(lines) != 0:
        alone += check(lines, lines[0])
        lines = lines.replace(lines[0], "")
    if len(alone) == 0:
        print("fully paired")
    else:
        print(alone)
main()
