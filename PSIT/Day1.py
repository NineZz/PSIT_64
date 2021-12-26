"""Day I"""
def main():
    """function leap year"""
    year = int(input())
    if year%100 == 0:
        if year%400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        if year%4 == 0:
            print("Yes")
        else:
            print("No")
main()
