"""Median"""
import math
def main():
    """Median"""
    max_input = int(input())
    num_list = []
    for _ in range(max_input):
        number = int(input())
        num_list.append(number)
    sort_list = sorted(num_list)
    if max_input%2 != 0:
        mids = math.ceil(max_input/2)
        print("%.1f"%sort_list[mids-1])
    elif max_input%2 == 0:
        mid_1 = int(max_input/2)
        mid_2 = mid_1+1
        ans = (float(sort_list[mid_1-1]) + float(sort_list[mid_2-1]))/2
        print("%.1f"%ans)
main()
