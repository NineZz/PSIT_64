"""[Midterm] Harshad"""
def main():
    """Yay"""
    for _ in range(10):
        this_num = input()
        summary = 0
        for char in this_num.strip("-"):
            if char == "0":
                continue
            summary += int(char)

        if this_num != "0" and int(this_num)%summary == 0:
            print("Yes")
        else:
            print("No")
main()
