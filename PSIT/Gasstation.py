"""GasStations"""
def main(goal, status, all_gas, count):
    """GasStations"""
    remain = status
    if len(all_gas) != 0:
        all_gas += [all_gas[-1]]
    for i in range(len(all_gas) - 1):
        if all_gas[i] > remain:
            break
        elif (all_gas[i] < remain and all_gas[i + 1] <= remain) or all_gas[i] >= goal:
            pass
        else:
            count += 1
            remain = all_gas[i] + status
    print("depleted" if remain < goal else count)
main(float(input()), float(input()), [float(input()) for _ in range(int(input()))], 0)
