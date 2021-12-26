"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def check_mx(num_x, num_y):
    """function check max"""
    return num_x > num_y and num_x or num_y

def check_mn(num_x, num_y):
    """function check min"""
    return num_x < num_y and num_x or num_y

def main(word, num_1, num_2, num_3):
    """function main"""
    num_list = [num_1, num_2, num_3]
    num_mx = check_mx(check_mx(num_1, num_2), num_3)
    num_mn = check_mn(check_mn(num_1, num_2), num_3)
    num_list.remove(num_mx)
    num_list.remove(num_mn)
    if word == "Ascend":
        print("%.2f, %.2f, %.2f"%(num_mn, num_list[0], num_mx))
    elif word == "Descend":
        print("%.2f, %.2f, %.2f"%(num_mx, num_list[0], num_mn))
main(input(), float(input()), float(input()), float(input()))
