"""[Midterm] Stair"""
def main():
    """[Midterm] Stair"""
    cumulative_case = 0
    step = 0
    reach = int(input())
    staircase = int(input())
    is_unreachable = False
    for _ in range(staircase):
        each_case = int(input())
        if cumulative_case+each_case > reach:
            if each_case > reach:
                is_unreachable = True
                break
            else:
                step += 1
                cumulative_case = each_case
        else:
            cumulative_case += each_case
    if cumulative_case <= reach:
        step += 1

    if is_unreachable:
        print("NO")
    else:
        print(step)
main()
