"""RockPaperScissor"""
def main():
    """RockPaperScissor"""
    a_point = 0
    b_point = 0

    line = input()
    for runner in range(0, len(line)-1, 2):

        both_in = line[runner:runner+2]

        if both_in == "RS":
            a_point += 1
        if both_in == "RP":
            b_point += 1
        if both_in == "SP":
            a_point += 1
        if both_in == "SR":
            b_point += 1
        if both_in == "PR":
            a_point += 1
        if both_in == "PS":
            b_point += 1

    if a_point > b_point:
        print("A win %d-%d"%(a_point, b_point))
    elif b_point > a_point:
        print("B win %d-%d"%(b_point, a_point))
    else:
        print("DRAW %d"%a_point)
main()
