"""[Midterm] Lotto"""
def main():
    """[Midterm] Lotto"""
    first_p = input()
    if first_p == "000000":
        first_p_close_2 = "000001"
        first_p_close_1 = "999999"
    elif first_p == "999999":
        first_p_close_2 = "000000"
        first_p_close_1 = "999998"
    else:
        first_p_close_1 = "%06d"%(int(first_p)-1)
        first_p_close_2 = "%06d"%(int(first_p)+1)
    sec_p = input()
    thr_f_p_1 = input()
    thr_f_p_2 = input()
    thr_b_p_1 = input()
    thr_b_p_2 = input()
    lotto = input()

    total_prize = 0
    if lotto == first_p:
        total_prize += 6000000
    if lotto == first_p_close_1:
        total_prize += 100000
    if lotto == first_p_close_2:
        total_prize += 100000
    if lotto[-2:] == sec_p:
        total_prize += 2000
    if lotto[:3] == thr_f_p_1:
        total_prize += 4000
    if lotto[:3] == thr_f_p_2:
        total_prize += 4000
    if lotto[-3:] == thr_b_p_1:
        total_prize += 4000
    if lotto[-3:] == thr_b_p_2:
        total_prize += 4000
    print(total_prize)
main()
