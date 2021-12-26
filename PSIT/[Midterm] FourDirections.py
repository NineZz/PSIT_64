"""[Midterm] FourDirections"""
def get(direction, line):
    """[Midterm] FourDirections"""
    if direction == "U":
        return get_up(line)
    if direction == "D":
        return get_down(line)
    if direction == "L":
        return get_left(line)
    if direction == "R":
        return get_right(line)
def get_up(line):
    """up"""
    if line == 1:
        return "  *  "
    if line == 2:
        return " *** "
    if line == 3:
        return "* * *"
    if line == 4:
        return "  *  "
    if line == 5:
        return "  *  "
def get_down(line):
    """down"""
    if line == 1:
        return "  *  "
    if line == 2:
        return "  *  "
    if line == 3:
        return "* * *"
    if line == 4:
        return " *** "
    if line == 5:
        return "  *  "
def get_left(line):
    """left"""
    if line == 1:
        return "  *  "
    if line == 2:
        return " *   "
    if line == 3:
        return "*****"
    if line == 4:
        return " *   "
    if line == 5:
        return "  *  "
def get_right(line):
    """right"""
    if line == 1:
        return "  *  "
    if line == 2:
        return "   * "
    if line == 3:
        return "*****"
    if line == 4:
        return "   * "
    if line == 5:
        return "  *  "
def main():
    """main"""
    line = input()
    for n_line in range(1, 6):
        sx_line = ""
        for char in line:
            sx_line += get(char, n_line)+" "
        print(sx_line.rstrip())
main()
