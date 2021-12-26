"""Seeker"""
def main():
    """main func"""
    text = input() + " "
    num = ""
    num_sum = 0
    check = 0
    for i in text:
        if i.isdigit() == True:
            num += i
            check = 1
        else:
            if check == 1:
                num_sum += int(num)
                num = ""
                check = 0
    print(num_sum)
main()
