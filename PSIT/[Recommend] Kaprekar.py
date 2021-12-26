"""[Recommend] Kaprekar"""
def arrange(line):
    """arrange"""
    for run_1 in range(4):
        for run_2 in range(4):
            if line[run_1] < line[run_2]:
                temp_line = ""
                for run_3 in range(4):
                    if run_3 == run_1:
                        temp_line += line[run_2]
                    elif run_3 == run_2:
                        temp_line += line[run_1]
                    else:
                        temp_line += line[run_3]
                line = temp_line
    return line

def main():
    """main"""
    line = input()
    counter = 0
    while line != "6174":
        line = arrange(line)
        line_reversed = line[::-1]
        line = "%04d"%(int(line_reversed)-int(line))
        counter += 1
    print(counter)
main()
