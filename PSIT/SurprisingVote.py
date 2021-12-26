"""SurprisingVote"""
def main():
    """function Surprising"""
    sum_num = float(input())
    num_max = float(input())
    if num_max-(sum_num-2*(sum_num/2)) <= 2:
        print("Not surprising")
    elif num_max-(sum_num-2*num_max) <= 2:
        print("Not surprising")
    else:
        print("Surprising")
main()
