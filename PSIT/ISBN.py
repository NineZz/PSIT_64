"""ISBN"""
def main():
    """ISBN"""
    number = input().replace('-', '').replace(' ', '')
    result = 0
    count = 10
    for i in number:
        if count == 1:
            break
        result += int(i)*count
        count -= 1
    result = (-result)%11
    if int(number[9]) == result:
        print("Yes")
    else:
        if result >= 10:
            print("No X")
        else:
            print("No %d" %result)

main()
