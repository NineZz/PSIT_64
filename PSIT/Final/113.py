"""113"""
def main():
    """func main"""
    lines = input()
    while True:
        lines = lines.replace("113", "")
        if lines.count("113") == 0:
            print(lines)
            break
main()
