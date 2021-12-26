"""[Midterm] LargestNumber"""
def check_mx(num_x, num_y):
    """function checkmx"""
    if num_x > num_y:
        return num_x
    return num_y

def main():
    """function largest"""
    num_1 = input()
    num_2 = input()
    num_3 = input()
    answer = int(num_1+num_2+num_3)
    answer = check_mx(answer, int(num_1+num_3+num_2))
    answer = check_mx(answer, int(num_2+num_1+num_3))
    answer = check_mx(answer, int(num_2+num_3+num_1))
    answer = check_mx(answer, int(num_3+num_2+num_1))
    answer = check_mx(answer, int(num_3+num_1+num_2))
    return answer
print(main())
