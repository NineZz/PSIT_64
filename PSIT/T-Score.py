"""T-Score"""
def main():
    """T-Score"""
    number = int(input())
    max_score = int(input())
    z_list = []
    score_lst = []
    for _ in range(number):
        score = int(input())
        if score <= max_score:
            score_lst.append(score)
    sum_score = sum(score_lst)
    avg_x = sum_score/number
    sd_x = (((number*(sum_score**2)) - (sum_score**2))/(number*(number-1)))**0.5
    if sd_x == 0:
        print(('50.00'+'\n')*number)
    else:
        for i in score_lst:
            ans = (i-avg_x)/sd_x
            z_list.append(ans)
        for j in z_list:
            print('%.2f'%(50+(10*j)))
main()
