"""FOR!F-Ball"""
def main():
    """ball"""
    position = 1
    line = input()
    for char in line:
        if char == "A":
            if position == 1:
                position = 2
            elif position == 2:
                position = 1
        if char == "B":
            if position == 2:
                position = 3
            elif position == 3:
                position = 2
        if char == "C":
            if position == 1:
                position = 3
            elif position == 3:
                position = 1
    print(position)
main()
