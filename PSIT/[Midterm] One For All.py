"""[Midterm] One For All"""
def main():
    """one for all"""
    number = int(input())
    i = 1
    name_num = ""
    while i < number+1:
        name = input()
        if i == number:
            name_num += name+"_%d"%i
        elif i%2 != 0:
            name_num += name+"*"*i
        elif i%2 == 0:
            name_num += name+"-"*i
        i += 1
    print(name_num)
main()
