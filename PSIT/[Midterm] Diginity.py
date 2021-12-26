"""[Midterm] Diginity"""
def main():
    """Diginity"""

    while True:
        line = input()
        if line == "0":
            break

        while True:
            point = 0
            for digit in line:
                point += int(digit)

            if len(str(point)) == 1:
                break
            line = str(point)
        print(point)
main()
